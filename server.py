# import socket module
from socket import *
import sys  # In order to terminate the program

serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)  # handle one connection at a time
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        connectionSocket.send('HTTP/1.0 200 OK\r\n'.encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        connectionSocket.send('HTTP/1.0 404 NOT FOUND\r\n'.encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send('<html><body><h1>404</body></html>'.encode())
        connectionSocket.close()
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data
