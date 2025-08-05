import pygame
from Initialization import Display
import System.InputSystem as InputSystem
from Gamestate import LoadedEntities 
from System import UISystem ,SceneSystem 

clock = pygame.time.Clock()
running = True 

def startGameloop():

    while running:
        timeDelta = clock.tick(60) / 1000.0

        Display.startDisplay()
        for event in pygame.event.get():
            UISystem.checkEventUI(event, timeDelta)
            InputSystem.detectInput(event)
        UISystem.drawUI(timeDelta)
        LoadedEntities.displayEntities()
        SceneSystem.sceneChecker()
        
        pygame.display.flip()

