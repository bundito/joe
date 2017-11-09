#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout, QAbstractButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter, QPixmap

from DownloadListing import Listing



class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()



class ButtonTest(QDialog):

    def __init__(self):
        super(ButtonTest, self).__init__()
        self.top = 10
        self.left = 10
        self.width = 500
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
        buttonHeight = 50

        for obj in Listing:
            runbutton = QPushButton(obj.filename[0:20])
            runbutton.clicked.connect(lambda checked, filename=obj.filename: self.on_runclick(filename))
            runbutton.setMinimumHeight(buttonHeight)
            #runbutton.setFlat(True)


            trashbutton = PicButton(QPixmap('./trash_can.png'))

            trashbutton.clicked.connect(lambda checked, filename=obj.filename: self.on_delclick(filename))
            #trashbutton.resize(50,50)
            trashbutton.setMaximumHeight(50)
            trashbutton.setMaximumWidth(50)
            layout.addWidget(runbutton, counter, 0, 1, 4)
            layout.addWidget(trashbutton, counter, 5, 1, 1)

            counter = counter + 1

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_runclick(self, filename):
        print("process %s" % filename)

    @pyqtSlot()
    def on_delclick(self, filename):
        print("rm -rf %s" % filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonTest()
    sys.exit(app.exec_())
