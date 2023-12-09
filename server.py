from LanPy import Server
import time

server = Server('192.168.5.149', 50504)
server.host(0, 20)

while True:
    print(time.time())
    time.sleep(1)

    
