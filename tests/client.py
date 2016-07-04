import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from wswrapper import *
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.gethostbyname(socket.gethostname()), 1234

client = Wrapper(client, do_handshake_on_connect=True)

client.connect(addr)
print(client.state)

client.send(b'hello')