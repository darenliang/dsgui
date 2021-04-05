from PyQt5.QtCore import *

from utils import filesize


class FileModel(QAbstractTableModel):
    def __init__(self):
        super(FileModel, self).__init__()
        self.files = []
        self.view = []
        self.columns = ["Name", "Size", "Date created"]
        self.column_sort = 0
        self.reverse_sort = False

    def set(self, files):
        self.layoutAboutToBeChanged.emit()
        self.files = files
        self.sort_files()
        self.layoutChanged.emit()

    def sort_files(self):
        if self.column_sort == 0 or self.column_sort == 2:
            self.view = sorted(
                self.files,
                key=lambda x: x[self.column_sort].lower(),
                reverse=self.reverse_sort
            )
        # custom view for size
        elif self.column_sort == 1:
            self.view = sorted(
                self.files,
                key=lambda x: x[self.column_sort],
                reverse=self.reverse_sort
            )

    def sort(self, Ncol, order):
        self.layoutAboutToBeChanged.emit()
        self.column_sort = Ncol
        self.reverse_sort = order == Qt.AscendingOrder
        self.sort_files()
        self.layoutChanged.emit()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            if index.column() == 1:
                return filesize.naturalsize(
                    self.view[index.row()][index.column()]
                )
            else:
                return self.view[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.files)

    def columnCount(self, index):
        return 3

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.columns[section])
