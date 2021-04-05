import datetime
import os
import subprocess
import webbrowser

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.about import Ui_about
from gui.main import Ui_mainWindow
from utils import config, model, thread, message
from widgets.settings import Settings

LOCAL_TIMEZONE = datetime.datetime.now(
    datetime.timezone.utc
).astimezone().tzinfo


class MainWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)  # noqa

        self.refreshing = False
        self.busy = False
        self.popen = None

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":icons/icon.png"))

        self.ui.actionQuit.triggered.connect(app.quit)
        self.ui.actionConfiguration.triggered.connect(self.open_settings)
        self.ui.actionWebsite.triggered.connect(self.open_website)
        self.ui.actionAbout.triggered.connect(self.open_about)

        self.ui.refreshButton.clicked.connect(self.refresh_list)
        self.ui.uploadButton.clicked.connect(self.upload_file)
        self.ui.downloadButton.clicked.connect(self.download_file)
        self.ui.cancelButton.clicked.connect(self.cancel_transfer)
        self.ui.renameButton.clicked.connect(self.rename_file)
        self.ui.deleteButton.clicked.connect(self.delete_file)

        self.file_model = model.FileModel()
        self.ui.tableView.setModel(self.file_model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(
            0,
            QHeaderView.Stretch
        )
        self.ui.tableView.horizontalHeader().setSectionResizeMode(
            1,
            QHeaderView.ResizeToContents
        )
        self.ui.tableView.horizontalHeader().setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents
        )

        self.threadpool = QThreadPool()
        self.refresh_list()

    #
    # Hide instead of close
    #
    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def rename_file(self):
        row_index = self.ui.tableView.currentIndex().row()
        if row_index == -1:
            return

        filename = \
            self.file_model.view[row_index][0]

        text, ok = QInputDialog.getText(
            self, f"Rename {filename}", "New filename:", QLineEdit.Normal,
            filename
        )
        if not ok or text == "" or text == filename:
            return

        result = subprocess.run(
            [config.dscli_bin, "mv", filename, text],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            shell=True
        )

        if result.returncode != 0:
            message.create(
                QMessageBox.Warning,
                "Warning",
                f"Failed to rename {filename} to {text}."
            ).exec()
            return

        self.refresh_list()

    def delete_file(self):
        row_index = self.ui.tableView.currentIndex().row()
        if row_index == -1:
            return

        filename = \
            self.file_model.view[row_index][0]

        reply = QMessageBox.question(
            self, f"Delete {filename}",
            f"Are you sure?",
            QMessageBox.Yes |
            QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        result = subprocess.run(
            [config.dscli_bin, "rm", filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            shell=True
        )

        if result.returncode != 0:
            message.create(
                QMessageBox.Warning,
                "Warning",
                f"Failed to delete {filename}."
            ).exec()
            return

        self.refresh_list()

    def cancel_transfer(self):
        if not self.busy:
            return

        self.popen.kill()

    def download_file(self):
        if self.busy:
            message.create(
                QMessageBox.Warning,
                "Warning",
                "Transfer busy."
            ).exec()
            return

        row_index = self.ui.tableView.currentIndex().row()
        if row_index == -1:
            return

        filename = \
            self.file_model.view[row_index][0]

        download_location = \
            QFileDialog.getSaveFileName(None, "Download file", filename)[0]

        if download_location == "":
            return

        self.ui.filenameLabel.setText(
            f"Downloading: {filename} -> {download_location}")
        self.busy = True

        def download_file_impl(progress_callback):
            self.popen = subprocess.Popen(
                [config.dscli_bin, "dl", filename, download_location, "-d"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                stdin=subprocess.PIPE,
                universal_newlines=True,
                shell=True
            )

            for stdout_line in iter(self.popen.stdout.readline, ""):
                if stdout_line == "":
                    continue

                try:
                    total, downloaded = [
                        int(x) for x in
                        stdout_line.strip().split()
                    ]
                except:
                    raise RuntimeError

                progress_callback.emit(int(100 * downloaded / total))

            self.popen.stdout.close()
            return_code = self.popen.wait()

            if return_code != 0:
                raise RuntimeError

        worker = thread.Worker(download_file_impl)

        worker.signals.progress.connect(self.update_progress_bar)
        worker.signals.result.connect(self.cleanup_transfer)
        worker.signals.error.connect(self.warning_transfer)

        self.threadpool.start(worker)

    def upload_file(self):
        if self.busy:
            message.create(
                QMessageBox.Warning,
                "Warning",
                "Transfer busy."
            ).exec()
            return

        filename = QFileDialog.getOpenFileName(None, "Upload file")[0]
        if filename == "":
            return

        text, ok = QInputDialog.getText(
            self, f"Upload {filename}", "Remote filename:", QLineEdit.Normal,
            os.path.basename(filename)
        )
        if not ok or text == "":
            return

        self.ui.filenameLabel.setText(f"Uploading: {filename} -> {text}")
        self.busy = True

        def upload_file_impl(progress_callback):
            self.popen = subprocess.Popen(
                [config.dscli_bin, "up", filename, text, "-d"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                stdin=subprocess.PIPE,
                universal_newlines=True,
                shell=True
            )

            for stdout_line in iter(self.popen.stdout.readline, ""):
                if stdout_line == "":
                    continue

                try:
                    total, uploaded = [
                        int(x) for x in
                        stdout_line.strip().split()
                    ]
                except:
                    raise RuntimeError

                progress_callback.emit(int(100 * uploaded / total))

            self.popen.stdout.close()
            return_code = self.popen.wait()

            if return_code != 0:
                raise RuntimeError

        worker = thread.Worker(upload_file_impl)

        worker.signals.progress.connect(self.update_progress_bar)
        worker.signals.result.connect(self.cleanup_transfer)
        worker.signals.error.connect(self.warning_transfer)

        self.threadpool.start(worker)

    def cleanup_transfer(self):
        self.ui.filenameLabel.setText("Idle")
        self.ui.progressBar.setValue(0)
        self.busy = False
        self.refresh_list()

    def warning_transfer(self):
        self.cleanup_transfer()
        message.create(
            QMessageBox.Warning,
            "Warning",
            "Transfer cancelled."
        ).exec()

    def update_progress_bar(self, progress):
        self.ui.progressBar.setValue(progress)

    def open_settings(self):
        self.hide()
        self.settings_dialog = Settings()
        self.settings_dialog.show()

    @staticmethod
    def open_website():
        webbrowser.open("https://github.com/darenliang/dsgui", new=2)

    def open_about(self):
        self.about_widget = QWidget()  # noqa

        self.about = Ui_about()
        self.about.setupUi(self.about_widget)
        self.about.label.setText(f"dsgui {config.dsgui_version}")
        self.about.imageLabel.setPixmap(QPixmap(":icons/icon.png"))

        self.about_widget.setWindowIcon(QIcon(":icons/icon.png"))
        self.about_widget.show()

    def refresh_list(self):
        if self.refreshing:
            return

        self.ui.statusbar.showMessage("Refreshing...")
        self.refreshing = True

        worker = thread.Worker(self.refresh_list_impl)
        worker.signals.result.connect(self.refresh_list_gui)
        worker.signals.error.connect(self.refresh_warning)

        self.threadpool.start(worker)

    def refresh_warning(self):
        self.ui.statusbar.showMessage("Refresh error")
        self.refreshing = False

    @staticmethod
    def refresh_list_impl(progress_callback):
        result = subprocess.run(
            [config.dscli_bin, "ls", "-l"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            shell=True
        )

        if result.returncode != 0:
            raise RuntimeError

        return result.stdout.decode()

    def refresh_list_gui(self, result):
        self.ui.statusbar.showMessage("Files loaded")
        self.refreshing = False

        lines = [x for x in result.split("\n") if x]

        files = []
        for i, line in enumerate(lines):
            filesize, timestamp, filename = line.split(" ", 2)
            timestamp = datetime.datetime.fromtimestamp(
                int(timestamp),
                tz=LOCAL_TIMEZONE
            ).strftime("%Y/%m/%d %H:%M:%S")

            files.append((filename, filesize, timestamp))

        self.file_model.set(files)
