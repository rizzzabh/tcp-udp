import socket 


server_socket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

server_socket.bind(("127.0.0.1" , 54321))

print("UDP server is running...")

data , addr = server_socket.recvfrom(1024)

print ("Recieved from client: " , data.decode())

server_socket.sendto("Hello from UDP server".encode() , addr)


server_socket.close() 