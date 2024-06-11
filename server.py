import socket

hostServer=socket.gethostname()
port=8080
serverSocket=socket.socket()
# serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

serverSocket.bind((hostServer,port))

serverSocket.listen(5)

print("server is good to go...")
clientSocket,clientaddress=serverSocket.accept()
while True:
    # clientSocket,clientaddress=serverSocket.accept()
    request=clientSocket.recv(1500).decode()
    print(request)
    
    if request == 'GET':
        fin = open('index.html')
        content = fin.read()
        fin.close()
        response = 'HTTP/1.1 200 OK\n\n' + content
        clientSocket.sendall(response.encode())
        print("GET request done")

        clientSocket.close()   
