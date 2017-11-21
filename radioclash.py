from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
import DownloadListing
import pickle

class Chat(LineReceiver):

    def __init__(self, users):
        self.command = ""
        self.state = "GET"

    def lineReceived(self, line):
        print(line)
        self.sendReply(b'ACK')
        if line == b'dir':
            self.handleDirectory()
        else:
            self.sendReply(b'Welcome to the machine.')

    def sendReply(self, msg):
        pickled_msg = pickle.dumps(msg)
        self.sendLine(pickled_msg)

    def handleDirectory(self):
        msg = []
        for objitem in DownloadListing.Listing:
            msg.append(objitem.filename)
        self.sendReply(msg)















class ChatFactory(Factory):
    def __init__(self):
        self.command = ""  # no orders yet

    def buildProtocol(self, addr):
        return Chat(self.command)

reactor.listenTCP(9998, ChatFactory())
reactor.run()