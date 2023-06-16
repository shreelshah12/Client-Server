from socket import *
import sys

# Assign port number
serverPort = 8080

# --- Step 1: Initialize the socket --- 

# Server creates TCP socket
# First paramater indicates that underlying network is using IPv4
# Second parameter indicates that that socket is of type SOCK_STREAM, which means it is TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Allow for the reuse of address
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Binds port number to server's socket
serverSocket.bind(('', serverPort))

#  Wait and listen for some client to knock on the welcoming door
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    # --- Step 2: Establish TCP connection ---
    # Server listens for TCP connection request from client
    connSocket, addr = serverSocket.accept()
    connSocket.settimeout(10)
    
    try: 
        # Step 3: Receive data from connSocket
        http_message = connSocket.recv(1024)
        print(http_message)
        # --- Step 4-6: Parse the message and read the file
        # File name is located after the first "/"
        filename = http_message.decode().partition("/")[2].split()[0]
        file = open(filename)
        file_message = file.read()
        # Step 7: Make a response
        # Create HTTP response message consisting of header line + requested file 
        response = "HTTP/1.0 200 OK\n\n" + file_message
        # Send response over TCP connection
        connSocket.send(response.encode())
        # Step 8: Close the connection
        connSocket.close()
    except IOError:
        response = "HTTP/1.0 404 Not Found\n\n File not found"
        connSocket.send(response.encode())
        connSocket.close()
    except KeyboardInterrupt:
        print("Closing server socket")
        if connSocket:
            connSocket.close()
        break
serverSocket.shutdown()
serverSocket.close()
sys.exit()
    

