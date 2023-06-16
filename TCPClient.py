from cgitb import html
from socket import *

# Assign port number
serverPort = 8080

# --- Step 1: Initialize a socket ---
# FIrst parameter indicates underlying network is IPv4
# Second parameter indicates that coket is of type SOCK_STREAM, meaning it is a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Step 2: Get an URI input
uri = input('Enter the URI: ')

# Step 3: Establish TCP connection to the server
clientSocket.connect((gethostbyname(""), serverPort))
# Step 4: Send HTTP request
clientSocket.send(uri.encode())
# Step 5: Receive data from client socket
message = clientSocket.recv(1024)
# Parse the HTTP response
print(message)

# Step 6: Close the connection
clientSocket.close()