import socket
host = "localhost"
port =5555
sok = socket.socket()#also valid instead of following statement
#sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sok.bind((host,port))
print("server start")
sok.listen(1)
client,addr = sok.accept()

print("client address: ", addr)
msg = "Hello client how are you?"
client.send(msg.encode())
client.send(b'Bye')
client.close()
print("Close")
