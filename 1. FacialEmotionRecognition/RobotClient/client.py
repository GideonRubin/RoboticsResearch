# Based on https://pythontic.com/modules/socket/udp-client-server-example
import socket

def sendMessage(msg):
    msgFromClient = msg

    # Change these if necessary
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = ("127.0.0.1", 20001)
    bufferSize = 1024

    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    # Receive message from server
    # msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    # msg = (msgFromServer[0])

