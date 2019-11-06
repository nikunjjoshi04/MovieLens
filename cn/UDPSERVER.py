import socket
import time
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    tup = ("localhost",5000)
    time.sleep(20)
    s.sendto(b"Hello Client ",tup)
    msg = "Bye"
    s.sendto(msg.encode(),tup)
except Exception as ex:
    print(ex)
s.close()
