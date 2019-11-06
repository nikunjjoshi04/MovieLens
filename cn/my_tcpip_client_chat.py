import socket
host = "localhost"
port = 8888

try:
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.connect((host,port))

    print("Client IS OnLine...!\n")

    msg = input("Enter MSG :- ")
    sok.send(msg.encode())

    content = sok.recv(1024)
    print(content.decode(),"\n")
except Exception as e:
    print("Error",e)
finally:
    sok.close()
    print("Client Is OffLine...!")
    
