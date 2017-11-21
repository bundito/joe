# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joemain.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(425, 558)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 381, 30))
        font = QtGui.QFont()
        font.setFamily(".Al Tarikh PUA")
        font.setBold(True)
        font.setWeight(75)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.progNameLabel = MainWindow(self.widget_2)
        self.progNameLabel.setGeometry(QtCore.QRect(20, 0, 361, 16))
        self.progNameLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.progNameLabel.setObjectName("progNameLabel")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 490, 401, 61))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
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
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 401, 441))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 399, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 10, 391, 671))
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 391, 681))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.itemGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.itemGridLayout.setContentsMargins(5, 5, 5, 5)
        self.itemGridLayout.setVerticalSpacing(5)
        self.itemGridLayout.setObjectName("itemGridLayout")
        self.trashButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.trashButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trashButton.sizePolicy().hasHeightForWidth())
        self.trashButton.setSizePolicy(sizePolicy)
        self.trashButton.setMinimumSize(QtCore.QSize(50, 50))
        self.trashButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.trashButton.setBaseSize(QtCore.QSize(50, 50))
        self.trashButton.setStyleSheet("QPushButton#trashButton {\n"
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
"}")
        self.trashButton.setObjectName("trashButton")
        self.itemGridLayout.addWidget(self.trashButton, 0, 1, 1, 1)
        self.labelButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.labelButton.setMinimumSize(QtCore.QSize(0, 50))
        self.labelButton.setStyleSheet("QPushButton#labelButton {\n"
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
"}")
        self.labelButton.setObjectName("labelButton")
        self.itemGridLayout.addWidget(self.labelButton, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.itemGridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Joe"))
        self.progNameLabel.setText(_translate("Dialog", "TextLabel"))
        self.groupBox.setTitle(_translate("Dialog", "Utils"))
        self.configButton.setText(_translate("Dialog", "Config"))
        self.revertButton.setText(_translate("Dialog", "Revert"))
        self.quitButton.setText(_translate("Dialog", "Quit"))
        self.trashButton.setText(_translate("Dialog", "PushButton"))
        self.labelButton.setText(_translate("Dialog", "PushButton"))

from mainwindow import MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

