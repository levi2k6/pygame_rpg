import pygame
from core.display import Display
from init.coreRegistry import CoreRegistry
from init.gameStateRegistry import StateRegistry
from init.renderRegistry import RenderRegistry
from init.simulationRegistry import SimulationRegistry
from inputs.inputRegistry import InputRegistry
from ui.uiRegistry import UIRegistry

clock = pygame.time.Clock()

class GameLoop: 

    def __init__(
        self, 
        coreRegistry: CoreRegistry,
        stateRegistry: StateRegistry,
        inputRegistry: InputRegistry, 
        uiRegistry: UIRegistry,
        simulationRegistry: SimulationRegistry, 
        renderRegistry: RenderRegistry,
     ) -> None:
        self.display: Display = coreRegistry.display;
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.inputRegistry = inputRegistry
        self.gameState = stateRegistry.gameState
        self.uiManager = uiRegistry.uiManager 
        self.simulationRegistry = simulationRegistry
        self.rendererUi = renderRegistry.rendererUi

        self.startGameloop()


    def startGameloop(self):
        while self.isRunning:

            self.display.screen.fill((0,0,0))
            delta = self.clock.tick(60) / 1000.0

            events = pygame.event.get()
            
            self.isRunning = self.simulationRegistry.eventHandler.processEvent(events)

            self.simulate()
            self.rendererUi.renderUi(self.uiManager, self.display, delta)

            pygame.display.flip()

    def simulate(self):
        pass






