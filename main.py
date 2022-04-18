from tracemalloc import start
from src.startup import * 
from src.config import *
from src.shell import *

# basic config
basicconfig = {
    "configfile" : "config.json",
    "asciilogos" : "asciilogos",
    "seweratman" : "man"
}


# call the server startup methods
def serverstart():
    ServerStarUp(basicconfig["asciilogos"])

# call the json argument parser
def jsonparse() -> dict:
    parser = JsonParser(basicconfig["configfile"])
    configfile = parser.loadfile()
    return configfile

# start sewerat shell
def startshell(config: dict):
    SeweratShell(config)



def main():
    serverstart()             # server startup 
    jconfig = jsonparse()     # read config file returns dict
    startshell(jconfig)       # pass the returned dict
    



if __name__ == "__main__":
    main()
