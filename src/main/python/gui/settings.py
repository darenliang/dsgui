# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings.sizePolicy().hasHeightForWidth())
        settings.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(settings)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.quickstartLabel = QtWidgets.QLabel(settings)
        self.quickstartLabel.setTextFormat(QtCore.Qt.RichText)
        self.quickstartLabel.setOpenExternalLinks(True)
        self.quickstartLabel.setObjectName("quickstartLabel")
        self.verticalLayout.addWidget(self.quickstartLabel)
        self.userTokenLabel = QtWidgets.QLabel(settings)
        self.userTokenLabel.setObjectName("userTokenLabel")
        self.verticalLayout.addWidget(self.userTokenLabel)
        self.userTokenLineEdit = QtWidgets.QLineEdit(settings)
        self.userTokenLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userTokenLineEdit.setObjectName("userTokenLineEdit")
        self.verticalLayout.addWidget(self.userTokenLineEdit)
        self.botBox = QtWidgets.QCheckBox(settings)
        self.botBox.setObjectName("botBox")
        self.verticalLayout.addWidget(self.botBox)
        self.serverIDLabel = QtWidgets.QLabel(settings)
        self.serverIDLabel.setObjectName("serverIDLabel")
        self.verticalLayout.addWidget(self.serverIDLabel)
        self.serverIDLineEdit = QtWidgets.QLineEdit(settings)
        self.serverIDLineEdit.setObjectName("serverIDLineEdit")
        self.verticalLayout.addWidget(self.serverIDLineEdit)
        self.checkBox = QtWidgets.QCheckBox(settings)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ok = QtWidgets.QPushButton(settings)
        self.ok.setObjectName("ok")
        self.horizontalLayout.addWidget(self.ok)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Dscli Settings"))
        self.quickstartLabel.setText(_translate("settings", "For a guide on how to get set up: <a href=\"https://github.com/darenliang/dscli/blob/master/quickstart/README.md\">Quickstart Guide</a><br><br>"))
        self.userTokenLabel.setText(_translate("settings", "Discord Token:"))
        self.botBox.setText(_translate("settings", "Is this token for a Bot?"))
        self.serverIDLabel.setText(_translate("settings", "Server ID:"))
        self.checkBox.setText(_translate("settings", "Delete all channels in server"))
        self.ok.setText(_translate("settings", "OK"))
