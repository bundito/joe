import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont

from twisted.internet import reactor, protocol as p

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()



class EchoClient(p.Protocol):
    def connectionMade(self):
        self.transport.write(self.factory.data)

    def dataReceived(self, data):
        print('Received:', data)
        self.transport.loseConnection()

class EchoClientFactory(p.ClientFactory):
    protocol = EchoClient
    def __init__(self, data):
        self.data = data

reactor.connectTCP('localhost', 21421, EchoClientFactory('Hello, world'))
#reactor.run()


if __name__ == '__main__':
    class Echo(p.Protocol):
        def dataReceived(self, data):
            self.transport.write(data)


    class EchoFactory(p.Factory):
        def buildProtocol(self, addr):
            print('Connection by', addr)
            return Echo()


    reactor.listenTCP(21422, EchoFactory())
    #reactor.run()


    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())