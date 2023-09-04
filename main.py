import ctypes
import sys
import time
from datetime import datetime
from pathlib import Path

import psutil
import win32gui
import win32process

from src.ui_functions import Window, QtWidgets
from src.update import UpdateWindow

APP_NAME = "MK PUBG Mobile Tool"
APP_VERSION = "v1.0.4"
FULL_APP_NAME = f"{APP_NAME} {APP_VERSION}"
ctypes.windll.kernel32.SetConsoleTitleW(FULL_APP_NAME)


def hide_command_prompt():
    """
    Hide the command prompt window when launching the GUI app.
    """
    _apps = [
        "python",
        "pythonw",
        "cmd",
        "powershell",
        "terminal"
    ]
    first_iteration = True
    try_num = 0
    while True:
        active_window = win32gui.GetForegroundWindow()
        window_title = str(win32gui.GetWindowText(active_window)).lower()
        thread_id, current_pid = win32process.GetWindowThreadProcessId(active_window)
        current_target_name = psutil.Process(current_pid).name().lower()

        full_app_name_lower = FULL_APP_NAME.lower()
        window_title_lower = window_title.lower()

        if (any(forbidden_app in current_target_name for forbidden_app in _apps) and
            full_app_name_lower in window_title_lower) or (
            full_app_name_lower in window_title_lower and "explorer" not in current_target_name):
            ctypes.windll.user32.ShowWindow(active_window, 0)
            break

        if first_iteration:
            print("[!] Click on the command prompt window to hide it and start the GUI app")
            first_iteration = False
        try_num += 1
        time.sleep(0.5)
        if try_num > 30:
            print(f"Please send me the following message: \n"
                  f"window_title: {window_title}\n"
                  f"current_target_name: {current_target_name}")
            break


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
        # hide_command_prompt()  # Disable this if you want to see the command prompt or the app doesn't work

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
        with open(f"{Path.cwd()}/errors.log", "a") as f:
            f.write(f"-------------------{datetime.now()}-------------------\n")
            f.write(f"CRASH_ERR: {e}\n")
