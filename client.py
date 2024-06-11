import socket
import time

clientSock=socket.socket()
machine=socket.gethostname()
port=8080
clientSock.connect((machine, port))   
message = input("Enter http method (GET,POST,PUT,HEAD): ")

    # Continue sending messages until the user types "bye"
while message.lower().strip() != "bye":
    # Send the message to the server
    clientSock.send(message.encode())
    
    # Receive the response from the server (buffer size is 1024 bytes)
    serverResponse = clientSock.recv(1024).decode()
    
    # Print the sent message and the server's response
    print("Sending message:", message)
    print("Server sent back:", serverResponse)
    
    # Wait for a short period before prompting for the next message
    time.sleep(5)
    reply=input("Do you want to continue (y/n): ")
    if reply=="y":
        message = input("Enter http method : ")
    else:
        message=input("enter [bye] to exit :")  