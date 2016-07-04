import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from wswrapper import *



# ------------- TESTING HANDSHAKE ----------------------------
client_key = Handshake.get_client_key()

handshake = Handshake().pack_client_handshake(client_key)

print('Client handshake')
print(handshake)

print('Server responce')
print(Handshake().pack_server_handshake(client_handshake=handshake))

# Handshake.check(client_key=client_key, server_key=server_key)

# ------------------------------------------------------------

