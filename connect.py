import ssl, socket

HOST, PORT = "127.0.0.1", 23600

def main():
  sock = socket.socket(socket.AF_INET)
  sock.settimeout(10)
  
  ctx = ssl.create_default_context()
  ctx.verify_mode = ssl.CERT_OPTIONAL

  ssl_sock = ctx.wrap_socket(sock, server_hostname="127.0.0.1")  
  
  
  ssl_sock.connect((HOST, PORT))
  # ssl_sock.read(1024, data)
  
  while True:
    pass

if __name__ == "__main__":
  main()
