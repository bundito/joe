import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout, QButtonGroup
from PyQt5.QtCore import *

from DirListing import Listing


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Grid Test'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()

        counter = 0

        class Widget(QWidget):
            def __init__(self, *args, **kwargs):
                QWidget.__init__(self, *args, **kwargs)
                self.setLayout(QVBoxLayout())
                group = QButtonGroup(self)
                for i in range(10):
                    button = QPushButton("{}".format(i), self)
                    self.layout().addWidget(button)
                    group.addButton(button, i)
                group.buttonClicked[int].connect(self.on_click)
                group.buttonClicked.connect(self.on_click2)


        @pyqtSlot(int)
        def on_click(self, i):
            print("button-{}".format(i))

        def on_click2(self, btn):
            print("2button-{}".format(btn.text()))

def lower(self):
    if __name__ == '__main__':
        app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())