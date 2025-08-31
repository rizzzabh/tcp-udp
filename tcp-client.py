import socket 

client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1" , 54321))

client_socket.send("Hello from client".encode())

reply = client_socket.recv(1024).decode()

print("Message from server : " , reply)

client_socket.close()