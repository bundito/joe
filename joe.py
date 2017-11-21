import sys

from PyQt5.QtCore import QSize, QRect, pyqtSlot, QPropertyAnimation, QObject, QCoreApplication, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QPushButton, \
    QSizePolicy, QSpacerItem, QDialog, QFrame
#from Ui_config_dialog import Ui_configDialog as Form

#from DownloadListing import Listing
from Ui_joe_mainwindow import Ui_mainWin

import joe_sender

message = []
message.append("dir")
raw_list = joe_sender.sendmessage(message)
Listing = raw_list

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_mainWin()
ui.setupUi(window)



def end(self):
    QCoreApplication.instance().quit()


ui.quitButton.clicked.connect(lambda checked, i=1: end(ui))



########################
def show_config(self):
    dialog = QDialog()
    dialog.ui = Form()
    dialog.ui.setupUi(dialog)
    dialog.exec_()
    dialog.show()


ui.configButton.clicked.connect(lambda: show_config(ui))


###----------------- Start building the scroller ----------------###

# prep for filling that nasty scroller...
# delete the QGridLayout that's already there and attach a new one
ui.gridLayoutWidget.deleteLater()
ui.gLW2 = QWidget(ui.scrollAreaWidgetContents)
ui.itemGrid2 = QGridLayout(ui.gLW2)

counter = 0
max = len(Listing)

# determine and set the max height of the widget inside the scroller
maxHeight = (len(Listing) -1) * 65
ui.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 399, maxHeight))


# start adding rows, using code directly from Ui_joemainwindow.py
while counter < max:
    dlObject = Listing[counter]

    ui.labelbutton = QPushButton(ui.gLW2)
    ui.labelbutton.setMaximumSize(QSize(315, 50))
    ui.labelbutton.setMinimumHeight(50)
    #ui.labelbutton.setMinimumSize(QSize(315, 50))
    #ui.labelbutton.setGeometry(QRect(0,0,315,50))
    ui.labelbutton.setStyleSheet("QPushButton {background: white; border 1px solid black}\n"
"QPushButton.pushed {background: #a6a6a6}")
    ui.labelbutton.setObjectName(dlObject)
    ui.labelbutton.setText(dlObject)
    ui.labelbutton.setObjectName("labelbutton_%s" % counter)
    ui.itemGrid2.addWidget(ui.labelbutton, counter, 0, 1, 1)

    ui.trashbutton = QPushButton(ui.gLW2)
    sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(ui.trashbutton_0.sizePolicy().hasHeightForWidth())
    ui.trashbutton.setSizePolicy(sizePolicy)
    ui.trashbutton.setMinimumSize(QSize(50, 50))
    ui.trashbutton.setMaximumSize(QSize(50, 50))
    ui.trashbutton.setStyleSheet("QPushButton {background: white; border 1px solid black}\n"
"QPushButton.pushed {background: #a6a6a6}")
    ui.trashbutton.setText("")
    icon = QIcon()
    icon.addPixmap(QPixmap("bw-trash-clipart.gif"), QIcon.Normal, QIcon.Off)
    ui.trashbutton.setIcon(icon)
    ui.trashbutton.setIconSize(QSize(36, 36))
    ui.labelbutton.setObjectName("trashbutton_%s" % counter)
    ui.trashbutton.clicked.connect(lambda checked, i=counter: delete_row(i))
    ui.labelbutton.clicked.connect(lambda checked, i=counter: process_item(i))
    ui.itemGrid2.addWidget(ui.trashbutton, counter, 2, 1, 1)

    counter = counter + 1

# add a spacer at the bottom to push everything up
ui.spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
ui.itemGrid2.addItem(ui.spacerItem1, counter + 1, 0, 1, 1)
ui.scrollArea.setWidget(ui.scrollAreaWidgetContents)

###---------- End of scroller construction --------------###

@pyqtSlot()
def process_item(rownumber):
    QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
    message = []
    item_name = Listing[rownumber]
    message.append("rename")
    message.append(item_name)
    retval = joe_sender.sendmessage(message)
    print(retval)
    delete_row(rownumber)
    QApplication.setOverrideCursor(QCursor(Qt.ArrowCursor))


def anim_delete(self):
    animation = QPropertyAnimation(self, b'maximumSize')
    animation.setDuration(750)
    animation.setStartValue(QSize(315, 50))
    animation.setEndValue(QSize(0, 50))
    animation.start()

    self.animation = animation

@pyqtSlot()
def destroy(rownumber):
    qWTitle = ui.itemGrid2.itemAtPosition(rownumber, 0)
    qWTrash = ui.itemGrid2.itemAtPosition(rownumber, 2)

    # peel back another layer of abstraction
    widgetTitle = qWTitle.widget()
    widgetTrash = qWTrash.widget()

    ui.itemGrid2.removeWidget(widgetTitle)
    ui.itemGrid2.removeWidget(widgetTrash)

    # destroy! (later)
    widgetTitle.deleteLater()
    widgetTrash.deleteLater()


@pyqtSlot()
def delete_row(rownumber):

    ###----- Visual (delete from grid ------###

    qWTitle = ui.itemGrid2.itemAtPosition(rownumber,0)
    # peel back another layer of abstraction
    widgetTitle = qWTitle.widget()

    anim_delete(widgetTitle)

    QTimer.singleShot(750, lambda: destroy(rownumber))

    # shrink the underlying scroll panel so it stays proportional
    # (it's nothing more than a plain old widget)
    panel_rect = ui.scrollAreaWidgetContents.geometry()
    h = panel_rect.height()
    h = h - 60
    panel_rect.setHeight(h)
    ui.scrollAreaWidgetContents.setGeometry(panel_rect)

    ###-------- End visual work on scroller --------###

window.show()
sys.exit(app.exec_())