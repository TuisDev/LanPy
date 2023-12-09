import socket
import threading
import struct
import time
import select

class Server:
  def __init__ (self, address, port):
    self.address = address
    self.port = port
    self.thread_count = 0
    self.connections = 0
    self.locked = False

  def __handle_client(self, conn):
    try:
      while True:
        self.__recv()
        time.sleep(1)
        conn.getsockname() # Check to make sure connection exists
    except OSError:
      self.thread_count -= 1
      print("Connection Closed")

  def __accept(self):
    while True:
      conn, addr = self.sock.accept()
      if self.locked:
        break
      print(f"Connected to {addr}")
      if self.thread_count < self.connections or self.connections == 0:
        threading.Thread(
          target=self.__handle_client, args=(conn,), daemon=True
        ).start()
        self.thread_count += 1
        threading.Thread(
          target=self.__disconnect_handler, args=(conn,), daemon=True
        ).start()
      else:
        print("Server Full")

  def share(self, information):
      self.conn.sendall(information.encode())

  def host(self, connections=0, backlog=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((self.address, self.port))
    if backlog is not None:
      sock.listen(20)
    self.connections = connections
    self.sock = sock
    threading.Thread(target=self.__accept, daemon=True).start()

  def __disconnect_handler(self, conn):
      if select.select([conn], [], [])[0]:
        conn.close()
      
    
  def lock(self):
    self.locked = True

  def unlock(self):
    self.locked = False
    self.__accept()

  def __recv(self):
    pass

  def kick(self):
    pass

  def ban(self):
    pass

  def unban(self):
    pass

  def broadcast(self):
    pass

  def close(self):
    pass

  def link(self):
    pass

  def __link(self):
    pass

  def exit(self):
    self.sock.close()

  
class Client:
  def __init__(self, address, port):
    self.address = address
    self.port = port

  def join(self):
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((self.address, self.port))
      self.sock = sock

  def __thread_recv(self):
    while True:
      print(self.sock.recv(1024).decode())

  def __recv(self):
    print(type(self.sock))
    print(self.sock.recv(1024).decode())
       # threading.Thread(target=self.thread_recv, daemon=True)
  
  def exit(self):
    self.sock.close()

  def search(self):
    pass

  def __link(self):
    pass