import socket
host = "localhost"
port = 8888

try:
    print("\nServer Is OnLine...!")
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.bind((host,port))

    sok.listen(1)
    client,addr = sok.accept()
    print("Address of Client :- ",addr)

    content = client.recv(1024)
    print(content.decode())

    msg = input("Enter MSG :- ")
    client.send(msg.encode())
    
except Exception as e:
    print("\nError_1",e)
    
finally:
    sok.close()
    print("\nServer Is OffLine...!")
