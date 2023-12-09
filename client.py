from LanPy import Client
import time

client = Client('192.168.5.149', 50504)
client.join()

while True:
    print(time.time())
    time.sleep(1)