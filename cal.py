import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QCalendarWidget, QLabel
from PyQt5.QtCore import QRect
from Ui_calendar import Ui_Dialog as Form

from Ui_calendar_start import Ui_MainWindow

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor


app = QApplication(sys.argv)  # <—- QApp doesn’t change


class Echo(Protocol):
    def dataReceived(self, incoming):
        orig_incoming = incoming
        decoded = incoming.decode("utf-8").strip('\x00')
        print(decoded)
        #SendData(self, decoded)
        # if decoded == "dir":
        #     for fileobj in DownloadListing.Listing:
        #         SendData(self, fileobj.filename)
        #         SendData(self, "\r\n")


    def SendData(self, data):
        self.transport.write(data.encode('utf-8'))



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.calendarWidget = QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QRect(50, 60, 312, 173))
        self.calendarWidget.setObjectName("calendarWidget")
        self.OkButton = QPushButton(Dialog)
        self.OkButton.setGeometry(QRect(240, 240, 113, 32))
        self.OkButton.setObjectName("OkButton")
        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setGeometry(QRect(120, 240, 113, 32))
        self.cancelButton.setObjectName("cancelButton")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(30, 10, 331, 31))
        self.label.setObjectName("label")


    def show_config(self, data):
        Echo.SendData("dir")

        i = 1
        self.OkButton.clicked.connect(lambda checked, i=2: self.show_config(data))


if __name__ == "__main__":
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(8000, f)
    reactor.run()
    # app = QApplication(sys.argv)
    window = QDialog()  # <—— WidgetClass from UI
    window.show()
    sys.exit(app.exec_())