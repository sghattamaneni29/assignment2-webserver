# import socket module
import socket
# import builtins
from socket import *
from builtins import ConnectionResetError
from builtins import BrokenPipeError
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(('', port))
    serverSocket.listen(3)

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024)
            print('message: \n', message)
            filename = message.split()[1]
            f = open(filename[1:])
            fileData = f.read()
            print('output from file:', fileData)
            connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

            # Send the content of the requested file to the client
            for i in range(0, len(fileData)):
                connectionSocket.send(fileData[i].encode('utf-8'))

            connectionSocket.send('\r\n'.encode('utf-8'))
            connectionSocket.close()
        except IOError:
            # Send HTTP response message for file not found
            connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
            connectionSocket.send('<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'.encode())
            # Close the client connection socket
            connectionSocket.close()

    serverSocket.close()
    sys.exit()


if __name__ == "__main__":
    # use this space to debug and verify that the program works
    webServer(13331)
