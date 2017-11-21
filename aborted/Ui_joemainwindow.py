# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joe_mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(477, 591)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 490, 401, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 401, 47))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.configButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configButton.sizePolicy().hasHeightForWidth())
        self.configButton.setSizePolicy(sizePolicy)
        self.configButton.setMinimumSize(QtCore.QSize(0, 0))
        self.configButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.configButton.setStyleSheet(_fromUtf8("QPushButton#configButton {\n"
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
"}"))
        self.configButton.setObjectName(_fromUtf8("configButton"))
        self.gridLayout.addWidget(self.configButton, 0, 0, 1, 1)
        self.revertButton = QtGui.QPushButton(self.layoutWidget)
        self.revertButton.setMinimumSize(QtCore.QSize(0, 35))
        self.revertButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.revertButton.setBaseSize(QtCore.QSize(0, 0))
        self.revertButton.setStyleSheet(_fromUtf8("QPushButton#revertButton {\n"
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
"}"))
        self.revertButton.setObjectName(_fromUtf8("revertButton"))
        self.gridLayout.addWidget(self.revertButton, 0, 1, 1, 1)
        self.quitButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton.sizePolicy().hasHeightForWidth())
        self.quitButton.setSizePolicy(sizePolicy)
        self.quitButton.setMinimumSize(QtCore.QSize(0, 0))
        self.quitButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.quitButton.setStyleSheet(_fromUtf8("QPushButton#quitButton {\n"
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
"}"))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.gridLayout.addWidget(self.quitButton, 0, 2, 1, 1)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(50, 10, 381, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8(".Al Tarikh PUA"))
        font.setBold(True)
        font.setWeight(75)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.progNameLabel = MainWindow(self.widget_2)
        self.progNameLabel.setGeometry(QtCore.QRect(10, 0, 361, 21))
        self.progNameLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.progNameLabel.setObjectName(_fromUtf8("progNameLabel"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 40, 401, 441))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-15, 0, 399, 459))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 10, 391, 671))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 681))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.itemGridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.itemGridLayout.setMargin(5)
        self.itemGridLayout.setVerticalSpacing(5)
        self.itemGridLayout.setObjectName(_fromUtf8("itemGridLayout"))
        self.trashButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.trashButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trashButton.sizePolicy().hasHeightForWidth())
        self.trashButton.setSizePolicy(sizePolicy)
        self.trashButton.setMinimumSize(QtCore.QSize(50, 50))
        self.trashButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.trashButton.setBaseSize(QtCore.QSize(50, 50))
        self.trashButton.setStyleSheet(_fromUtf8("QPushButton#trashButton {\n"
"    border-style: outset;\n"
"    background-color: white;\n"
"    border-width: 1px;\n"
"    border-radius: 1px;\n"
"    border-color: black;\n"
"    font: 12px;\n"
"}\n"
"QPushButton#trashButton:pressed {\n"
"    background-color: #afafaf;\n"
"    border-style: inset;\n"
"}"))
        self.trashButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../bw-trash-clipart.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.trashButton.setIcon(icon)
        self.trashButton.setIconSize(QtCore.QSize(36, 36))
        self.trashButton.setObjectName(_fromUtf8("trashButton"))
        self.itemGridLayout.addWidget(self.trashButton, 0, 1, 1, 1)
        self.labelButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.labelButton.setMinimumSize(QtCore.QSize(0, 50))
        self.labelButton.setStyleSheet(_fromUtf8("QPushButton#labelButton {\n"
"    border-style: outset;\n"
"    background-color: white;\n"
"    border-width: 1px;\n"
"    border-radius: 1px;\n"
"    border-color: black;\n"
"    font: 12px;\n"
"}\n"
"QPushButton#labelButton:pressed {\n"
"    background-color: #afafaf;\n"
"    border-style: inset;\n"
"}"))
        self.labelButton.setObjectName(_fromUtf8("labelButton"))
        self.itemGridLayout.addWidget(self.labelButton, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.itemGridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Utils", None))
        self.configButton.setText(_translate("MainWindow", "Config", None))
        self.revertButton.setText(_translate("MainWindow", "Revert", None))
        self.quitButton.setText(_translate("MainWindow", "Quit", None))
        self.progNameLabel.setText(_translate("MainWindow", "TextLabel", None))
        self.labelButton.setText(_translate("MainWindow", "PushButton", None))


