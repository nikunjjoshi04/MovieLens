import socket
host = 'localhost'
port=5000
s = socket.socket()
s.connect((host,port))
filename = input("Enter filename:  ")
s.send(filename.encode())
content = s.recv(1024)
print(content.decode())
s.close()
