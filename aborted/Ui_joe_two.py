# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joe_two.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(40, 30, 401, 401))
        self.scrollArea_2.setWidgetResizable(False)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 399, 459))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 391, 401))
        self.widget_2.setObjectName("widget_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.widget_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 361, 381))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.itemGridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.itemGridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.itemGridLayout_2.setVerticalSpacing(5)
        self.itemGridLayout_2.setObjectName("itemGridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.itemGridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 440, 441, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 20, 401, 47))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.configButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configButton_2.sizePolicy().hasHeightForWidth())
        self.configButton_2.setSizePolicy(sizePolicy)
        self.configButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.configButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.configButton_2.setStyleSheet("QPushButton#configButton {\n"
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
        self.configButton_2.setObjectName("configButton_2")
        self.gridLayout_2.addWidget(self.configButton_2, 0, 0, 1, 1)
        self.revertButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.revertButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.revertButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.revertButton_2.setBaseSize(QtCore.QSize(0, 0))
        self.revertButton_2.setStyleSheet("QPushButton#revertButton {\n"
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
        self.revertButton_2.setObjectName("revertButton_2")
        self.gridLayout_2.addWidget(self.revertButton_2, 0, 1, 1, 1)
        self.quitButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quitButton_2.sizePolicy().hasHeightForWidth())
        self.quitButton_2.setSizePolicy(sizePolicy)
        self.quitButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.quitButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.quitButton_2.setStyleSheet("QPushButton#quitButton {\n"
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
        self.quitButton_2.setObjectName("quitButton_2")
        self.gridLayout_2.addWidget(self.quitButton_2, 0, 2, 1, 1)
        self.programTitle_2 = QtWidgets.QLabel(self.centralwidget)
        self.programTitle_2.setGeometry(QtCore.QRect(40, 10, 391, 16))
        font = QtGui.QFont()
        font.setFamily("Al Tarikh")
        font.setBold(False)
        font.setWeight(50)
        self.programTitle_2.setFont(font)
        self.programTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.programTitle_2.setObjectName("programTitle_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Utils"))
        self.configButton_2.setText(_translate("MainWindow", "Config"))
        self.revertButton_2.setText(_translate("MainWindow", "Revert"))
        self.quitButton_2.setText(_translate("MainWindow", "Quit"))
        self.programTitle_2.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

