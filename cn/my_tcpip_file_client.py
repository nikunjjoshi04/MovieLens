import socket
host = "localhost"
port = 8888

try:
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.connect((host,port))

    filename = input("Enter file name :- ")
    sok.send(filename.encode())
    content = sok.recv(1024)
    print(content.decode())
except Exception as e:
    print("Error",e)
finally:
    sok.close()
    print("Client Close...!")

