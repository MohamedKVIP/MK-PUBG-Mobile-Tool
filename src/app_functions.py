import os
import shutil
import subprocess
import sys
import winreg
import xml.etree.ElementTree as ET
from shutil import copy
from time import sleep

import GPUtil
import adbutils
import psutil
import pythoncom
import tempfile
import winshell
import wmi
from PyQt5.QtCore import QSettings
from win32api import EnumDisplayDevices, EnumDisplaySettings
from win32com.client import Dispatch


class Settings:
    def __init__(self):
        self.settings = QSettings("MK Apps", "MK PUBG Mobile Tool")
        self.REG_PATH = r'SOFTWARE\Tencent\MobileGamePC'
        self.pubg_versions = {
            "com.tencent.ig": "PUBG Mobile Global",
            "com.vng.pubgmobile": "PUBG Mobile VN",
            "com.rekoo.pubgm": "PUBG Mobile TW",
            "com.pubg.krmobile": "PUBG Mobile KR",
            "com.pubg.imobile": "Battlegrounds Mobile India"}

    @staticmethod
    def kill_adb():
        """
        Kills the ADB (Android Debug Bridge) process if it is currently running.
        """
        try:
            subprocess.run(["taskkill", "/F", "/IM", "adb.exe"], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    # Get Script Run Location
    @staticmethod
    def resource_path(relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath('.'))
        return os.path.join(base_path, relative_path)


class Registry(Settings):
    def get_reg(self, name):
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.REG_PATH, 0, winreg.KEY_READ) as registry_key:
                value, regtype = winreg.QueryValueEx(registry_key, name)
                return value
        except FileNotFoundError:
            return None

    @staticmethod
    def get_local_reg(name, path="AppMarket"):
        """
        Get the value of a registry key in the local machine.
        """
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                rf'SOFTWARE\WOW6432Node\Tencent\MobileGamePC\{path}') as registry_key:
                value, regtype = winreg.QueryValueEx(registry_key, name)
                return value
        except OSError:
            return None

    def set_dword(self, name, value):
        """
        Set the value of a DWORD in the Windows registry.
        """
        try:
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.REG_PATH) as registry_key:
                winreg.SetValueEx(registry_key, name, 0, winreg.REG_DWORD, value)
            return True
        except WindowsError:
            return False


class Optimizer(Registry):

    @staticmethod
    def kill_gameloop():
        """
        Kills a list of processes related to the gameloop.

        Returns:
            - True if at least one process was killed.
            - False if no process was killed.
        """
        # List of processes to be killed
        processes_to_kill = [
            'aow_exe.exe',  # Process 1
            'AndroidEmulatorEn.exe',  # Process 2
            'AndroidEmulator.exe',  # Process 3
            'AndroidEmulatorEx.exe',  # Process 4
            'TBSWebRenderer.exe',  # Process 5
            'syzs_dl_svr.exe',  # Process 6
            'AppMarket.exe',  # Process 7
            'QMEmulatorService.exe',  # Process 8
            'RuntimeBroker.exe',  # Process 9
            'GameLoader.exe',  # Process 10
            'TSettingCenter.exe',  # Process 11
            'Auxillary.exe',  # Process 12
            'TP3Helper.exe',  # Process 13
            'tp3helper.dat',  # Process 14
            'GameDownload.exe'  # Process 15
        ]

        # Counter to track number of processes killed
        processes_killed = 0

        # Loop through each process in the list and kill them
        for process in processes_to_kill:
            result = subprocess.run(['taskkill', '/F', '/IM', process, '/T'], stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL)
            if result.returncode == 0:
                processes_killed += 1

        # If at least one process was killed, return True; otherwise, return False
        return processes_killed >= 1

    def add_to_windows_defender_exclusion(self):
        """
        Adds the directory of the game loop to the Windows Defender exclusion list.
        """
        gameloop_path = os.path.dirname(self.get_local_reg("InstallPath"))
        command = ["powershell", "-Command", f"Add-MpPreference -ExclusionPath '{gameloop_path}' -Force"]
        subprocess.call(command)

    @staticmethod
    def change_dns_servers(dns_servers):
        """
        Change the DNS servers for all network adapters.
        """
        pythoncom.CoInitialize()  # Initialize the COM library

        wmi_api = wmi.WMI()  # Create a WMI API object

        # Retrieve all network adapters
        adapters = wmi_api.Win32_NetworkAdapterConfiguration(IPEnabled=True)

        success = all(adapter.SetDNSServerSearchOrder(dns_servers)[0] == 0 for adapter in adapters)

        # Flush DNS cache
        subprocess.run(['ipconfig', '/flushdns'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)

        return success

    def optimize_for_nvidia(self):
        nvidia_profile_path = self.resource_path("assets/mk.nip")

        def change_nvidia_profile():
            gameloop_ui_path = self.get_local_reg("InstallPath", path="UI").replace("\\", "/")

            tree = ET.parse(nvidia_profile_path, parser=ET.XMLParser(encoding='utf-16'))
            root = tree.getroot()

            profilename = root.find('.//ProfileName')
            executeables = root.find('.//Executeables')
            path_elem = executeables.find('string')

            path_elem.text = f"{gameloop_ui_path}/androidemulatoren.exe".lower()
            profilename.text = path_elem.text.replace('/', '\\')

            gpu = GPUtil.getGPUs()[0] if GPUtil.getGPUs() else None

            filter_setting = tree.find(".//ProfileSetting[SettingNameInfo='Enable FXAA']")
            if gpu and gpu.memoryTotal / 1024 < 3:
                filter_setting.find('SettingValue').text = '0'
            else:
                filter_setting.find('SettingValue').text = '1'

            tree.write(nvidia_profile_path, encoding='utf-16')

        def is_gpu_nvidia() -> bool:
            try:
                gpu_provider = wmi.WMI().Win32_VideoController()[0].AdapterCompatibility
                return "NVIDIA" in gpu_provider
            except:
                return False

        if is_gpu_nvidia():
            change_nvidia_profile()

            args = [
                self.resource_path("assets/nvidiaProfileInspector.exe"),
                nvidia_profile_path,
                "-silent"
            ]
            subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def optimize_gameloop_registry(self):
        install_path = self.get_local_reg("InstallPath", path="UI")
        registry_keys = [
            'AndroidEmulator.exe',
            'AndroidEmulatorEn.exe',
            'AndroidEmulatorEx.exe',
            'aow_exe.exe',
        ]
        base_key = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options'
        value_name = 'CpuPriorityClass'
        value_data = '3'

        for key in registry_keys:
            full_key = fr"{base_key}\{key}\PerfOptions"
            command = [
                'reg', 'ADD', full_key,
                '/v', value_name,
                '/t', 'REG_DWORD',
                '/d', value_data,
                '/f'
            ]
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        registry_entries = [
            (
                r'HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers',
                '~ DISABLEDXMAXIMIZEDWINDOWEDMODE HIGHDPIAWARE'
            ),
            (
                r'HKEY_CURRENT_USER\SOFTWARE\Microsoft\DirectX\UserGpuPreferences',
                'GpuPreference=2;'
            )
        ]

        commands = [
            [
                'reg', 'ADD', registry_key,
                '/v', fr'{install_path}\{key}',
                '/t', 'REG_SZ',
                '/d', value,
                '/f'
            ]
            for registry_key, value in registry_entries
            for key in registry_keys
        ]

        for command in commands:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def temp_cleaner(self):
        """
        Cleans temporary files and directories.

        Returns:
            bool: True if the function successfully cleans the temporary files and directories.
        """
        base_path = getattr(sys, '_MEIPASS', os.path.abspath('.'))
        gameloop_ui_path = self.get_local_reg('InstallPath', path='UI')

        # Clear temporary files
        temp_path = tempfile.gettempdir()
        for folder in os.listdir(temp_path):
            folder_path = os.path.join(temp_path, folder)
            if folder_path == base_path:
                continue
            if os.path.isdir(folder_path):
                shutil.rmtree(folder_path, ignore_errors=True)
            else:
                try:
                    os.remove(folder_path)
                except:
                    pass

        def clear_files(directory):
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception:
                    pass

        # Clear Windows Temp folder
        clear_files(r"C:\Windows\Temp")

        # Clear prefetch files
        clear_files(os.path.expandvars(r'%windir%\Prefetch'))

        # Clear Gameloop ShaderCache files
        clear_files(os.path.join(gameloop_ui_path, 'ShaderCache'))

        return True

    def gameloop_settings(self):
        """
        Generates the game loop settings based on the system's hardware specifications.
        """
        def make_scale(value, low=False):
            for version_key in self.pubg_versions.keys():
                content_scale_key = f"{version_key}_ContentScale"
                render_quality_key = f"{version_key}_RenderQuality"
                fps_level_key = f"{version_key}_FPSLevel"

                reg_content_scale = self.get_reg(content_scale_key)
                if reg_content_scale is not None:
                    self.set_dword(content_scale_key, value)

                reg_fps_level = self.get_reg(fps_level_key)
                if reg_fps_level is not None:
                    self.set_dword(fps_level_key, 0)

                reg_render_quality = self.get_reg(render_quality_key)
                if reg_render_quality is not None:
                    render_value = value
                    if low:
                        # value = 0
                        render_value = 2
                    elif value == 1:
                        render_value = 2
                    self.set_dword(render_quality_key, render_value)

        ram_value = round((int(75) * psutil.virtual_memory().total / (1024 ** 3)) / 100) * 1024
        ram_value = min(ram_value, (8 * 1024))

        cpu_value = round((int(75) * psutil.cpu_count(logical=False)) / 100)
        cpu_value = min(cpu_value, 8)

        dc = EnumDisplayDevices(None, 0, 0)
        settings = EnumDisplaySettings(dc.DeviceName, -1)
        refresh_rate = settings.DisplayFrequency
        self.set_dword("VSyncEnabled", 1 if refresh_rate < 89 else 0)

        gpu = GPUtil.getGPUs()[0] if GPUtil.getGPUs() else None
        if gpu:
            gpu_memory = int(gpu.memoryTotal / 1024)
            self.set_dword("SetGraphicsCard", 1)
            if gpu_memory < 4:
                self.set_dword("VMDPI", 240)
                self.set_dword("FxaaQuality", 0)

                if gpu_memory <= 2:
                    self.set_dword("LocalShaderCacheEnabled", 0)
                    self.set_dword("ShaderCacheEnabled", 0)
                    make_scale(1, low=True)
                else:
                    self.set_dword("LocalShaderCacheEnabled", 1)
                    self.set_dword("ShaderCacheEnabled", 1)
                    make_scale(1)

            elif gpu_memory < 8 and cpu_value <= 4:
                self.set_dword("LocalShaderCacheEnabled", 1)
                self.set_dword("ShaderCacheEnabled", 1)
                self.set_dword("VMDPI", 480)
                self.set_dword("FxaaQuality", 2 if cpu_value == 4 else 1)
                make_scale(1)
            else:
                self.set_dword("LocalShaderCacheEnabled", 1)
                self.set_dword("ShaderCacheEnabled", 1)
                self.set_dword("VMDPI", 480)
                self.set_dword("FxaaQuality", 2)
                make_scale(2)

            self.set_dword("GraphicsCardEnabled", 1)

        else:
            self.set_dword("GraphicsCardEnabled", 0)
            self.set_dword("LocalShaderCacheEnabled", 0)
            self.set_dword("ShaderCacheEnabled", 0)
            self.set_dword("VMDPI", 240)
            self.set_dword("FxaaQuality", 0)
            make_scale(1, low=True)

        self.set_dword("ForceDirectX", 1)
        self.set_dword("RenderOptimizeEnabled", 1)
        self.set_dword("AdbDisable", 0)
        self.set_dword("VMMemorySizeInMB", ram_value)
        self.set_dword("VMCpuCount", cpu_value)

        # print(f"[{self.G}#{self.R_A}] The smart settings have been applied {self.G}successfully{self.R_A}")

    def ipad_layout_settings(self, reset=False):
        """
        Modify the layout of the XML file based on the edited values.

        Parameters:
            reset (bool): If True, the XML file will be reset to its original state by copying the backup file. If False, the layout will be modified based on the edited values.
        """
        appdata_folder = os.getenv('APPDATA')
        androidtbox_folder = os.path.join(appdata_folder, 'AndroidTbox')
        original_file = os.path.join(androidtbox_folder, 'TVM_100.xml')
        backup_file = os.path.join(androidtbox_folder, 'TVM_100.xml.mkbackup')

        def set_keymap_layout():
            """
            Modify the layout of the XML file based on the edited values.
            """
            ipad_keymap_values = {
                "Smart 720P": {
                    "SwimUp": {"Space": ("0.832831", "0.691767")},
                    "SwimmingUp": {"Space": ("0.832831", "0.691767")},
                    "Whistle": {"Space": ("0.907380", "0.651606"), "G": ("0.952560", "0.767068")},
                    "Moto": {"E": ("0.801205", "0.634538"), "Q": ("0.710090", "0.639558")},
                    "Moto2": {"E": ("0.801205", "0.634538"), "Q": ("0.710090", "0.639558")},
                    "SetUp": {"Y": (("0.717620", "0.215863"), ("0.768072", "0.215863")),
                              "T": (("0.707078", "0.114458"), ("0.763554", "0.114458"))}
                },
                "Smart 1080P": {
                    "SwimUp": {"Space": ("0.879518", "0.759036")},
                    "SwimmingUp": {"Space": ("0.879518", "0.759036")},
                    "Whistle": {"Space": ("0.932982", "0.748996"), "G": ("0.963855", "0.828313")},
                    "Moto": {"E": ("0.854669", "0.728916"), "Q": ("0.790663", "0.730924")},
                    "Moto2": {"E": ("0.854669", "0.728916"), "Q": ("0.790663", "0.730924")}
                },
                "Smart 2K": {
                    "SwimUp": {"Space": ("0.879518", "0.759036")},
                    "SwimmingUp": {"Space": ("0.879518", "0.759036")},
                    "Whistle": {"Space": ("0.932982", "0.748996"), "G": ("0.963855", "0.828313")},
                    "Moto": {"E": ("0.854669", "0.728916"), "Q": ("0.790663", "0.730924")},
                    "Moto2": {"E": ("0.854669", "0.728916"), "Q": ("0.790663", "0.730924")}
                }
            }

            # Read the XML content
            with open(original_file, 'r', encoding='utf-8') as xml_file:
                xml_code = xml_file.read()

            # Create an ElementTree from the XML content
            root = ET.fromstring(f'<root>{xml_code}</root>')

            for version in self.pubg_versions:
                edited_combinations = {}
                for item_elem in root.findall(f".//Item[@ApkName='{version}'].//KeyMapMode"):
                    name_attr = item_elem.get("Name")

                    if name_attr in ipad_keymap_values:
                        for key_mapping_elem in item_elem.findall(".//KeyMapping"):
                            item_name = key_mapping_elem.get("ItemName")

                            for switch_operation_elem in key_mapping_elem.findall(".//SwitchOperation"):
                                enable_switch = switch_operation_elem.get("EnableSwitch")

                                if name_attr in ipad_keymap_values and enable_switch in ipad_keymap_values[name_attr]:
                                    if item_name in ipad_keymap_values[name_attr][enable_switch]:
                                        new_x, new_y = ipad_keymap_values[name_attr][enable_switch][item_name]

                                        if (name_attr, item_name, enable_switch) not in edited_combinations:
                                            switch_operation_elem.set("Point_X", new_x)
                                            switch_operation_elem.set("Point_Y", new_y)
                                            edited_combinations[(name_attr, item_name, enable_switch)] = True

                        for key_mapping_elem in item_elem.findall(".//KeyMappingEx"):
                            item_name = key_mapping_elem.get("ItemName")

                            for switch_operation_elem in key_mapping_elem.findall(".//SwitchOperation"):
                                enable_switch = switch_operation_elem.get("EnableSwitch")

                                if name_attr in ipad_keymap_values and enable_switch in ipad_keymap_values[name_attr]:
                                    if item_name in ipad_keymap_values[name_attr][enable_switch]:
                                        new_values = list(ipad_keymap_values[name_attr][enable_switch][item_name])

                                        for (x, y), point_val in zip(new_values, key_mapping_elem.findall(".//Point")):
                                            point_val.set("Point_X", x)
                                            point_val.set("Point_Y", y)

            modified_xml_code = ET.tostring(root, encoding='utf-8').decode('utf-8')
            modified_xml_code = modified_xml_code.replace("<root>", "").replace("</root>", "")

            with open(original_file, 'w', encoding='utf-8') as modified_file:
                modified_file.write(modified_xml_code)

        if reset:
            shutil.copy2(backup_file, original_file)
            os.remove(backup_file)
        else:
            if not os.path.exists(backup_file):
                shutil.copy2(original_file, backup_file)
            set_keymap_layout()

    def ipad_settings(self, width: int, height: int) -> None:
        """
        Update iPad settings with the given width and height.
        """
        _width = self.settings.value("VMResWidth")
        _height = self.settings.value("VMResHeight")

        if _width is None or _height is None:
            vm_res_width = self.get_reg("VMResWidth")
            vm_res_height = self.get_reg("VMResHeight")
            self.settings.setValue("VMResWidth", vm_res_width)
            self.settings.setValue("VMResHeight", vm_res_height)

        self.ipad_layout_settings()
        self.set_dword("VMResWidth", width)
        self.set_dword("VMResHeight", height)

    def reset_ipad(self):
        """
        Resets the resolution of the iPad to its default values.
        """
        width = self.settings.value("VMResWidth")
        height = self.settings.value("VMResHeight")

        if width and height:
            self.settings.setValue("VMResWidth", None)
            self.settings.setValue("VMResHeight", None)
            self.ipad_layout_settings(reset=True)
            self.set_dword("VMResWidth", width)
            self.set_dword("VMResHeight", height)
            return width, height
        else:
            return None, None


class Game(Optimizer):

    def gen_game_icon(self, game_name):
        gameloop_market_path = self.get_local_reg("InstallPath") or r"C:\Program Files\TxGameAssistant\AppMarket"
        pythoncom.CoInitialize()
        desktop = winshell.desktop()

        version_id = next((key for key, value in self.pubg_versions.items() if value == game_name), None)
        path_icon = os.path.join(desktop, f"{game_name}.lnk")
        target = rf"{gameloop_market_path}\AppMarket.exe"

        icon = self.resource_path(fr"assets\icons\{version_id}.ico")
        copy(icon, fr"{gameloop_market_path}\{version_id}.ico")

        shortcut = Dispatch('WScript.Shell').CreateShortCut(path_icon)
        shortcut.Targetpath = target
        shortcut.Arguments = f"-startpkg {version_id}  -from DesktopLink"
        shortcut.Description = "By Mohamed Kamal (MKvip) - Discord: mkvip"
        shortcut.IconLocation = fr"{gameloop_market_path}\{version_id}.ico"
        shortcut.save()

    def check_adb_status(self):
        adb_status = self.get_reg("AdbDisable")

        if adb_status == 0:
            self.adb_enabled = True
            return
        elif adb_status == 1:
            self.set_dword("AdbDisable", 0)
            self.adb_enabled = False
            return

        raise ValueError("Unknown AdbDisable status.")

    @staticmethod
    def is_gameloop_running():
        running_process_list = subprocess.check_output(["tasklist"])
        emulator_processes = [b"AndroidEmulatorEx.exe", b"AndroidEmulatorEn.exe"]
        return any(process in running_process_list for process in emulator_processes)

    def check_adb_connection(self):
        try:
            client = adbutils.AdbClient()
            self.adb = client.device(serial="emulator-5554")
            self.adb.sync.pull("/default.prop", self.resource_path(r'assets\testADB.mkvip'))
            self.adb_work = True
        except Exception:
            self.kill_adb()
            self.adb_work = False

    def pubg_version_found(self):
        """
        Checks if any version of PUBG is installed on the device.
        """
        self.PUBG_Found = [version_name for package_name, version_name in self.pubg_versions.items()
                       if self.adb.shell(f"pm list packages {package_name}")]

    def get_graphics_file(self, package: str):
        active_savegames_path = f"/sdcard/Android/data/{package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/SaveGames/Active.sav"
        local_file_path = self.resource_path('assets/old.mkvip')
        self.pubg_package = package
        self.adb.sync.pull(active_savegames_path, local_file_path)

        with open(local_file_path, 'rb') as file:
            self.active_sav_content = file.read()

    def save_graphics_file(self):
        file_path = self.resource_path("assets/new.mkvip")
        with open(file_path, 'wb') as file:
            file.write(self.active_sav_content)

    def set_fps(self, val: str) -> None:
        """
        Updates the Active.sav file with the new FPS value.
        """
        fps_mapping = {
            "Low": b"\x02",
            "Medium": b"\x03",
            "High": b"\x04",
            "Ultra": b"\x05",
            "Extreme": b"\x06",
            "90 fps": b"\x07",
        }
        fps_value = fps_mapping.get(val)

        fps_properties = ["FPSLevel", "BattleFPS", "LobbyFPS"]
        if fps_value is not None:
            for prop in fps_properties:
                header = prop.encode(
                    'utf-8') + b'\x00\x0c\x00\x00\x00IntProperty\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'
                before, _, after = self.active_sav_content.partition(header)
                after = after[:1].replace(after[:1], fps_value) + after[1:]
                self.active_sav_content = before + _ + after

    def read_hex(self, name):
        """
        Reads the value of the specified property from the Active.sav file.
        """
        header = name.encode('utf-8') + b'\x00\x0c\x00\x00\x00IntProperty\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'
        _, _, content = self.active_sav_content.partition(header)
        return content[:1]

    def change_graphics_file(self, name, val):
        """
        Updates the Active.sav file with the new graphics setting value.
        """
        header = name.encode('utf-8') + b'\x00\x0c\x00\x00\x00IntProperty\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00'
        a, b, c = self.active_sav_content.partition(header)
        c = val + c[1:]
        self.active_sav_content = a + b + c

    def get_graphics_setting(self):
        """
        Gets the graphics setting name from the hex value.
        """
        graphics_setting_hex = self.read_hex("BattleRenderQuality")
        graphics_setting_dict = {
            b'\x01': "Smooth",
            b'\x02': "Balanced",
            b'\x03': "HD",
            b'\x04': "HDR",
            b'\x05': "Ultra HD"
        }
        return graphics_setting_dict.get(graphics_setting_hex, None)

    def get_fps(self):
        """
        Gets the FPS value from the Active.sav file.
        """
        fps_hex = self.read_hex("BattleFPS")
        fps_dict = {
            b"\x02": "Low",
            b"\x03": "Medium",
            b"\x04": "High",
            b"\x05": "Ultra",
            b"\x06": "Extreme",
            b"\x07": "90 fps",
        }
        return fps_dict.get(fps_hex, None)

    def get_shadow(self):
        """
        Gets the shadow value from the UserCustom.ini file.
        """
        shadow_name = None
        user_custom_ini_path = f"/sdcard/Android/data/{self.pubg_package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserCustom.ini"
        self.adb.sync.pull(user_custom_ini_path, self.resource_path(r'assets\user.mkvip'))

        with open(self.resource_path(r"assets\user.mkvip")) as file:
            for line in file:
                line = line.strip()
                if line.startswith("+CVars=0B572A11181D160E280C1815100D0044"):
                    if int(line[-2:]) == 49:
                        shadow_name = "Disable"
                    elif int(line[-2:]) == 48:
                        shadow_name = "Enable"
                    break

        return shadow_name

    # TODO : Add this function
    def set_shadow(self, value):
        """
        Sets the shadow value in the Active.sav file.
        :param value: Shadow value to set ("ON" or "OFF")
        :return: True if successful, False otherwise
        """
        shadow_value = {"ON": 48, "OFF": 49}.get(value)
        if shadow_value is None:
            return False

        lines = []
        with open(self.resource_path(r"assets\user.mkvip"), "r") as file:
            for line in file:
                if line.strip().startswith("+CVars=0B572A11181D160E280C1815100D0044"):
                    line = f"+CVars=0B572A11181D160E280C1815100D0044{shadow_value}\n"
                elif line.strip().startswith("+CVars=0B572C0A1C0B2A11181D160E2A0E100D1A1144"):
                    line = f"+CVars=0B572C0A1C0B2A11181D160E2A0E100D1A1144{shadow_value}\n"
                lines.append(line)

        with open(self.resource_path(r"assets\user.mkvip"), "w") as file:
            file.writelines(lines)

        return True

    def get_graphics_style(self):
        """
        Gets the graphics style name from the hex value.
        :return: name of the graphics style
        """
        battle_style_hex = self.read_hex("BattleRenderStyle")
        battle_style_dict = {
            b'\x01': "Classic",
            b'\x02': "Colorful",
            b'\x03': "Realistic",
            b'\x04': "Soft",
            b'\x06': "Movie"
        }

        return battle_style_dict.get(battle_style_hex, "Not Found, It Will Be Added In The Next Update")

    def set_graphics_style(self, style):
        """
        Sets the graphics style.
        """
        battle_style_dict = {
            "Classic": b'\x01',
            "Colorful": b'\x02',
            "Realistic": b'\x03',
            "Soft": b'\x04',
            "Movie": b'\x06'
        }
        battle_style = battle_style_dict.get(style, "Not Found, It Will Be Added In The Next Update")
        self.change_graphics_file("BattleRenderStyle", battle_style)

    def set_graphics_quality(self, quality):
        """
        Sets the graphics quality for different game modes.
        """
        graphics_setting_dict = {
            "Smooth": b'\x01',
            "Balanced": b'\x02',
            "HD": b'\x03',
            "HDR": b'\x04',
            "Ultra HD": b'\x05'
        }

        graphics_setting = graphics_setting_dict.get(quality, b'\x00')

        # Set the graphics quality
        graphics_files = ["ArtQuality", "LobbyRenderQuality", "BattleRenderQuality"]
        for value in graphics_files:
            self.change_graphics_file(value, graphics_setting)

    def push_active_shadow_file(self):
        """
        Pushes the modified Active.sav & Shadow file to the device and restarts the game.
        """
        self.adb.shell(f"am force-stop {self.pubg_package}")
        sleep(0.2)

        files = [
            (self.resource_path(r"assets\new.mkvip"),
             "/sdcard/Android/data/{self.pubg_package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/SaveGames/Active.sav"),
            (self.resource_path(r"assets\user.mkvip"),
             "/sdcard/Android/data/{self.pubg_package}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserCustom.ini")
        ]

        for src, dest in files:
            self.adb.sync.push(src, dest)
            sleep(0.2)

    def start_app(self):
        package = f"{self.pubg_package}/com.epicgames.ue4.SplashActivity"
        self.adb.shell(f"am start -n {package}")

    def kr_fullhd(self):
        def backup_folder(path):
            backup_path = path + '.MKbackup'

            output = self.adb.shell(f"[ -d {path} ] && echo 1 || echo 0").strip()
            backup_output = self.adb.shell(f"[ -d {backup_path} ] && echo 1 || echo 0").strip()
            if backup_output == '0' and output == '1':
                self.adb.shell(['mv', path, backup_path])
            elif backup_output == '1' and output == '1':
                self.adb.shell(['rm', '-r', path])

        def restore_folder(path):
            backup_path = path + '.MKbackup'
            backup_output = self.adb.shell(f"[ -d {backup_path} ] && echo 1 || echo 0").strip()
            if backup_output == '1':
                self.adb.shell(['mv', backup_path, path])

        data_path = f"/sdcard/Android/data/{self.pubg_package}"
        obb_path = f"/sdcard/Android/obb/{self.pubg_package}"
        user_custom_ini_path = f"{data_path}/files/UE4Game/ShadowTrackerExtra/ShadowTrackerExtra/Saved/Config/Android/UserCustom.ini"

        self.adb.push(self.resource_path('assets\mk_kr.ini'), user_custom_ini_path)

        safe_path = "/sdcard/mk_safe_folder"
        self.adb.shell(f"mkdir -p {safe_path}")
        self.adb.shell(f"cp -r {data_path}/shared_prefs {safe_path}/shared_prefs")
        self.adb.shell(f"cp -r {data_path}/databases {safe_path}/databases")

        backup_folder(data_path)
        backup_folder(obb_path)

        self.adb.shell(['pm', 'clear', self.pubg_package])
        self.adb.shell(['pm', 'grant', self.pubg_package, 'android.permission.READ_EXTERNAL_STORAGE'])
        self.adb.shell(['pm', 'grant', self.pubg_package, 'android.permission.WRITE_EXTERNAL_STORAGE'])

        restore_folder(data_path)
        restore_folder(obb_path)

        self.adb.shell(f"cp -r {safe_path}/shared_prefs {data_path}/shared_prefs")
        self.adb.shell(f"cp -r {safe_path}/databases {data_path}/databases")

        self.start_app()

        self.adb.shell(f"rm -r {safe_path}")