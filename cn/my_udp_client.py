import socket

tup = ("localhost",8888)

try:
    print("Client is online...!")
    sok = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sok.bind(tup)
    msg,addr = sok.recvfrom(1024)
    sok.settimeout(20)
    print("Client Address :- ",addr)
    print(msg.decode())
except Exception as e:
    print("Error",e)

finally:
    sok.close()
    print("Client is Offline...!")    
