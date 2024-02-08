import ctypes
import sys
from datetime import datetime
from pathlib import Path
from src.ui_functions import Window, QtWidgets
from src.update import UpdateWindow

APP_NAME = "MK PUBG Mobile Tool"
APP_VERSION = "v1.0.6"
FULL_APP_NAME = f"{APP_NAME} {APP_VERSION}"
ctypes.windll.kernel32.SetConsoleTitleW(FULL_APP_NAME)


def run_application():
    """
    Run the main GUI application.
    """
    ui = Window(APP_NAME, APP_VERSION)
    ui.show()
    app.exec_()


if __name__ == "__main__":
    print("[#] Starting the GUI app")

    try:
        app = QtWidgets.QApplication(sys.argv)
        update = UpdateWindow()
        update.check_for_updates(APP_VERSION)

        if update.is_update_needed():
            update.show()
            if app.exec_() == 0:
                run_application()
        else:
            run_application()
    except Exception as e:
        with open(f"{Path.cwd()}/error.log", "a") as f:
            f.write(f"-------------------{datetime.now()}-------------------\n")
            f.write(f"CRASH_ERR: {e}\n")
