import socketserver
import struct
import DownloadListing
import pickle
import analyzetitle

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    message = ""

    def handle(self):
        message=""
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        query_data = pickle.loads(self.data)
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())
        if query_data[0] == "dir":
            message = []
            for fileobj in DownloadListing.Listing:
                fname = fileobj.filename
                message.append(fname)
            self.xmit_reponse(message)

        if query_data[0] == "rename":
            title = query_data[1]
            bundle = {}
            bundle = analyzetitle.sendquery("-rename", title)
            print("Bundle = ")
            print(bundle)
            self.xmit_reponse(bundle)

    def xmit_reponse(self, msg):
        message = pickle.dumps(msg)
        msg = struct.pack('>I', len(message)) + message
        self.request.sendall(msg)


if __name__ == "__main__":
    HOST, PORT = "10.0.0.53", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)


    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
