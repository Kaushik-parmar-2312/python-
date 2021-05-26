import socket
host=input("entert website name:")
ip=socket.gethostbyname(host)
print("website ip address:",ip)