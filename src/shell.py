from getpass import getuser
from src.debugger import * 
from src.startup import *
import os 


class SeweratShell(Debug):
    
    def __init__(self, config: dict):
        # call the base class constructors
        super(Debug, self).__init__() 

        self.configfile = config 

        # get some systeminformation 
        self.user = getuser()
        self.cwd = os.getcwd()

        self.readshell() # popping shell

    # open the serweratc2 manuals
    def seweratman(self):
        if os.path.exists(self.configfile["seweratman"]):
            with open(self.configfile["seweratman"] + "/help.man", "r") as manfile:
                print(manfile.read())
        
    # read shell input 
    def readshell(self):
        while True:
            # read command from stdin
            command = input("Sewerat:> ").lower()
            # check command 
            if command == "exit" or command == "quit":
                exit(0)
            
            # list all commands 
            elif command == "help" or command == "list":
                self.seweratman()
                continue

            # clear terminal 
            elif command == "clear" or command == "cls":
                self.clear()
                continue 
                



