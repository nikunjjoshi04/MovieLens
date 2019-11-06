import socket
host='localhost'
port = 5555
sok = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sok.connect((host,port))
msg = input("Enter Message for server: ")
while msg != "Exit":
    sok.send(msg.encode())
    msg = sok.recv(1024).decode()
    print("Server: ",msg)
    msg = input("Enter Message for server: ")
sok.close()
