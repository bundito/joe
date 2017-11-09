#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout, QAbstractButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter, QPixmap, QIcon

from DownloadListing import Listing

import parser
import pickle

buttonHeight = 50

class ButtonTest(QDialog):

    def __init__(self):
        super(ButtonTest, self).__init__()

        app_height = (buttonHeight + 10) * len(Listing)

        self.top = 10
        self.left = 10
        self.width = 500
        self.height = app_height
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Directory Buttons")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createListingLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createListingLayout(self):
        self.horizontalGroupBox = QGroupBox("Joe")
        layout = QGridLayout()
        counter = 0

        for obj in Listing:
            runbutton = QPushButton(obj.filename)
            runbutton.clicked.connect(lambda checked, filename=obj.filename: self.on_runclick(filename))
            runbutton.setMinimumHeight(buttonHeight)

            trashbutton = QPushButton()
            trashbutton.setIcon(QIcon('./bw-trash-clipart.gif'))
            trashbutton.clicked.connect(lambda checked, filename=obj.filename: self.on_delclick(filename))
            trashbutton.setMaximumHeight(buttonHeight)
            trashbutton.setMaximumWidth(buttonHeight)

            layout.addWidget(runbutton, counter, 0, 1, 4)
            layout.addWidget(trashbutton, counter, 5, 1, 1)

            counter = counter + 1

        self.horizontalGroupBox.setLayout(layout)
    #
    # def createUtilLayout(self):
    #     self.horizontalGroupBox = QGroupBox("Utils")
    #     utilLayout = QGridLayout()
    #
    #     configButton = QPushButton("Config")
    #     revertButton = QPushButton("Revert")
    #     quitButton = QPushButton("Quit")
    #
    #     utilLayout.addwidget(configButton, 0, 0)
    #     utilLayout.addWidget(revertButton, 0, 1)
    #     utilLayout.addWidget(quitButton, 0, 2)

    #self.horizontalGroupBox.setLayout(utilLayout)


    @pyqtSlot()
    def on_runclick(self, filename):
        print("process %s" % filename)
        picklepass(filename)

    @pyqtSlot()
    def on_delclick(self, filename):
        print("rm -rf %s" % filename)


def picklepass(fname):
    for x in Listing:
        if x.filename == fname:
            golden = x

    kosher = pickle.dumps(golden)
    parser.sendquery(kosher, "-rename")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonTest()
    sys.exit(app.exec_())
