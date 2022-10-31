import socket
import csv
import json
import time

port = 12344
file = 'myModel.csv'
id = -1

with open(file, 'r', newline='') as f:
    reader = csv.reader(f)
    last = ''

    for line in reader:
        last = line

    if len(last) > 1:
        id = int(last[0])

    f.close()


def server(port: int, initialMessage: str, writter: csv.DictWriter) -> socket.socket:
    global id
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(initialMessage)

    s.bind(('127.0.0.1', port))
    print('socket binded to %s' % (port))

    s.listen(0)
    cId = id + 5

    while cId > id :

        c, addr = s.accept()
        
        msg: dict = json.loads(c.recv(256).decode())
        
        id += 1
        msg['id'] = id
        msg['serverTime'] = time.strftime("%D|%H:%M:%S")
        
        msg['resTime'] = round(time.time() - msg['clientTime'], 5)
        writter.writerow(msg)

        if(id == cId):
            msg['action'] = 'disconnect'

        c.sendall(bytes(json.dumps(msg), encoding='utf-8'))
        c.close()
        print(id)

    return s


writter = csv.DictWriter(
    open(file, 'a', newline=''), 
    fieldnames=['id', 'user', 'title', 'content', 'clientTime', 'serverTime', 'resTime'])
if(id == -1):
    writter.writeheader()
    id = 0

server(port, "server created", writter).close()
