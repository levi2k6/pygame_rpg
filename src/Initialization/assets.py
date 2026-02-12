import pygame

data = {}

class Assets():
    def __init__(self):
        self.data = {}
        self.loadAssets()
        

    def loadAssets(self):
        asset =  {"name": "forsen", "sprite": pygame.image.load("./assets/forsen.jpeg").convert_alpha()}
        self.data[asset["name"]] = asset["sprite"]

