import pygame
from Initialization import Display
from Entity.Marker import Marker 

teamLeft = [
    Marker().setPosition(Display.width * 0.25, Display.height * 0.37),
    Marker().setPosition(Display.width * 0.37, Display.height * 0.50),
    Marker().setPosition(Display.width * 0.25, Display.height * 0.63)
]

teamRight = [
    Marker().setPosition(Display.width * 0.75, Display.height * 0.37),
    Marker().setPosition(Display.width * 0.63, Display.height * 0.50),
    Marker().setPosition(Display.width * 0.75, Display.height * 0.63)
]
    
def drawScene():
    teamLeft[0].draw(Display.screen)  
    teamLeft[1].draw(Display.screen)
    teamLeft[2].draw(Display.screen)

    teamRight[0].draw(Display.screen)
    teamRight[1].draw(Display.screen)
    teamRight[2].draw(Display.screen)



    






