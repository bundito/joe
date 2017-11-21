# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joe_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWin(object):
    def setupUi(self, mainWin):
        mainWin.setObjectName("mainWin")
        mainWin.resize(477, 591)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWin.sizePolicy().hasHeightForWidth())
        mainWin.setSizePolicy(sizePolicy)
        mainWin.setStyleSheet("QMainWindow {background: rgb(82, 134, 210)}")
        self.centralwidget = QtWidgets.QWidget(mainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.utilGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.utilGroupBox.setGeometry(QtCore.QRect(50, 490, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.utilGroupBox.setFont(font)
        self.utilGroupBox.setObjectName("utilGroupBox")
        self.layoutWidget = QtWidgets.QWidget(self.utilGroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 401, 47))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.configButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configButton.sizePolicy().hasHeightForWidth())
        self.configButton.setSizePolicy(sizePolicy)
        self.configButton.setMinimumSize(QtCore.QSize(0, 0))
        self.configButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.configButton.setStyleSheet("QPushButton#configButton {\n"
"    border-style: outset;\n"
"    background-color: white;\n"
"    border-width: 1px;\n"
"    border-radius: 1px;\n"
"    border-color: black;\n"
"    font: 12px;\n"
"}\n"
"QPushButton#configButton:pressed {\n"
"    background-color: #afafaf;\n"
"    border-style: inset;\n"
"}")
        self.configButton.setObjectName("configButton")
        self.gridLayout.addWidget(self.configButton, 0, 0, 1, 1)
        self.revertButton = QtWidgets.QPushButton(self.layoutWidget)
        self.revertButton.setMinimumSize(QtCore.QSize(0, 35))
        self.revertButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.revertButton.setBaseSize(QtCore.QSize(0, 0))
        self.revertButton.setStyleSheet("QPushButton#revertButton {\n"
"    border-style: outset;\n"
"    background-color: white;\n"
"    border-width: 1px;\n"
"    border-radius: 1px;\n"
"    border-color: black;\n"
"    font: 12px;\n"
"}\n"
"QPushButton#revertButton:pressed {\n"
"    background-color: #afafaf;\n"
"    border-style: inset;\n"
"}")
        self.revertButton.setObjectName("revertButton")
        self.gridLayout.addWidget(self.revertButton, 0, 1, 1, 1)
        self.quitButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        self.quitButton.setMinimumSize(QtCore.QSize(0, 0))
        self.quitButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.quitButton.setStyleSheet("QPushButton#quitButton {\n"
"    border-style: outset;\n"
"    background-color: white;\n"
"    border-width: 1px;\n"
"    border-radius: 1px;\n"
"    border-color: black;\n"
"    font: 12px;\n"
"}\n"
"QPushButton#quitButton:pressed {\n"
"    background-color: #afafaf;\n"
"    border-style: inset;\n"
"}")
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 0, 2, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 50, 400, 430))
        self.scrollArea.setStyleSheet("QWidget {background: rgb(82, 134, 210)}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("QScrollArea {border: 1px solid black}")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 200))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setStyleSheet("﻿QWidget {background: rgb(82, 134, 210)}")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.itemGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.itemGrid.setContentsMargins(3, 3, 3, 3)
        self.itemGrid.setHorizontalSpacing(0)
        self.itemGrid.setObjectName("itemGrid")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.itemGrid.addItem(spacerItem, 0, 1, 1, 1)
        self.trashbutton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trashbutton_0.sizePolicy().hasHeightForWidth())
        self.trashbutton_0.setSizePolicy(sizePolicy)
        self.trashbutton_0.setMinimumSize(QtCore.QSize(50, 50))
        self.trashbutton_0.setMaximumSize(QtCore.QSize(50, 50))
        self.trashbutton_0.setStyleSheet("QPushButton {background: white; border 1px solid black}\n"
"QPushButton.pushed {background: #a6a6a6}")
        self.trashbutton_0.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bw-trash-clipart.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trashbutton_0.setIcon(icon)
        self.trashbutton_0.setIconSize(QtCore.QSize(36, 36))
        self.trashbutton_0.setObjectName("trashbutton_0")
        self.itemGrid.addWidget(self.trashbutton_0, 0, 2, 1, 1)
        self.labelbutton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.labelbutton_0.setMinimumSize(QtCore.QSize(315, 50))
        self.labelbutton_0.setStyleSheet("QPushButton {background: white; border 1px solid black}\n"
"QPushButton.pushed {background: #a6a6a6}")
        self.labelbutton_0.setObjectName("labelbutton_0")
        self.itemGrid.addWidget(self.labelbutton_0, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.itemGrid.addItem(spacerItem1, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 461, 31))
        self.widget.setObjectName("widget")
        self.progNameLabel = QtWidgets.QLabel(self.widget)
        self.progNameLabel.setGeometry(QtCore.QRect(50, 5, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progNameLabel.setFont(font)
        self.progNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progNameLabel.setObjectName("progNameLabel")
        self.widget.raise_()
        self.utilGroupBox.raise_()
        self.scrollArea.raise_()
        mainWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWin)
        self.statusbar.setObjectName("statusbar")
        mainWin.setStatusBar(self.statusbar)

        self.retranslateUi(mainWin)
        QtCore.QMetaObject.connectSlotsByName(mainWin)

    def retranslateUi(self, mainWin):
        _translate = QtCore.QCoreApplication.translate
        mainWin.setWindowTitle(_translate("mainWin", "MainWindow"))
        self.utilGroupBox.setTitle(_translate("mainWin", "Utils"))
        self.configButton.setText(_translate("mainWin", "Config"))
        self.revertButton.setText(_translate("mainWin", "Revert"))
        self.quitButton.setText(_translate("mainWin", "Quit"))
        self.labelbutton_0.setText(_translate("mainWin", "PushButton"))
        self.progNameLabel.setText(_translate("mainWin", "TextLabel"))

