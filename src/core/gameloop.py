from typing import List
import pygame
from pygame import Event, Surface
from pygame_gui import UIManager
from Initialization.display import Display
from enums.enumScene import EnumScene
from core.gameState import GameState
from init import coreRegistry
from init.coreRegistry import CoreRegistry
from init.renderRegistry import RenderRegistry
from inputs.inputRegistry import InputRegistry

clock = pygame.time.Clock()

class GameLoop: 

    def __init__(
        self, 
        coreRegistry: CoreRegistry,
        inputRegistry: InputRegistry, 
        renderRegistry: RenderRegistry 
     ) -> None:
        self.display: Display = coreRegistry.display;
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.inputRegistry = inputRegistry
        self.gameState = coreRegistry.gameState
        self.uiManager = coreRegistry.uiManager
        self.rendererUi = renderRegistry.rendererUi


    def startGameloop(self):
        while self.isRunning:

            self.display.screen.fill((0,0,0))
            delta = self.clock.tick(60) / 1000.0

            events: List[Event] = pygame.event.get()

            self.simulate()
            self.rendererUi.renderUi(self.uiManager, events, self.display, delta)

            pygame.display.flip()


    def simulate(self):
        pass






