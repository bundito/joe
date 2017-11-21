# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combowindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setGeometry(QtCore.QRect(0, 10, 731, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickWidget.sizePolicy().hasHeightForWidth())
        self.quickWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Al Tarikh")
        self.quickWidget.setFont(font)
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 450, 441, 71))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 401, 47))
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
        self.scrollArea.setGeometry(QtCore.QRect(50, 50, 401, 401))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 391, 401))
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.itemGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.itemGridLayout.setContentsMargins(5, 5, 5, 5)
        self.itemGridLayout.setVerticalSpacing(5)
        self.itemGridLayout.setObjectName("itemGridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.itemGridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.resultswidget = QtWidgets.QWidget(self.centralwidget)
        self.resultswidget.setGeometry(QtCore.QRect(490, 50, 231, 261))
        self.resultswidget.setObjectName("resultswidget")
        self.result_title = QtWidgets.QLabel(self.resultswidget)
        self.result_title.setGeometry(QtCore.QRect(10, 10, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.result_title.setFont(font)
        self.result_title.setAlignment(QtCore.Qt.AlignCenter)
        self.result_title.setObjectName("result_title")
        self.foundTitle = QtWidgets.QLabel(self.resultswidget)
        self.foundTitle.setGeometry(QtCore.QRect(10, 40, 211, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.foundTitle.setFont(font)
        self.foundTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.foundTitle.setObjectName("foundTitle")
        self.episodesBox = QtWidgets.QGroupBox(self.resultswidget)
        self.episodesBox.setGeometry(QtCore.QRect(10, 60, 221, 61))
        self.episodesBox.setObjectName("episodesBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.episodesBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 201, 42))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Utils"))
        self.configButton.setText(_translate("MainWindow", "Config"))
        self.revertButton.setText(_translate("MainWindow", "Revert"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.result_title.setText(_translate("MainWindow", "Title"))
        self.foundTitle.setText(_translate("MainWindow", "Title"))
        self.episodesBox.setTitle(_translate("MainWindow", "Episodes"))

from PyQt5 import QtQuickWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

