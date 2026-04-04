from game.gameInit import GameInit
from game.gameExit import GameExit
from init.gameStateRegistry import StateRegistry 
from loadedAssets.assetsRegistry import AssetsRegistry
from init.coreRegistry import CoreRegistry 
from inputs.inputRegistry import InputRegistry
import pygame
import sys

from game.gameloop import GameLoop
from init.renderRegistry import RenderRegistry
from init.serializationRegistry import SerializationRegistry
from init.simulationRegistry import SimulationRegistry
from init.worldRegistry import WorldRegistry
from ui.uiRegistry import UIRegistry

pygame.init()

#inits
coreRegistry: CoreRegistry = CoreRegistry()

assetsRegistry: AssetsRegistry = AssetsRegistry()

stateRegistry: StateRegistry = StateRegistry()

serializationRegistry: SerializationRegistry = SerializationRegistry(coreRegistry.player)

inputRegistry: InputRegistry = InputRegistry(stateRegistry, serializationRegistry.serializationPlayer)

uiRegistry: UIRegistry = UIRegistry(coreRegistry.display, inputRegistry)

worldRegistry: WorldRegistry = WorldRegistry(coreRegistry, assetsRegistry)

simulationRegistry: SimulationRegistry = SimulationRegistry(coreRegistry, stateRegistry, assetsRegistry, worldRegistry, inputRegistry, uiRegistry) 

renderRegistry: RenderRegistry = RenderRegistry(coreRegistry, stateRegistry, worldRegistry, uiRegistry)

#game life cycle
gameInit: GameInit = GameInit(simulationRegistry)
gameloop: GameLoop = GameLoop(coreRegistry, stateRegistry, inputRegistry, uiRegistry, simulationRegistry, renderRegistry)
gameExit: GameExit = GameExit()

#end
pygame.quit()
sys.exit()
