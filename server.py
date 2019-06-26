import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("THE SERVER IS CREATED")
host="192.168.1.100"
port=1234
server_socket.bind((host,port))
print("the server socket is created at ip {} and port {}".format(host,port))
server_socket.listen()
print("the socket is ready to listen to client")
client_socket,client_addr=server_socket.accept()
print("the client is at ip {} and port {}".format(client_addr[0],client_addr[1]))
while True:
    smsg=input("server :")
    client_socket.send(smsg.encode())
    if smsg.strip().lower() == 'bye':
        print("connection is closed by server")
        client_socket.close()
        server_socket.close()
        break
    cmsg=client_socket.recv(1024)
    print("client: ",cmsg.decode())
    if cmsg.decode().strip().lower()=="bye":
        print("connection is closed by client")
        client_socket.close()
        server_socket.close()
        break

