import socket
import json
import time

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12344
data = json.dumps({
    'user': 'abc',
    'title': 'something',
    'content': 'this is a, content',
    'clientTime': time.time()
})

# connect to the server on local computer
s.connect(('127.0.0.1', port))

s.sendall(bytes(data, encoding='utf-8'))

# receive data from the server and decoding to get the string.
print(json.loads(s.recv(1024).decode('utf-8')))
# close the connection
s.close()
