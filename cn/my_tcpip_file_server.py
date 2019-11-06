import socket
host = "localhost"
port = 8888

try:
    print("Server Is Start...!")
    
    sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sok.bind((host,port))

    sok.listen(1)
    client,addr = sok.accept()

    print("Client Address :- ")

    filename = client.recv(1024)
    filename = str(filename.decode())

    print("File Name Is :- ",filename)

    try:
        path = "E:\\movilens\\venv\\cn\\"+filename
        file = open(path,'rb')
        content = file.read()
        client.send(content)
    except Exception as e:
        print("Error2",e)
    finally:
        file.close()
        print("File Is Close...!")
        
except Exception as e:
    print("Error1",e)
finally:
    sok.close()
    print("Server Is Close...!")
    
