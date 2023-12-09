from LanPy import Server
import time

server = Server('', 50504)
server.host(1, 20)

while True:
    print(time.time())
    time.sleep(1)

    
