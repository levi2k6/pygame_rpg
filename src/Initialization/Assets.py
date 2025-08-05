import pygame

data = {}

def loadAssets():
    asset =  {"name": "forsen", "sprite": pygame.image.load("../assets/forsenE.png").convert_alpha()}
    data[asset["name"]] = asset["sprite"]
