from LanPy import Client
import time

client = Client('127.0.0.1', 50504)
client.join()

var1, var2 = 2, 3
var3, var4 = 5, 7
while True:
    client.share((var3, var4))
    # if client.recieve() is not None:
    #     var1, var2 = client.recieve()
    #     print(var1)
    #     print(var2)