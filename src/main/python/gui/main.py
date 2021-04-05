# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.uploadButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadButton.setObjectName("uploadButton")
        self.horizontalLayout_2.addWidget(self.uploadButton)
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout_2.addWidget(self.downloadButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.renameButton = QtWidgets.QPushButton(self.centralwidget)
        self.renameButton.setObjectName("renameButton")
        self.horizontalLayout_2.addWidget(self.renameButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_2.addWidget(self.refreshButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setDefaultSectionSize(23)
        self.verticalLayout.addWidget(self.tableView)
        self.filenameLabel = QtWidgets.QLabel(self.centralwidget)
        self.filenameLabel.setObjectName("filenameLabel")
        self.verticalLayout.addWidget(self.filenameLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(mainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionWebsite = QtWidgets.QAction(mainWindow)
        self.actionWebsite.setObjectName("actionWebsite")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionConfiguration = QtWidgets.QAction(mainWindow)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionWebsite)
        self.menuAbout.addAction(self.actionAbout)
        self.menuSettings.addAction(self.actionConfiguration)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Dsgui"))
        self.uploadButton.setText(_translate("mainWindow", "Upload File"))
        self.downloadButton.setText(_translate("mainWindow", "Download File"))
        self.cancelButton.setText(_translate("mainWindow", "Cancel Transfer"))
        self.renameButton.setText(_translate("mainWindow", "Rename"))
        self.deleteButton.setText(_translate("mainWindow", "Delete"))
        self.refreshButton.setText(_translate("mainWindow", "Refresh File List"))
        self.filenameLabel.setText(_translate("mainWindow", "Idle"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuAbout.setTitle(_translate("mainWindow", "Help"))
        self.menuSettings.setTitle(_translate("mainWindow", "Settings"))
        self.actionQuit.setText(_translate("mainWindow", "Quit"))
        self.actionWebsite.setText(_translate("mainWindow", "Website"))
        self.actionAbout.setText(_translate("mainWindow", "About"))
        self.actionConfiguration.setText(_translate("mainWindow", "Configuration"))