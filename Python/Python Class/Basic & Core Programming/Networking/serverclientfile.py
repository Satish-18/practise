'''
#making server file
import socket
host="localhost"
port=6767

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

print("server listening on port",port)
s.listen(1)

c,addr=s.accept()

filename=c.recv(1024)

try:
    f=open(filename,"rb")
    content=f.read()
    c.send(content)
    f.close()
except filenotfounderror:
    c.send(b"file does not found")
c.close()
'''
#Making clint file
import socket
s=socket.socket()

s.connect(("localhost",6767))
filename=("Input enter the file name:")
s.send(filename.encode())
content=s.recv(1024)
print(content.decode())
s.close()
