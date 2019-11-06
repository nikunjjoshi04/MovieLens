import socket
import time

tup = ("localhost",8888)

try:
    print("Server is Online...!")
    sok = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    time.sleep(20)

    msg = "hi client"
    sok.sendto(msg.encode(),tup)

except Exception as e:
    print("Error",e)

finally:
    sok.close()
    print("Server is offline...!")
