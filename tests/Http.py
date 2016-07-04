import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from wswrapper import *

request = b'GET / HTTP/1.1\r\nSec-WebSocket-Protocol: chat\r\nUpgrade: websocket\r\nSec-WebSocket-Key: 53kYIhd1iQFbmnTznT6NdA==\r\nConnection: Upgrade\r\nSec-WebSocket-Version: 13\r\n\r\n'
response = b'HTTP/1.1 101 Switching Protocols\r\n' \
                        b'Upgrade: websocket\r\n' \
                        b'Connection: Upgrade\r\n' \
                        b'Sec-WebSocket-Accept: hej\r\n\r\n'

# request = b'd s s'
h = HttpRequest().unpack(request)
r = HttpResponse().unpack(response)
print(h)
print(h.body)
h.body = b'hej'
print(h.pack())

print()
print(r)
print(r.pack().decode('utf-8'))