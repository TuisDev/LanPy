from LanPy import Client
import time

client = Client('127.0.0.1', 50504)
client.join()

while True:
    print(time.time())
    time.sleep(1)