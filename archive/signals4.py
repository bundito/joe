#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout, QButtonGroup
from PyQt5.QtCore import pyqtSlot

from DirListing import Listing

class ButtonTest(QDialog):
    def __init__(self):
        super(ButtonTest, self).__init__()
        self.top = 10
        self.left = 10
        self.width = 320
        self.height = 500
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
        group = QButtonGroup(self)

        for obj in Listing:
            button = QPushButton(obj.filename)
            layout.addWidget(button, counter, 0)
            counter = counter + 1
            group.addButton(button, counter)
        group.buttonClicked[int].connect(self.on_click)
        group.buttonClicked.connect(self.on_click2)

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot(int)
    def on_click(self, i):
        print("button{}".format(i))

    def on_click2(self, btn):
        print(btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonTest()
    sys.exit(app.exec_())
