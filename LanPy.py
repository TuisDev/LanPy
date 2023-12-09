import socket
import threading
import struct
import time

class Server:
  def __init__ (self, address, port):
    self.address = address
    self.port = port

  def thread_host(self, sock: socket):
    conn, addr = sock.accept()
    self.conn = conn
    print(f"Connected to {addr}")

  def share(self, information):
      self.conn.sendall(information.encode())

  def host(self, backlog=None):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.bind((self.address, self.port))
      if backlog is not None:
        sock.listen(20)
      conn, addr = sock.accept()
      self.conn = conn
      print(f"Connected to {addr}")
      # threading.Thread(target=self.thread_host, args=(sock,), daemon=True).start()

class Client:
  def __init__(self, address, port):
    self.address = address
    self.port = port

  def join(self):
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((self.address, self.port))
      self.sock = sock

  def thread_recv(self):
    while True:
      print(self.sock.recv(1024).decode())

  def recv(self):
    print(type(self.sock))
    print(self.sock.recv(1024).decode())
       # threading.Thread(target=self.thread_recv, daemon=True)
  
  def close(self):
    self.sock.close()


