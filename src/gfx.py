from PyQt5.QtCore import QThread, pyqtSignal, QObject


class SubmitWorkerThread(QThread):
    task_completed = pyqtSignal()

    def __init__(self, window, ui, gfx):
        super(SubmitWorkerThread, self).__init__()
        self.app = window
        self.ui = ui
        self.gfx = gfx

    def run(self):
        self.app.show_status_message("Working on Graphics Settings ...")

        checked_graphics_button = next((button for button in self.gfx.graphics_buttons if button.isChecked()), None)
        if checked_graphics_button:
            self.app.set_graphics_quality(checked_graphics_button.text())

        checked_fps_button = next((button for button in self.gfx.fps_buttons if button.isChecked()), None)
        if checked_fps_button:
            self.app.set_fps(checked_fps_button.text())

        checked_style_button = next((button for button in self.gfx.style_buttons if button.isChecked()), None)
        if checked_style_button:
            self.app.set_graphics_style(checked_style_button.property("styleId"))

        self.app.save_graphics_file()
        self.app.push_active_shadow_file()

        if self.app.pubg_package == "com.pubg.krmobile" and self.ui.resolution_btn.isChecked():
            self.app.kr_fullhd()
        else:
            self.app.start_app()

        self.task_completed.emit()


class ConnectWorkerThread(QThread):
    task_completed = pyqtSignal()

    def __init__(self, window, ui):

        super(ConnectWorkerThread, self).__init__()
        self.app = window
        self.ui = ui

    def get_active_file(self, pubg_version):
        """ Get the active file for the given PUBG version """

        pubg_package = next(key for key, value in self.app.pubg_versions.items() if value == pubg_version)
        self.app.get_graphics_file(pubg_package)

    def show_connection_error(self, message):
        self.ui.connect_gameloop_btn.setChecked(False)
        self.ui.connect_gameloop_btn.setText("Connect to Gameloop")
        self.app.show_status_message(message)
        self.task_completed.emit()

    def run(self):
        self.ui.connect_gameloop_btn.setText("Connecting...")
        self.ui.connect_gameloop_btn.setEnabled(False)
        self.app.show_status_message("Connecting to Gameloop...", 3)
        self.app.check_adb_status()

        if not self.app.adb_enabled:
            message = "Restart GameLoop and Try Again." if self.app.is_gameloop_running() else "GameLoop not working."
            self.show_connection_error(message)
            return

        if not self.app.is_gameloop_running():
            self.show_connection_error("GameLoop not working.")
            return

        self.app.check_adb_connection()

        if not self.app.is_adb_working:
            message = "Restart GameLoop and Try Again." if self.app.is_gameloop_running() else "Gameloop not working."
            self.show_connection_error(message)
            return

        self.app.pubg_version_found()
        num_found = len(self.app.PUBG_Found)

        if num_found == 0:
            self.app.show_status_message("You don't have any PUBG Mobile version installed")
            self.task_completed.emit()
            return
        elif num_found > 1:
            self.ui.pubgchoose_dropdown.clear()
            self.ui.pubgchoose_dropdown.addItems(self.app.PUBG_Found)
            self.ui.pubgchoose_dropdown.setCurrentText(self.app.PUBG_Found[0])
            self.ui.PubgchooseFrame.setVisible(True)
            self.app.show_status_message("Select version to use")
            self.task_completed.emit()
            return

        self.app.show_status_message(f"Using version {self.app.PUBG_Found[0]}", 3)
        self.get_active_file(self.app.PUBG_Found[0])
        self.ui.connect_gameloop_btn.setText("Connected")
        self.task_completed.emit()


class GFX(QObject):

    def __init__(self, window):
        super(GFX, self).__init__()

        from .ui import Ui_MainWindow
        from .ui_functions import Window
        self.ui: Ui_MainWindow = window.ui
        self.app: Window = window

        self.call_app()

    def call_app(self):
        # Hide Labels and Buttons in UI
        self.ui.ResolutionkrFrame.hide()
        self.ui.PubgchooseFrame.hide()

        self.graphics_buttons_func()
        self.fps_buttons_func()
        self.style_buttons_func()

        self.gfx_buttons(enabled=False)

        # Button connections
        self.ui.connect_gameloop_btn.clicked.connect(self.connect_gameloop_button_click)
        self.ui.submit_gfx_btn.clicked.connect(self.gfx_submit_button_click)

    def gfx_submit_button_click(self):

        self.ui.submit_gfx_btn.setEnabled(False)
        self.worker_submit = SubmitWorkerThread(self.app, self.ui, self)
        self.worker_submit.task_completed.connect(self.submit_gfx_done)
        self.worker_submit.start()

    def submit_gfx_done(self):
        self.ui.submit_gfx_btn.setEnabled(True)
        if self.app.pubg_package == "com.pubg.krmobile" and self.ui.resolution_btn.isChecked():
            status_message = "Graphics settings applied, resolution set to 1080p."
        else:
            status_message = "Graphics settings applied successfully."
        self.app.show_status_message(status_message)

    def connect_gameloop_button_click(self, checked: bool):
        if checked:
            self.ui.connect_gameloop_btn.setEnabled(False)
            self.worker = ConnectWorkerThread(self.app, self.ui)
            self.worker.task_completed.connect(self.connect_gameloop_task_completed)
            self.worker.start()
        else:
            self.gfx_buttons(enabled=checked)
            self.ui.disable_shadow_btn.setChecked(False)
            self.ui.enable_shadow_btn.setChecked(False)
            self.ui.ResolutionkrFrame.hide()
            self.ui.PubgchooseFrame.hide()
            self.app.kill_adb()
            self.ui.connect_gameloop_btn.setText("Connect to GameLoop")
            self.app.show_status_message("Disconnected from GameLoop", 3)

    def use_pubg_version(self):
        val = self.ui.pubgchoose_dropdown.currentText()
        pubg_package = next(k for k, v in self.app.pubg_versions.items() if v == val)
        self.app.get_graphics_file(pubg_package)
        self.ui.connect_gameloop_btn.setText("Connected")
        self.app.show_status_message(f"Using version {val}", 3)
        self.ui.PubgchooseFrame.hide()
        self.connect_gameloop_task_completed(checked=False)

    def connect_gameloop_task_completed(self, checked: bool = True):
        if not self.app.is_adb_working:
            self.ui.connect_gameloop_btn.setEnabled(True)
            return
        if checked:
            if len(self.app.PUBG_Found) > 1:
                self.ui.pubgchoose_btn.clicked.connect(self.use_pubg_version)
                return
        self.ui.connect_gameloop_btn.setEnabled(True)

        self.graphics_buttons = [
            self.ui.smooth_graphics_btn,
            self.ui.balanced_graphics_btn,
            self.ui.hd_graphics_btn,
            self.ui.hdr_graphics_btn,
            self.ui.ultrahd_graphics_btn,
        ]
        self.graphics_value = self.app.get_graphics_setting()

        for button in self.graphics_buttons:
            if button.text() == self.graphics_value:
                button.setChecked(True)
                break

        self.fps_buttons = [
            self.ui.low_fps_btn,
            self.ui.medium_fps_btn,
            self.ui.high_fps_btn,
            self.ui.ultra_fps_btn,
            self.ui.extreme_fps_btn,
            self.ui.fps90_fps_btn,
            self.ui.fps120_fps_btn
        ]
        self.fps_value = self.app.get_fps()

        for button in self.fps_buttons:
            if button.text() == self.fps_value:
                button.setChecked(True)
                break

        self.style_buttons = [
            self.ui.classic_style_btn,
            self.ui.colorful_style_btn,
            self.ui.realistic_style_btn,
            self.ui.soft_style_btn,
            self.ui.movie_style_btn
        ]
        battle_style_dict = {
            b'\x01': "Classic",
            b'\x02': "Colorful",
            b'\x03': "Realistic",
            b'\x04': "Soft",
            b'\x06': "Movie"
        }

        for button, style_id in zip(self.style_buttons, battle_style_dict.values()):
            button.setProperty("styleId", style_id)

        self.style_value = self.app.get_graphics_style()

        for button in self.style_buttons:
            if self.style_value.lower() in button.objectName():
                button.setChecked(True)
                break

        self.shadow_buttons = [
            self.ui.disable_shadow_btn,
            self.ui.enable_shadow_btn
        ]
        self.shadow_value = self.app.get_shadow()

        for button in self.shadow_buttons:
            if button.text() == self.shadow_value:
                button.setChecked(True)
                break

        if self.app.pubg_package == "com.pubg.krmobile":
            self.ui.ResolutionkrFrame.setVisible(True)
            self.ui.resolution_btn.setChecked(True)

        self.gfx_buttons(enabled=True)

    def graphics_buttons_func(self):
        buttons = [
            self.ui.smooth_graphics_btn,
            self.ui.balanced_graphics_btn,
            self.ui.hd_graphics_btn,
            self.ui.hdr_graphics_btn,
            self.ui.ultrahd_graphics_btn
        ]
        for button in buttons:
            button.clicked.connect(lambda checked, btn=button: self.check_button_selected(buttons, btn))

    def fps_buttons_func(self):
        buttons = [
            self.ui.low_fps_btn,
            self.ui.medium_fps_btn,
            self.ui.high_fps_btn,
            self.ui.ultra_fps_btn,
            self.ui.extreme_fps_btn,
            self.ui.fps90_fps_btn,
            self.ui.fps120_fps_btn
        ]
        for button in buttons:
            button.clicked.connect(lambda checked, btn=button: self.check_button_selected(buttons, btn))

    def style_buttons_func(self):
        buttons = [
            self.ui.classic_style_btn,
            self.ui.colorful_style_btn,
            self.ui.realistic_style_btn,
            self.ui.soft_style_btn,
            self.ui.movie_style_btn
        ]
        for button in buttons:
            button.clicked.connect(lambda checked, btn=button: self.check_button_selected(buttons, btn))

    @staticmethod
    def check_button_selected(buttons, clicked_button):
        for button in buttons:
            button.setChecked(button is clicked_button)

    def gfx_buttons(self, enabled: bool):
        buttons = [
            self.ui.smooth_graphics_btn,
            self.ui.balanced_graphics_btn,
            self.ui.hd_graphics_btn,
            self.ui.hdr_graphics_btn,
            self.ui.ultrahd_graphics_btn,
            self.ui.low_fps_btn,
            self.ui.medium_fps_btn,
            self.ui.high_fps_btn,
            self.ui.ultra_fps_btn,
            self.ui.extreme_fps_btn,
            self.ui.fps90_fps_btn,
            self.ui.fps120_fps_btn,
            self.ui.classic_style_btn,
            self.ui.colorful_style_btn,
            self.ui.realistic_style_btn,
            self.ui.soft_style_btn,
            self.ui.movie_style_btn,
            # self.ui.disable_shadow_btn,
            # self.ui.enable_shadow_btn,
            self.ui.submit_gfx_btn
        ]

        for button in buttons:
            button.setEnabled(enabled)
            if not enabled:
                button.setChecked(enabled)
