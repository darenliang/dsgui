from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def create(icon, title, text):
    msg = QMessageBox()
    msg.setWindowIcon(QIcon(":icons/icon.png"))
    msg.setIcon(icon)
    msg.setWindowTitle(title)
    msg.setText(text)
    return msg
