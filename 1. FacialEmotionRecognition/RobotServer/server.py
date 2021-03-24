# Based on https://pythontic.com/modules/socket/udp-client-server-example

import socket
import NaoChat

# Change these if necessary
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("Robo server up and listening")

# Listen for incoming datagrams
while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    print(message.decode())

    #Sends data to Nao in Choregraphe
    NaoChat.sayAndSend(message.decode())
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)