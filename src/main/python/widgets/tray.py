import sys

from widgets.main import *
from widgets.settings import *


class SystemTray(QSystemTrayIcon):
    def __init__(self, app):
        QSystemTrayIcon.__init__(self)

        #
        # Save opening state to prevent windows from being GC'd
        #
        self.main_window = MainWindow(app)
        self.settings_dialog = None

        #
        # Tray
        #
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(":icons/icon.png"))
        self.tray.setVisible(True)

        #
        # Menu items
        #
        self.menu = QMenu()

        file_explorer_option = QAction("File Explorer")
        file_explorer_option.triggered.connect(self.open_main_window)
        self.menu.addAction(file_explorer_option)

        settings_option = QAction("Settings")
        settings_option.triggered.connect(self.open_settings)
        self.menu.addAction(settings_option)

        self.menu.addSeparator()

        quit_option = QAction("Quit")
        quit_option.triggered.connect(app.quit)
        self.menu.addAction(quit_option)

        #
        # Add menu
        #
        self.tray.setContextMenu(self.menu)
        self.tray.setToolTip("dscli: Store files on Discord without limits")

        #
        # Add tray click action
        #
        self.tray.activated.connect(self.open_system_tray)

        exit_code = app.exec()
        sys.exit(exit_code)

    def open_main_window(self):
        if not self.main_window.isHidden():
            self.main_window.activateWindow()
            self.main_window.refresh_list()
            return

        if self.settings_dialog is not None:
            self.settings_dialog.close()

        self.main_window.show()
        self.main_window.refresh_list()

    def open_settings(self):
        if self.main_window is not None:
            self.main_window.hide()

        self.settings_dialog = Settings()
        self.settings_dialog.show()

    def open_system_tray(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.open_main_window()
