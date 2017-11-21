import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from Ui_joe_two import Ui_MainWindow

import DownloadListing

# from PyQt5 import QuickWidgets

app = QApplication(sys.argv) #     <—- QApp doesn’t change
window = QMainWindow() #                 <—— WidgetClass from UI
ui = Ui_MainWindow() #                   <—- def under class in .py file
ui.setupUi(window)

counter = 0
max = len(DownloadListing.Listing)

while counter < max:
    for obj in DownloadListing.Listing:
        titlebutton = QPushButton(obj.filename)
        trashbutton = QPushButton(obj.fullpath)
        titlebutton.setText = obj.filename

        ui.gridLayout_2.addWidget(titlebutton, counter, 0, 1, 1)
        ui.gridLayout_2.addWidget(trashbutton, counter, 1, 1, 1)

        counter = counter + 1

    #spacerItem = QSpacerItem(40, 20, QtQSizePolicy.Expanding, QSizePolicy.Minimum)
    #ui.gridLayout_2.addWidget(, 1, 1, , QSizePolicy.Minimum)




window.show()
sys.exit(app.exec_())