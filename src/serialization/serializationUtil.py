import os
import sys

import platform
import struct


class SerializationUtil:

    def getSavePath(self):
        system = platform.system()

        if system == "Linux":
            base = os.path.expanduser("~/.local/share")
        elif sys.platform == "Windows":
            base = os.environ["APPDATA"]
        else:
            raise RuntimeError("Unsupported os")

        savePath = os.path.join(base, "pygame_rpg")
        return savePath 

    def getPlayerSavePath(self): 
        savePath = self.getSavePath()
        playerSavePath =os.path.join(savePath, "player_saves")
        return playerSavePath 


    def initSaveDirectories(self): 
        if not os.path.exists(self.getPlayerSavePath()):
            os.mkdir(self.getPlayerSavePath())
            print("player_saves is successfully initialize")



