# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(50, 60, 312, 173))
        self.calendarWidget.setObjectName("calendarWidget")
        self.OkButton = QtWidgets.QPushButton(Dialog)
        self.OkButton.setGeometry(QtCore.QRect(240, 240, 113, 32))
        self.OkButton.setObjectName("OkButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(120, 240, 113, 32))
        self.cancelButton.setObjectName("cancelButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 331, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.OkButton.setText(_translate("Dialog", "Ok"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.label.setText(_translate("Dialog", "titleLabel"))

