#!/usr/bin/env python

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import DownloadListing


class Echo(Protocol):
    def dataReceived(self, incoming):
        orig_incoming = incoming
        decoded = incoming.decode("utf-8").strip('\x00')
        SendData(self, decoded)
        if decoded == "dir":
            for fileobj in DownloadListing.Listing:
                SendData(self, fileobj.filename)
                SendData(self, "\r\n")


def SendData(self, data):
    self.transport.write(data.encode('utf-8'))


def main():
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(8000, f)
    reactor.run()


if __name__ == '__main__':
    main()
