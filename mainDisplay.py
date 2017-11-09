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
        windowLayout = QVBoxLayout()

        self.createListingLayout()
        windowLayout.addWidget(self.horizontalGroupBox)

        windowLayout.addStretch(2)

        self.createUtilLayout()
        windowLayout.addWidget(self.horizontalGroupBox)

        self.setLayout(windowLayout)

        self.show()

    itemlayout = QGridLayout()

    def createListingLayout(self):
        self.horizontalGroupBox = QGroupBox("Joe")

        counter = 0

        for obj in Listing:
            runbutton = QPushButton(obj.filename)
            runbutton.clicked.connect(lambda checked, filename=obj.filename: self.on_runclick(filename))
            runbutton.setMinimumHeight(buttonHeight)

            trashbutton = QPushButton()
            trashbutton.setIcon(QIcon('./bw-trash-clipart.gif'))
            trashbutton.clicked.connect(lambda checked, count = counter: self.on_delclick(count))
            trashbutton.setMaximumHeight(buttonHeight)
            trashbutton.setMaximumWidth(buttonHeight)

            self.itemlayout.addWidget(runbutton, counter, 0, 1, 4)
            self.itemlayout.addWidget(trashbutton, counter, 5, 1, 1)

            counter = counter + 1

        self.horizontalGroupBox.setLayout(self.itemlayout)

    def removeItem(self, rowNumber):
        removeTitle = self.itemlayout.itemAtPosition(rowNumber, 0)
        removeTrash = self.itemlayout.itemAtPosition(rowNumber, 5)
        self.itemlayout.removeItem(removeTitle)
        self.itemlayout.removeItem(removeTrash)
        removeTitle.widget().deleteLater()
        removeTrash.widget().deleteLater()

    def createUtilLayout(self):
         self.horizontalGroupBox = QGroupBox("Utils")
         layout = QGridLayout()

         configButton = QPushButton("Config")
         revertButton = QPushButton("Revert")
         quitButton = QPushButton("Quit")

         layout.addWidget(configButton, 0, 0)
         layout.addWidget(revertButton, 0, 1)
         layout.addWidget(quitButton, 0, 2)

         self.horizontalGroupBox.setLayout(layout)


    @pyqtSlot()
    def on_runclick(self, filename):
        print("process %s" % filename)
        picklepass(filename)

    @pyqtSlot()
    def on_delclick(self, filename):
        print("rm -rf %s" % filename)
        self.removeItem(filename)



def picklepass(fname):
    for x in Listing:
        if x.filename == fname:
            golden = x
            break

    kosher = pickle.dumps(golden)
    parser.sendquery(kosher, "-rename")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonTest()
    sys.exit(app.exec_())
