import socket
host = 'localhost'
port = 5000
s= socket.socket()
s.bind((host,port))
s.listen(1)
client,addr = s.accept()
print("Client Address: ",addr)
filename = client.recv(1024)
filename = str(filename.decode())
print("File request from client is : ",filename)
try:
    path = "Z:\\New Folder\\Python\\Server\\"+filename
    file = open(path,'rb')
    content = file.read()
    client.send(content)
    print("File content send to client")
    file.close()
except FileNotFoundError:
    client.send(b"File not found")
client.close()
