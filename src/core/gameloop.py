import pygame
from Initialization.display import Display
from enums.enumScene import EnumScene
from gameState.gameState import GameState
from init.renderRegistry import RenderRegistry
from inputs.inputRegistry import InputRegistry
from render.rendererBasic import RendererBasic
from render.rendererWorld import RendererWorld
from simulation.cameraSystem import CameraSystem
from simulation.simulateBasic import SimulateBasic

clock = pygame.time.Clock()

class GameLoop: 

    def __init__(
        self, 
        display: Display,
        gameState: GameState,
        inputRegistry: InputRegistry, 
        renderRegistry: RenderRegistry 
     ) -> None:
        self.display: Display = display;
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.inputRegistry = inputRegistry
        self.gameState = gameState

    def startGameloop(self):
        while self.isRunning:

            self.processEvent()
            self.simulate()
            self.renderScene()

            self.display.screen.fill((0,0,0))
            delta = self.clock.tick(60) / 1000.0

            pygame.display.flip()


    def processEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False

            print("currentScene: ", self.gameState.currentScene)
            
            if event.type == pygame.KEYDOWN:
                if self.gameState.currentScene == EnumScene.MENU: 
                    inputFunc = self.inputRegistry.menuInputs.get(event.key)
                    if inputFunc == None:
                        print("key does not exists")
                        return
                    inputFunc.func()

                elif self.gameState.currentScene == EnumScene.WORLD:
                    inputFunc = self.inputRegistry.worldInputs.get(event.key)
                    if inputFunc == None:
                        print("key does not exists")
                        return
                    inputFunc.func()

    def simulate(self):
        pass


    def renderScene(self):
        pass




