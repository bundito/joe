import sys

from PyQt4 import QtGui
from Ui_scroller import Ui_MainWindow

import DownloadListing

app = QtGui.QApplication(sys.argv) #       <—- QApp doesn’t change
window = QtGui.QMainWindow()           #       <—— WidgetClass from UI
ui = Ui_MainWindow()        #       <—- def under class in .py file
ui.setupUi(window)


myform = QtGui.QGridLayout()
count = 0
for obj in DownloadListing.Listing:
    filename = obj.filename
    button1 = QtGui.QPushButton("Hi!")
    button1.setMinimumHeight(50)
    button2 = QtGui.QPushButton(filename)
    button2.setMinimumHeight(50)
    myform.addWidget(button2, count, 0, 1, 1)
    myform.addWidget(button1, count, 1,1,1)
    count = count + 1



ui.scrollWidget.setLayout(myform)
0

#ui.scrollArea.setWidgetResizable(True)
#ui.scrollArea.setWidget(ui.scrollWidget)
#ui.scrollArea.setFixedHeight(250)






window.show()
sys.exit(app.exec_())
