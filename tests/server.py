import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from wswrapper import *
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server = Wrapper(server)
addr = socket.gethostbyname(socket.gethostname()), 1234


server.bind(addr)
server.listen(10)

client, addr = server.accept()
print(addr, 'Connected')
while True:
    try:
        data = client.recv(1024)
    except WSError as err:
        print('Error', err)
        break

    if data == b'':
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        print('Connection closed')
        client, addr = server.accept()
        print(addr, 'Connected')
    else:
        print(addr, ':', data)
        client.send(data)
