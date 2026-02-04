import pygame

data = {}

class Assets():
    def __init__(self):
        self.data = {}

    def loadAssets(self):
        asset =  {"name": "forsen", "sprite": pygame.image.load("./assets/forsen.jpeg").convert_alpha()}
        data[asset["name"]] = asset["sprite"]

