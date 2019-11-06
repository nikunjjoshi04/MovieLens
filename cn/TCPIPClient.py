import socket
host='localhost'
port = 5555
sok = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sok.connect((host,port))
msg = sok.recv(1024) #1024 size of buffer
while msg:
    print(msg.decode())
    msg = sok.recv(1024)
sok.close()
