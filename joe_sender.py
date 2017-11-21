import socket
import struct
import pickle
import sys
import telnetlib


def sendmessage(incoming):

    HOST, PORT = "10.0.0.53", 9999
    data = incoming

    packed_data = pickle.dumps(data)

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(packed_data))

    # Receive data from the server and shut down

    def recv_msg(sock):
        # Read message length and unpack it into an integer
        raw_msglen = recvall(sock, 4)
        if not raw_msglen:
            return None
        msglen = struct.unpack('>I', raw_msglen)[0]
        # Read the message data
        return recvall(sock, msglen)

    def recvall(sock, n):
        # Helper function to recv n bytes or return None if EOF is hit
        data = b''
        while len(data) < n:
            packet = sock.recv(n - len(data))
            if not packet:
                return None
            data += packet
        return data

    returnmsg = recv_msg(sock)

    if returnmsg:
        message = pickle.loads(returnmsg)
        return message
    else:
        return None


