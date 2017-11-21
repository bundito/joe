                                        #!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

This example shows a tooltip on
a window and a button

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys
from PyQt5.QtWidgets import QPushButton, QToolTip, QWidget, QApplication
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize, QRect, pyqtSlot, QPropertyAnimation, QObject

import joe_sender

joe_sender.sendmessage("dir")

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        btn2 = QPushButton("This is a very long pushbutton", self)
        btn2.move(100,100)
        btn2.setGeometry(QRect(0,0,250,50))
        btn2.setMinimumSize(QSize(250,50))

        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Tooltips')
        self.show()

        btn.clicked.connect(lambda checked, i=1: self.send_data( "dir"))
        #btn2.clicked.connect(lambda checked, i=1: self.fade())


    def send_data(self, data):
        message = joe_sender.sendmessage(data)
        print(message)

    #                                                                                                                                                                                       def shrink(self, obj):
        # btn = obj
        # print(btn.minimumSize())
        # btn.anim = QPropertyAnimation(self, b'minimumSize')
        # btn.anim.setDuration(1000)
        # sizeStart = QSize(250,50)
        # sizeEnd = QSize(5, 50)
        # btn.anim.startValue(sizeStart)
        # btn.anim.endValue(sizeEnd)
        # # btn.anim.start()



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()