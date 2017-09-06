from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
port = 8080
serverSocket.bind(('', port))
serverSocket.listen(1)
while 201312845:
    print("kim il sik, ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read(1024)
        print(outputdata)
        #send on http header line into socket
        connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\
                                    Content-Type: text/html\r\n\r\n".encode()))
        connectionSocket.sendall(outputdata.encode())
        connectionSocket.close()
    except IOError:
        #send response message for file not found
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n".encode()))
        connectionSocket.close() # close client socket
        break
serverSocket.close()