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

pygame.init()

assetsRegistry: AssetsRegistry = AssetsRegistry()
coreRegistry: CoreRegistry = CoreRegistry()

serializationRegistry: SerializationRegistry = SerializationRegistry(coreRegistry.player)
# print("teams: ", player.teams)

inputRegistry: InputRegistry = InputRegistry(coreRegistry.gameState, serializationRegistry.serializationPlayer)

worldRegistry: WorldRegistry = WorldRegistry(coreRegistry, assetsRegistry)

simulationRegistry: SimulationRegistry = SimulationRegistry(coreRegistry, assetsRegistry, worldRegistry) 

renderRegistry: RenderRegistry = RenderRegistry(coreRegistry, worldRegistry.world)

gameloop: GameLoop = GameLoop(coreRegistry, inputRegistry, renderRegistry)
gameloop.startGameloop()


pygame.quit()
sys.exit()
