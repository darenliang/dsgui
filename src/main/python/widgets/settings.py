import subprocess

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.settings import Ui_settings
from utils import config, message


class Settings(QWidget):
    def __init__(self):
        QWidget.__init__(self)  # noqa

        self.ui = Ui_settings()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":icons/icon.png"))

        self.ui.ok.clicked.connect(self.submit)

    def submit(self):
        token = self.ui.userTokenLineEdit.text().strip()
        server_id = self.ui.serverIDLineEdit.text().strip()
        channel_checkbox = self.ui.checkBox.isChecked()

        if token == "" or server_id == "":
            message.create(
                QMessageBox.Warning,
                "Warning",
                "Token or Server ID is empty.",
            ).exec()
            return

        opts = [config.dscli_bin, "config", "-t", token, "-i", server_id]

        if channel_checkbox:
            opts.append("-d")

        result = subprocess.run(
            opts,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            shell=True
        )

        if result.returncode == 0:
            message.create(
                QMessageBox.Information,
                "Success",
                "Settings saved successfully."
            ).exec()
            self.close()
            return
        else:
            message.create(
                QMessageBox.Warning,
                "Error",
                "Settings saved unsuccessfully."
            ).exec()
            return
