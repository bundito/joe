# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_config.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 433)
        self.mediaBox = QtWidgets.QGroupBox(Dialog)
        self.mediaBox.setGeometry(QtCore.QRect(10, 40, 481, 151))
        self.mediaBox.setObjectName("mediaBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.mediaBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 40, 431, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.direcoryGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.direcoryGrid.setContentsMargins(0, 0, 0, 0)
        self.direcoryGrid.setObjectName("direcoryGrid")
        self.tvLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.tvLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tvLabel.setObjectName("tvLabel")
        self.direcoryGrid.addWidget(self.tvLabel, 1, 0, 1, 1)
        self.moviesLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.moviesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.moviesLabel.setObjectName("moviesLabel")
        self.direcoryGrid.addWidget(self.moviesLabel, 0, 0, 1, 1)
        self.downloadLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.downloadLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.downloadLabel.setObjectName("downloadLabel")
        self.direcoryGrid.addWidget(self.downloadLabel, 2, 0, 1, 1)
        self.moviesChoose = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.moviesChoose.setObjectName("moviesChoose")
        self.direcoryGrid.addWidget(self.moviesChoose, 0, 3, 1, 1)
        self.tvChoose = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.tvChoose.setObjectName("tvChoose")
        self.direcoryGrid.addWidget(self.tvChoose, 1, 3, 1, 1)
        self.tvEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.tvEdit.setObjectName("tvEdit")
        self.direcoryGrid.addWidget(self.tvEdit, 1, 1, 1, 2)
        self.downloadEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.downloadEdit.setObjectName("downloadEdit")
        self.direcoryGrid.addWidget(self.downloadEdit, 2, 1, 1, 2)
        self.downloadChoose = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.downloadChoose.setObjectName("downloadChoose")
        self.direcoryGrid.addWidget(self.downloadChoose, 2, 3, 1, 1)
        self.moviesEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.moviesEdit.setObjectName("moviesEdit")
        self.direcoryGrid.addWidget(self.moviesEdit, 0, 1, 1, 2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(70, 390, 421, 32))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.okCancelLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.okCancelLayout.setContentsMargins(0, 0, 0, 0)
        self.okCancelLayout.setObjectName("okCancelLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.okCancelLayout.addItem(spacerItem)
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.cancelButton.setObjectName("cancelButton")
        self.okCancelLayout.addWidget(self.cancelButton)
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.saveButton.setObjectName("saveButton")
        self.okCancelLayout.addWidget(self.saveButton)
        self.varsBox = QtWidgets.QGroupBox(Dialog)
        self.varsBox.setGeometry(QtCore.QRect(10, 200, 491, 181))
        self.varsBox.setObjectName("varsBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.varsBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 20, 421, 153))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.varsGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.varsGridLayout.setContentsMargins(0, 0, 0, 0)
        self.varsGridLayout.setObjectName("varsGridLayout")
        self.progNameLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.progNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progNameLabel.setObjectName("progNameLabel")
        self.varsGridLayout.addWidget(self.progNameLabel, 0, 0, 1, 1)
        self.progLocationChooser = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.progLocationChooser.setObjectName("progLocationChooser")
        self.varsGridLayout.addWidget(self.progLocationChooser, 3, 4, 1, 1)
        self.testmodeCheck = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.testmodeCheck.setObjectName("testmodeCheck")
        self.varsGridLayout.addWidget(self.testmodeCheck, 4, 1, 1, 1)
        self.progdirLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.progdirLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progdirLabel.setObjectName("progdirLabel")
        self.varsGridLayout.addWidget(self.progdirLabel, 3, 0, 1, 1)
        self.prognameEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.prognameEdit.setObjectName("prognameEdit")
        self.varsGridLayout.addWidget(self.prognameEdit, 0, 1, 1, 4)
        self.binDirectory = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binDirectory.sizePolicy().hasHeightForWidth())
        self.binDirectory.setSizePolicy(sizePolicy)
        self.binDirectory.setObjectName("binDirectory")
        self.varsGridLayout.addWidget(self.binDirectory, 3, 1, 1, 3)
        self.filebotChooser = QtWidgets.QToolButton(self.gridLayoutWidget_2)
        self.filebotChooser.setObjectName("filebotChooser")
        self.varsGridLayout.addWidget(self.filebotChooser, 2, 4, 1, 1)
        self.versionEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionEdit.sizePolicy().hasHeightForWidth())
        self.versionEdit.setSizePolicy(sizePolicy)
        self.versionEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.versionEdit.setBaseSize(QtCore.QSize(75, 0))
        self.versionEdit.setObjectName("versionEdit")
        self.varsGridLayout.addWidget(self.versionEdit, 1, 1, 1, 1)
        self.versionLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.versionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.versionLabel.setObjectName("versionLabel")
        self.varsGridLayout.addWidget(self.versionLabel, 1, 0, 1, 1)
        self.filebotLocEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.filebotLocEdit.setObjectName("filebotLocEdit")
        self.varsGridLayout.addWidget(self.filebotLocEdit, 2, 1, 1, 3)
        self.filebotLocLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.filebotLocLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filebotLocLabel.setObjectName("filebotLocLabel")
        self.varsGridLayout.addWidget(self.filebotLocLabel, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.varsGridLayout.addItem(spacerItem1, 1, 2, 1, 2)
        self.windowLabel = QtWidgets.QLabel(Dialog)
        self.windowLabel.setGeometry(QtCore.QRect(-280, 20, 501, 16))
        font = QtGui.QFont()
        font.setFamily("Al Tarikh")
        self.windowLabel.setFont(font)
        self.windowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.windowLabel.setObjectName("windowLabel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 481, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mediaBox.setTitle(_translate("Dialog", "Media Directories"))
        self.tvLabel.setText(_translate("Dialog", "TV Shows"))
        self.moviesLabel.setText(_translate("Dialog", "Movies"))
        self.downloadLabel.setText(_translate("Dialog", "Downloads"))
        self.moviesChoose.setText(_translate("Dialog", "..."))
        self.tvChoose.setText(_translate("Dialog", "..."))
        self.downloadChoose.setText(_translate("Dialog", "..."))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.saveButton.setText(_translate("Dialog", "OK"))
        self.varsBox.setTitle(_translate("Dialog", "System Variables"))
        self.progNameLabel.setText(_translate("Dialog", "Program Title"))
        self.progLocationChooser.setText(_translate("Dialog", "..."))
        self.testmodeCheck.setText(_translate("Dialog", "Test Mode"))
        self.progdirLabel.setText(_translate("Dialog", "Program Directory"))
        self.filebotChooser.setText(_translate("Dialog", "..."))
        self.versionLabel.setText(_translate("Dialog", "Version Number"))
        self.filebotLocLabel.setText(_translate("Dialog", "Filebot Location"))
        self.windowLabel.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

