from LanPy import Server

server = Server('', 50504)
server.host(20)
while True:
    server.share(input("?: "))