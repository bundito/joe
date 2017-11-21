# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'joe.ui'
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
        MainWindow.resize(524, 638)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("centralwidget: {background: #b6b6b6}"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.utilBox = QtGui.QWidget(self.centralwidget)
        self.utilBox.setGeometry(QtCore.QRect(80, 550, 391, 71))
        self.utilBox.setStyleSheet(_fromUtf8("QWidget {background: #a4a4a4}"))
        self.utilBox.setObjectName(_fromUtf8("utilBox"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.utilBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.configButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.configButton.setEnabled(True)
        self.configButton.setMinimumSize(QtCore.QSize(122, 50))
        self.configButton.setObjectName(_fromUtf8("configButton"))
        self.horizontalLayout.addWidget(self.configButton)
        self.revertButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.revertButton.setMinimumSize(QtCore.QSize(122, 50))
        self.revertButton.setObjectName(_fromUtf8("revertButton"))
        self.horizontalLayout.addWidget(self.revertButton)
        self.closeButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.closeButton.setMinimumSize(QtCore.QSize(122, 50))
        self.closeButton.setStyleSheet(_fromUtf8("QPushButton {background: white; border: 1px solid black}"))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(130, 110, 271, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 269, 369))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 341))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.itemGrid = QtGui.QGridLayout(self.gridLayoutWidget)
        self.itemGrid.setMargin(0)
        self.itemGrid.setVerticalSpacing(5)
        self.itemGrid.setObjectName(_fromUtf8("itemGrid"))
        self.trashbutton_0 = QtGui.QPushButton(self.gridLayoutWidget)
        self.trashbutton_0.setMinimumSize(QtCore.QSize(50, 50))
        self.trashbutton_0.setObjectName(_fromUtf8("trashbutton_0"))
        self.itemGrid.addWidget(self.trashbutton_0, 0, 1, 1, 1)
        self.titlebutton_0 = QtGui.QPushButton(self.gridLayoutWidget)
        self.titlebutton_0.setMinimumSize(QtCore.QSize(50, 50))
        self.titlebutton_0.setObjectName(_fromUtf8("titlebutton_0"))
        self.itemGrid.addWidget(self.titlebutton_0, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.itemGrid.addItem(spacerItem, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.configButton.setText(_translate("MainWindow", "Config", None))
        self.revertButton.setText(_translate("MainWindow", "Revert", None))
        self.closeButton.setText(_translate("MainWindow", "Close", None))
        self.trashbutton_0.setText(_translate("MainWindow", "PushButton", None))
        self.titlebutton_0.setText(_translate("MainWindow", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

