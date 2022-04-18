from src import debugger
from colorama import Fore, Style
import secrets
import time 
import os 


class ServerStarUp(debugger.Debug):

    def __init__(self, path):
        super().__init__() # call the base class constuctor
        self.path = path 
        self.startup()

    # startup function
    def startup(self):
        self.checkroot()
        self.clear()
        self.asciilogo()

    # check for root permissions
    def checkroot(self):
        if os.getuid() != 0:
            self.pstderr("Please run the script as root!!!", 0)
            exit(-1)

    # print a random asciilogo
    def asciilogo(self):
        # check if path exists
        if not os.path.exists(self.path):
            self.pstderr("Logopath not found!!!", 0)
            exit(-1)
        # choose random logofile
        logofiles = os.listdir(self.path)
        # format the logopath
        logopath = f"{self.path}/{secrets.choice(logofiles)}" 
        # read random logo file and print it colored
        with open(logopath, "r") as asciilogo:
            # format the logo 
            logo = f"{Fore.GREEN}{asciilogo.read()}{Style.RESET_ALL}"
             # print the formatted logo to the screen 
            print(logo)
        # timeout for nice popping shell
        time.sleep(1)

    