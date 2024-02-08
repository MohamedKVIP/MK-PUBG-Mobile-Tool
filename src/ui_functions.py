from PyQt5 import QtCore, QtWidgets
from .app_functions import Game
from .gfx import GFX
from .other import Other
from .ui import Ui_MainWindow


class Window(QtWidgets.QMainWindow, Game):
    def __init__(self, app_name, app_version):
        # Remove the default title bar
        super(Window, self).__init__()
        self.app_name = app_name
        self.app_version = app_version

        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.appname_label.setText(f"{app_name} {app_version}")
        self.timer = None

        # Set up the GFX and Other objects
        self.GFX = GFX(self)
        self.Other = Other(self)

        # Initialize variables for dragging
        self.draggable = True
        self.drag_start_position = None

        # Connect the button signals
        self.ui.gfx_button.clicked.connect(lambda: self.buttonClicked(self.ui.gfx_button, self.ui.gfx_page))
        self.ui.other_button.clicked.connect(lambda: self.buttonClicked(self.ui.other_button, self.ui.other_page))
        self.ui.about_button.clicked.connect(lambda: self.buttonClicked(self.ui.about_button, self.ui.about_page, ))
        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.minimize_btn.clicked.connect(lambda: self.setWindowState(QtCore.Qt.WindowMinimized))

    def buttonClicked(self, button, page):
        self.ui.gfx_button.setChecked(button == self.ui.gfx_button)
        self.ui.other_button.setChecked(button == self.ui.other_button)
        self.ui.about_button.setChecked(button == self.ui.about_button)

        self.ui.stackedWidget.setCurrentWidget(page)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.draggable:
            self.drag_start_position = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.draggable and self.drag_start_position is not None:
            if event.buttons() & QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.drag_start_position)
                self.drag_start_position = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = None

    def show_status_message(self, message, duration=5):
        if self.timer and self.timer.isActive():
            self.timer.stop()
        self.ui.appstatus_text_lable.setText(message)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.ui.appstatus_text_lable.setText(""))
        self.timer.start(duration * 1000)