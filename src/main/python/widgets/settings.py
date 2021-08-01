from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.settings import Ui_settings
from utils import config, message, process


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
        bot_checkbox = self.ui.botBox.isChecked()
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

        if bot_checkbox:
            opts.append("-b")

        result = process.run(opts)

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
