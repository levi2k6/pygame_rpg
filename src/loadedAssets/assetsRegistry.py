import os
from typing import Dict
from pathlib import Path
import pygame 

class AssetsRegistry:

    def __init__(self):
       self.assetsPath = "../assets/"
       self.textures: Dict = self.initTextures()

    def initTextures(self):
        textures: Dict = {}
        for file in os.scandir(self.assetsPath):
            if file.is_file():
                if file.name.lower().endswith((".png", ".jpeg")): 
                    texture = pygame.image.load(self.assetsPath + "forsen.jpeg") 
                    name = Path(file.name).stem
                    textures[name] = texture
        return textures




    

