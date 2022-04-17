import socket, ssl
import socketserver
from threading import Thread

pem_file = "certs/privkey.pem"
cert_file = "certs/cert.crt"

"""
can be replaced by and encryption algorithm
but be sure that the function signature still the same
this function returns the encryted string
"""
def encryption(data: str, key: str) -> str:
    maxindex = len(key) - 1
    keyindex = 0
    cipher = ""
    for byte in data:
        cipher += chr(ord(byte) ^ ord(data[keyindex]))
        if keyindex >= maxindex:
            keyindex = 0
            continue
        keyindex += 1
    return cipher


""" class Server(Thread):
    def __init__(self, host: str, port: int):
        Thread.__init__(self) 
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = port
             
    def bind(self):
      self.sock.bind((self.host, self.port))      
    
    def listen(self):
      
      self.bind()
      
      self.sock.listen(1) # stdout?
      client, addr = self.sock.accept()
      print(addr)
      while True:
        data = client.recv(1024)
 """
 
class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), 'utf-8')
        print(f"someone sent: {data}")
        response = bytes(f"to {data} I say: deez nuts")
        self.request.sendall(response)
