import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
host = '127.0.0.1'  # Localhost
port = 65432        # Arbitrary non-privileged port
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(1)
print(f"Server listening on {host}:{port}")

while True:
    # Accept a new connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive data from the client
    data = conn.recv(1024)  # Buffer size is 1024 bytes
    if not data:
        break
    print(f"Received: {data.decode()}")

    # Send a response back to the client
    conn.sendall(b"Hello, Client!")

    # Close the connection
    conn.close()