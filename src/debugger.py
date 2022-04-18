
from colorama import Fore, Style
from sys import stderr, stdout  
import sys
import os 

# this class is used for debugging/logging

class Debug:

    def __init__(self):
        self.reset = Style.RESET_ALL
        self.green = Fore.GREEN
        self.error = Fore.RED
        
    # write message to stderr
    def pstderr(self, msg: str, type: bool) -> None:
        # print error
        if type:    
            stderr.write(f"{self.error}[Error]{self.reset} {msg}\n")
            stderr.flush()
        # print warning
        else:
            stderr.write(f"{self.error}[Warning]{self.reset} {msg}\n")
            stderr.flush()
    
    # print green colored message to stdout
    def pstdout(self, msg: str):
        stdout.write(f"{self.green}[info]{self.reset}{msg}\n")
        stdout.flush()


    # clear the terminal 
    def clear(self):
        os.system("clear")



