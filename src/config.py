from src.debugger import Debug
import json
import os 


class JsonParser(Debug):

    def __init__(self, configpath):
        super().__init__()
        self.path = configpath
        self.loadfile()

    # read config file 
    def loadfile(self) -> dict:
        if os.path.exists(self.path): 
            with open(self.path, "r") as f:
                file = json.loads(f.read())
                return file 
        # print error 
        self.pstderr("Configfile not found!!!", 0) 
        exit(-1)
