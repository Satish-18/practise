
#Creating a server using a socket module
import socket
host="localhost"
port=4000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen()
print("server listening on port",port)

c,addr=s.accept()

print("Connection from",str(addr))

c.send(b"hello how are you")
c.send("bye".encode())
c.close()


#Creating a clint
import socket
s=socket.socket()

s.connect(("localhost",4000))

msg=s.recv(1024)

while msg:
    print("Received",msg.decode)
    msg=s.recv(1024)

s.close()
