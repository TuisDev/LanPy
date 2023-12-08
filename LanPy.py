import socket
import threading
import struct
import time

def host(address, port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM):
    s.connect((address, port))
  
