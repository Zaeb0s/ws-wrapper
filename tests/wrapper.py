import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from wswrapper import *
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

addr = socket.gethostbyname(socket.gethostname()), 1234

print(addr)

server.bind(addr)
server.listen(10)

ws = Wrapper(server, is_client=False)


socket.socket.connec
# client.do_handshake_as_server()
# print(addr, ':', client.recv(1024))
# print(addr, ':', client.recv(1024))
client, addr = ws.accept()
print(addr, 'Connected')
while True:
    data = client.recv(1024)
    if data == b'':
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        print('Connection closed')
        client, addr = ws.accept()
        print(addr, 'Connected')
    else:
        print(addr, ':', data)
        client.send(data)

# client.do_handshake_as_server()
# client.sock.setblocking(True)
# print(client.sock.recv(200))
# print(client.sock.recv(200))
# print(client.sock.recv(200))