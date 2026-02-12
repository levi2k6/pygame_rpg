import pygame
from Initialization.display import Display
from System.sceneSystem import SceneSystem
from System.inputSystem import InputSystem

clock = pygame.time.Clock()

class GameLoop: 

    def __init__(self, display: Display, inputSystem: InputSystem, sceneSystem: SceneSystem) -> None:
        self.display: Display = display;
        self.clock = pygame.time.Clock()
        self.isRunning = True;
        self.inputSystem = inputSystem
        self.sceneSystem = sceneSystem


    def startGameloop(self):
        while self.isRunning:
            self.display.screen.fill((0,0,0))
            delta = self.clock.tick(60) / 1000.0

            self.isRunning = self.inputSystem.detectInput(delta)
            self.sceneSystem.sceneChecker()
            
            pygame.display.flip()

