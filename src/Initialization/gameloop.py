import pygame
from Initialization.display import Display
import System.inputSystem as InputSystem
from Gamestate import LoadedEntities 
from System import UISystem ,SceneSystem 

clock = pygame.time.Clock()

class GameLoop: 

    def __init__(self, display: Display, inputSystem: InputSystem) -> None:
        self.display: Display = display;
        self.clock = pygame.time.Clock()
        self.isRunning = True;
        pass


    def startGameloop(self):
        while self.isRunning:
            timeDelta = self.clock.tick(60) / 1000.0

            self.display.startDisplay()
            for event in pygame.event.get():
                # UISystem.checkEventUI(event, timeDelta)
                InputSystem.detectInput(event)
            # UISystem.drawUI(timeDelta)
            LoadedEntities.displayEntities()
            SceneSystem.sceneChecker()
            
            pygame.display.flip()

