import socket
host = "localhost"
port = 8888

sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sok.bind((host,port))

print("Server is Start")
sok.listen(1)

client,addr = sok.accept()

print("Client Address :- ",addr)

msg = "Hello Client"

client.send(msg.encode())

sok.close()
