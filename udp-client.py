import socket 

client_socket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

client_socket.sendto("HELLO UDP Client".encode() , ("127.0.0.1" , 54321))

data , addr = client_socket.recvfrom(1024)

print("Server says : " , data.decode())

client_socket.close()