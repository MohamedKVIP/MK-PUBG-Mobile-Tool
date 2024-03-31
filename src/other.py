import ping3
from PyQt5.QtCore import QThread, pyqtSignal, QObject
import re
from . import setup_logger


class IPADWorkerThread(QThread):
    task_completed = pyqtSignal()

    def __init__(self, window, ui, gfx):
        super(IPADWorkerThread, self).__init__()
        self.app = window
        self.ui = ui
        self.gfx = gfx

    def run(self):
        width, height = self.extract_dimensions(self.ui.ipad_dropdown.currentText())
        self.app.ipad_settings(width, height)
        self.task_completed.emit()

    @staticmethod
    def extract_dimensions(string):
        pattern = r'(\d+)\s*x\s*(\d+)'
        match = re.search(pattern, string)

        if match:
            width = int(match.group(1))
            height = int(match.group(2))
            return width, height
        else:
            return None


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
        self.logger = setup_logger('error_logger', 'error.log')

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
        try:
            self.app.temp_cleaner()
            self.app.show_status_message("System performance improved.")
        except Exception as e:
            self.logger.error(f"Exception occurred: {str(e)}", exc_info=True)
            self.app.show_status_message(f"There was an Error saved in error.log")

    def gameloop_smart_settings_button_click(self, e):
        """ Gameloop Smart Settings Button On Click Function """
        try:
            self.app.gameloop_settings()
            self.app.show_status_message("Smart settings applied successfully.")
        except Exception as e:
            self.logger.error(f"Exception occurred: {str(e)}", exc_info=True)
            self.app.show_status_message(f"There was an Error saved in error.log")
    def gameloop_optimizer_button_click(self, e):
        """ Gameloop Optimizer Button On Click Function """
        try:
            self.app.add_to_windows_defender_exclusion()
            self.app.optimize_gameloop_registry()
            self.app.optimize_for_nvidia()
            self.app.show_status_message("Gameloop optimizer applied successfully.")
        except Exception as e:
            self.logger.error(f"Exception occurred: {str(e)}", exc_info=True)
            self.app.show_status_message(f"There was an Error saved in error.log")
    def all_recommended_button_click(self, e):
        """ All Recommended Button On Click Function """
        try:
            self.app.gameloop_settings()
            self.app.add_to_windows_defender_exclusion()
            self.app.optimize_gameloop_registry()
            self.app.optimize_for_nvidia()
            self.app.temp_cleaner()
            self.app.show_status_message("All recommended settings applied successfully.")
        except Exception as e:
            self.logger.error(f"Exception occurred: {str(e)}", exc_info=True)
            self.app.show_status_message(f"There was an Error saved in error.log")

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
        try:
            if self.app.is_gameloop_running():
                self.app.show_status_message(f"Close Gameloop to use this button. (Force Close Gameloop)", 5)
                return
            self.app.show_status_message("please wait, Working on it...", 15)
            self.ui.ipad_other_btn.setEnabled(False)
            self.ui.ipad_rest_btn.setEnabled(False)
            self.worker_ipad_submit = IPADWorkerThread(self.app, self.ui, self)
            self.worker_ipad_submit.task_completed.connect(self.submit_ipad_done)
            self.worker_ipad_submit.start()
        except ValueError:
            self.app.show_status_message("Invalid width or height values", 5)

    def submit_ipad_done(self):
        self.ui.ipad_other_btn.setEnabled(True)
        self.ui.ipad_rest_btn.setEnabled(True)
        self.ui.ipad_rest_btn.show()
        gameloop_status = "Restart" if self.app.is_gameloop_running() else "Start"
        self.app.show_status_message(f"{gameloop_status} Gameloop and enjoy with IPAD settings.", 7)

    def ipad_reset_button_click(self, e):
        if self.app.is_gameloop_running():
            self.app.show_status_message(
                "Close Gameloop to use this button. (Force Close Gameloop)", 5
            )
            return

        width, height = self.app.reset_ipad()
        self.ui.ipad_rest_btn.hide()

        # gameloop_status = "Restart" if self.app.is_gameloop_running() else "Start"
        message = f"Start Gameloop to Utilize Resolution ({width} x {height})."
        self.app.show_status_message(message, 7)