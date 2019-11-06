import socket
tup=("localhost",5000)
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(tup)
msg,addr = s.recvfrom(1024)
try:
    s.settimeout(20)
    while msg:
        print("From Address: ",addr)
        print("Received : "+msg.decode())
        msg,addr = s.recvfrom(1024)
except socket.timeout:
    print("Time is over closing operation......")
s.close()
        
