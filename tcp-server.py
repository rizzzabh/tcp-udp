import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1" , 54321))

server_socket.listen()

print ("SERVER is listening on port : 12345 " )

conn , addr = server_socket.accept()

print (f"connected with {addr}")

data = conn.recv(1024).decode()

print("Client says : ", data)

conn.send("Hello from server".encode())


conn.close()

server_socket.close()