from loadedAssets.assetsRegistry import AssetsRegistry
from init.coreRegistry import CoreRegistry 
from inputs.inputRegistry import InputRegistry
import pygame
import sys

from core.gameloop import GameLoop
from init.renderRegistry import RenderRegistry
from init.serializationRegistry import SerializationRegistry
from init.simulationRegistry import SimulationRegistry
from init.worldRegistry import WorldRegistry
from ui.uiRegistry import UIRegistry

pygame.init()

assetsRegistry: AssetsRegistry = AssetsRegistry()
coreRegistry: CoreRegistry = CoreRegistry()

serializationRegistry: SerializationRegistry = SerializationRegistry(coreRegistry.player)
# print("teams: ", player.teams)

inputRegistry: InputRegistry = InputRegistry(coreRegistry.gameState, serializationRegistry.serializationPlayer)

uiRegistry: UIRegistry = UIRegistry(coreRegistry.display, inputRegistry)

worldRegistry: WorldRegistry = WorldRegistry(coreRegistry, assetsRegistry)

simulationRegistry: SimulationRegistry = SimulationRegistry(coreRegistry, assetsRegistry, worldRegistry, inputRegistry, uiRegistry) 

renderRegistry: RenderRegistry = RenderRegistry(coreRegistry, worldRegistry, uiRegistry)

gameloop: GameLoop = GameLoop(coreRegistry, inputRegistry, uiRegistry, simulationRegistry, renderRegistry)

gameloop.startGameloop()


pygame.quit()
sys.exit()
