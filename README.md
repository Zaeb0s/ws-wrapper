# Setup
```sh
pip install wswrapper
```

# Normal Use
I have tried to make it so that the wrapped socket works almost idential to a normal python socket

```python
from wswrapper import Wrapper
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wrapped_sock = Wrapper(sock)
# wrapped_sock can now be used as a normal python socket
```

# Advanced Use
## Adding http headers
If you want to add more http headers to the handshake request/response set handshake_headers to a dict containing all additional header keys and values. The following will add a Host header field to the handshake request/response.
```python
from wswrapper import Wrapper
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wrapped_sock = Wrapper(sock, do_handshake_on_connect=False)
wrapped_sock.handshake_headers = {b'Host': b'localhost'}
```
## Checking Additional Information About Current Frame
Information about the current frame can be checked after receiving a part of or the whole payload of a frame. This can be used to check if the payload opcode was that of RFC6455 binary or text.
```python
print('Fin:', wrapped_sock.current_frame.fin)
print('Opcode:', wrapped_sock.current_frame.opcode)
print('Payload:', wrapped_sock.current_frame.payload)
```
