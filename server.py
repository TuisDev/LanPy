from LanPy import Server
import time

server = Server('', 50504)
server.host(0, 20)

start_time = time.time()

var1 = [15, "4", False]
var2 = True
while True:
    # server.share((var1, var2))
    if server.recieve() is not None:
        var3, var4= server.recieve()
        print(var3)
        print(var4)
    
