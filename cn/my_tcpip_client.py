import socket
host = "localhost"
port = 8888

sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sok.connect((host,port))

msg = sok.recv(1024)

print(msg.decode())
print("Close")

sok.close()
