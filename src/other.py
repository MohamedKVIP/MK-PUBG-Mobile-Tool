import ping3
import requests
from PyQt5.QtCore import QObject


class Other(QObject):
    def __init__(self, window):
        super(Other, self).__init__()
        from .ui import Ui_MainWindow
        from .ui_functions import Window
        self.ui: Ui_MainWindow = window.ui
        self.app: Window = window
        self.dns_servers = {
            "Google DNS - 8.8.8.8": ['8.8.8.8', '8.8.4.4'],
            "Cloudflare DNS - 1.1.1.1": ['1.1.1.1', '1.0.0.1'],
            "Quad9 DNS - 9.9.9.9": ['9.9.9.9', '149.112.112.112'],
            "Cisco Umbrella - 208.67.222.222": ['208.67.222.222', '208.67.220.220'],
            "Yandex DNS - 77.88.8.1": ['77.88.8.1', '77.88.8.8']
        }
        self.function()

    def function(self):
        ui = self.ui

        ui.tempcleaner_other_btn.clicked.connect(self.temp_cleaner_button_click)
        ui.glsmartsettings_other_btn.clicked.connect(self.gameloop_smart_settings_button_click)
        ui.gloptimizer_other_btn.clicked.connect(self.gameloop_optimizer_button_click)
        ui.all_other_btn.clicked.connect(self.all_recommended_button_click)
        ui.forceclosegl_other_btn.clicked.connect(self.kill_gameloop_processes_button_click)
        ui.shortcut_other_btn.clicked.connect(self.shortcut_submit_button_click)
        ui.dns_dropdown.currentTextChanged.connect(self.dns_dropdown)
        ui.dns_other_btn.clicked.connect(self.dns_submit_button_click)
        ui.ipad_other_btn.clicked.connect(self.ipad_submit_button_click)
        ui.ipad_rest_btn.clicked.connect(self.ipad_reset_button_click)

        ui.ipad_code.hide()
        ui.ipad_code_label.hide()

        _width = self.app.settings.value("VMResWidth")
        _height = self.app.settings.value("VMResHeight")

        if _width is None or _height is None:
            ui.ipad_rest_btn.hide()

    def temp_cleaner_button_click(self, e):
        """ Temp Cleaner Button On Click Function """
        self.app.temp_cleaner()
        self.app.show_status_message("System performance improved!")

    def gameloop_smart_settings_button_click(self, e):
        """ Gameloop Smart Settings Button On Click Function """
        self.app.gameloop_settings()
        self.app.show_status_message("Smart settings applied successfully.")

    def gameloop_optimizer_button_click(self, e):
        """ Gameloop Optimizer Button On Click Function """
        self.app.add_to_windows_defender_exclusion()
        self.app.optimize_gameloop_registry()
        self.app.optimize_for_nvidia()
        self.app.show_status_message("Gameloop optimizer applied successfully.")

    def all_recommended_button_click(self, e):
        """ All Recommended Button On Click Function """
        self.app.temp_cleaner()
        self.app.gameloop_settings()
        self.app.add_to_windows_defender_exclusion()
        self.app.optimize_gameloop_registry()
        self.app.optimize_for_nvidia()
        self.app.show_status_message("All recommended settings applied successfully.")

    def kill_gameloop_processes_button_click(self, e):
        """Terminates Gameloop processes when the button is clicked."""
        if self.app.kill_gameloop():
            message = "All Gameloop processes terminated."
        else:
            message = "No processes found to terminate."
        self.app.show_status_message(message)

    def shortcut_submit_button_click(self, e):
        """ Shortcut Submit Button On Click Function """
        version_value = self.ui.shortcut_dropdown.currentText()
        self.app.gen_game_icon(version_value)
        self.app.show_status_message("Shortcut Generated Successfully")

    def dns_submit_button_click(self, e):
        """ DNS Submit Button On Click Function """

        dns_key = self.ui.dns_dropdown.currentText()
        dns_server = self.dns_servers.get(dns_key)

        if self.app.change_dns_servers(dns_server):
            self.dns_dropdown(dns_key)
            self.app.show_status_message("DNS server changed successfully")
        else:
            self.app.show_status_message("Could not change DNS server")

    def dns_dropdown(self, value):
        server, _ = self.dns_servers[value]
        pings = [ping3.ping(server, timeout=1, unit='ms', size=56) or float('inf') for _ in range(5)]
        lowest_ping = min(pings)
        if lowest_ping != float('inf'):
            ping_result = f"{str(value).split(' -')[0]} Ping: {int(lowest_ping)}ms"
        else:
            ping_result = "No response from DNS servers"
        self.ui.dns_status_label.setText(ping_result)

    def ipad_submit_button_click(self, e):
        def get_ipad_layout_code():
            url = "https://raw.githubusercontent.com/MohamedKVIP/MK-PUBG-Mobile-Tool/main/ipad_layout.json"
            try:
                response = requests.get(url).json()
                code = response.get("code")
                last_update = response.get("last_update")
                if code:
                    self.ui.ipad_code.setText(code)
                    self.ui.ipad_code_label.setText(f"last update: {last_update}")
                    return True
            except:
                return False

        if get_ipad_layout_code():
            width, height = self.ui.ipad_dropdown.currentText().split(" x ", 1)
            try:
                width = int(width)
                height = int(height)
                if self.app.is_gameloop_running():
                    self.app.show_status_message(f"Close Gameloop to use this button. (Force Close Gameloop)", 5)
                    return
                self.ui.ipad_code.show()
                self.ui.ipad_code_label.show()
                self.ui.ipad_rest_btn.show()
                self.app.ipad_settings(width, height)
                gameloop_status = "Restart" if self.app.is_gameloop_running() else "Start"
                self.app.show_status_message(f"{gameloop_status} Gameloop and Copy layout code and use it in game.", 7)
            except ValueError:
                self.app.show_status_message("Invalid width or height values", 5)
        else:
            self.app.show_status_message("Could not get layout code")

    def ipad_reset_button_click(self, e):
        if self.app.is_gameloop_running():
            self.app.show_status_message(
                "Close Gameloop to use this button. (Force Close Gameloop)", 5
            )
            return

        width, height = self.app.reset_ipad()
        self.ui.ipad_rest_btn.hide()

        gameloop_status = "Restart" if self.app.is_gameloop_running() else "Start"
        message = f"{gameloop_status} Gameloop to Utilize Resolution ({width} x {height})."
        self.app.show_status_message(message, 7)