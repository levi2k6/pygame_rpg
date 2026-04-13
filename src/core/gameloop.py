import pygame
from enums.enumScene import EnumScene
from init.animationRegistry import AnimationRegistry
from render import rendererScene
from state.settings.display import Display
from init.coreRegistry import CoreRegistry
from init.stateRegistry import StateRegistry
from init.renderRegistry import RenderRegistry
from init.simulationRegistry import SimulationRegistry
from init.inputRegistry import InputRegistry
from core.eventHandler import EventHandler
from ui.uiRegistry import UIRegistry

clock = pygame.time.Clock()

class GameLoop: 

    def __init__(
        self, 
        eventHandler: EventHandler,
        stateRegistry: StateRegistry,
        inputRegistry: InputRegistry, 
        uiRegistry: UIRegistry,
        simulationRegistry: SimulationRegistry, 
        animationRegistry: AnimationRegistry,
        renderRegistry: RenderRegistry,
     ) -> None:
        self.eventHandler = eventHandler
        self.display: Display = stateRegistry.settingsState.display;
        self.clock = pygame.time.Clock()
        self.inputRegistry = inputRegistry
        self.gameState = stateRegistry.gameState
        self.uiManager = uiRegistry.uiManager 
        self.simulationRegistry = simulationRegistry
        self.animationRegistry = animationRegistry
        self.rendererUi = renderRegistry.rendererUi
        self.rendererWorld = renderRegistry.rendererWorld
        self.rendererScene = renderRegistry.rendererScene

        self.startGameloop()


    def startGameloop(self):
        while self.gameState.isRunning:

            delta = self.clock.tick(60) / 1000.0

            events = pygame.event.get()
            
            self.eventHandler.processEvents(events)

            self.sceneHandler(delta)

            pygame.display.flip()
            self.display.screen.fill((0,0,0))


    def sceneHandler(self, delta):
        if self.gameState.currentScene == EnumScene.MENU: 
            self.rendererUi.renderUiMenu(delta)

        elif self.gameState.currentScene == EnumScene.WORLD:
            self.rendererWorld.renderWorld()
            self.rendererUi.renderUiWorld(delta)












