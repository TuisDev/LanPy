from LanPy import Client

client = Client('127.0.0.1', 50504)
client.join()
while True:
    print(type(client.sock))
    print(client.sock.recv(1024).decode())