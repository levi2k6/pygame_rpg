from core.gameStart import GameStart
from core.gameExit import GameExit
from init.stateRegistry import StateRegistry 
from loadedAssets.assetsRegistry import AssetsRegistry
from init.coreRegistry import CoreRegistry 
from init.inputRegistry import InputRegistry
import pygame
import sys

from core.gameloop import GameLoop
from init.renderRegistry import RenderRegistry
from init.serializationRegistry import SerializationRegistry
from init.simulationRegistry import SimulationRegistry
from init.worldRegistry import WorldRegistry
from core.eventHandler import EventHandler
from ui.uiRegistry import UIRegistry

pygame.init()

#inits
assetsRegistry: AssetsRegistry = AssetsRegistry()

stateRegistry: StateRegistry = StateRegistry()

serializationRegistry: SerializationRegistry = SerializationRegistry(stateRegistry.gameState.player)

uiRegistry: UIRegistry = UIRegistry(stateRegistry.settingsState.display)

worldRegistry: WorldRegistry = WorldRegistry(stateRegistry, assetsRegistry)

simulationRegistry: SimulationRegistry = SimulationRegistry(stateRegistry, assetsRegistry, worldRegistry, uiRegistry) 

renderRegistry: RenderRegistry = RenderRegistry(stateRegistry, worldRegistry, uiRegistry)

inputRegistry: InputRegistry = InputRegistry(stateRegistry, serializationRegistry.serializationPlayer, simulationRegistry)


eventHandler: EventHandler = EventHandler(stateRegistry, uiRegistry, inputRegistry)
#game life cycle
gameInit: GameStart = GameStart(simulationRegistry)
gameloop: GameLoop = GameLoop(eventHandler, stateRegistry, inputRegistry, uiRegistry, simulationRegistry, renderRegistry)
gameExit: GameExit = GameExit()

#end
pygame.quit()
sys.exit()
