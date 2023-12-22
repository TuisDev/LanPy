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
    self.variables = None
    self.__recieve = None

  def __handle_client(self, conn):
    try:
      threading.Thread(target=self.__recv, args=(conn,), daemon=True).start()
      while True:
        time.sleep(0.5)
        if self.variables is not None:
          self.variables = [str(i) for i in self.variables]
            
          message = ";;;\n;;;".join(self.variables)
          conn.sendall(message.encode())
        else:
          conn.getsockname() # Ensure socket is operational
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

  def share(self, variables, client=None):
      self.variables = variables

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

  def __recv(self, conn):
    while True:
      message = conn.recv(1024).decode()
      self.__recieve = tuple(message.split(";;;\n;;;"))

  def get_connections(self):
    return self.connections

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

  def recieve(self):
    if self.__recieve is not None:
      return self.__recieve

  
class Client:
  def __init__(self, address, port):
    self.address = address
    self.port = port
    self.__recieve = None
    self.thread_count = 0

  def join(self):
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((self.address, self.port))
      self.sock = sock
      threading.Thread(target=self.__recv, daemon=True).start()

  def __recv(self):
    while True:
      message = self.sock.recv(1024).decode()
      self.__recieve = tuple(message.split(";;;\n;;;"))

  def share(self, variables):
    if self.thread_count == 0:
      self.thread_count += 1
      threading.Thread(target=self.__share, args=(variables,), daemon=True).start()

  def __share(self, variables):
    while True:
      time.sleep(0.5)
      if variables is not None:
        variables = [str(i) for i in variables]
          
        message = ";;;\n;;;".join(variables)
        self.sock.sendall(message.encode())
    
  
  def exit(self):
    self.sock.close()

  def search(self):
    pass

  def __link(self):
    pass

  def recieve(self):
    if self.__recieve is not None:
      return self.__recieve