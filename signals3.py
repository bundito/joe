#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout
from PyQt5.QtCore import pyqtSlot

from DownloadListing import Listing

#print(len(Listing))

class ButtonTest(QDialog):
    def __init__(self):
        super(ButtonTest, self).__init__()
        self.top = 10
        self.left = 10
        self.width = 320
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Directory Buttons")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Joe")
        layout = QGridLayout()
        counter = 0

        buttonHeight = (self.height / len(Listing)) - 20

        for obj in Listing:
            button = QPushButton(obj.filename)
            button.clicked.connect(lambda checked, filename=obj.filename: self.on_click(filename))
            button.setMinimumHeight(buttonHeight)
            button.isFlat()
            layout.addWidget(button, counter, 0)
            counter = counter + 1

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_click(self, filename):
        print(filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonTest()
    sys.exit(app.exec_())
