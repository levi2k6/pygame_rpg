from game.gameInit import GameInit
from game.gameExit import GameExit
from init.gameStateRegistry import StateRegistry 
from loadedAssets.assetsRegistry import AssetsRegistry
from init.coreRegistry import CoreRegistry 
from init.inputRegistry import InputRegistry
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
assetsRegistry: AssetsRegistry = AssetsRegistry()

coreRegistry: CoreRegistry = CoreRegistry()

stateRegistry: StateRegistry = StateRegistry()

serializationRegistry: SerializationRegistry = SerializationRegistry(stateRegistry.gameState.player)

inputRegistry: InputRegistry = InputRegistry(stateRegistry, serializationRegistry.serializationPlayer)

uiRegistry: UIRegistry = UIRegistry(stateRegistry.settingsState.display)

worldRegistry: WorldRegistry = WorldRegistry(stateRegistry, assetsRegistry)

simulationRegistry: SimulationRegistry = SimulationRegistry(stateRegistry, assetsRegistry, worldRegistry, uiRegistry, inputRegistry) 

renderRegistry: RenderRegistry = RenderRegistry(stateRegistry, worldRegistry, uiRegistry)


#game life cycle
# gameInit: GameInit = GameInit(simulationRegistry)
gameloop: GameLoop = GameLoop(coreRegistry, stateRegistry, inputRegistry, uiRegistry, simulationRegistry, renderRegistry)
gameExit: GameExit = GameExit()

#end
pygame.quit()
sys.exit()
