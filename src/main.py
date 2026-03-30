from assets.assetsRegistry import AssetsRegistry
from init.coreRegistry import CoreRegistry 
from inputs import inputMenu
from inputs.inputRegistry import InputRegistry
import pygame
from pygame import Vector2
import sys

# from core.gameState import GameState
from Initialization.display import Display 
from core.gameloop import GameLoop
from Initialization.assets import Assets
from init.renderRegistry import RenderRegistry
from init.serializationRegistry import SerializationRegistry
from init.simulationRegistry import SimulationRegistry
from init.worldRegistry import WorldRegistry

pygame.init()

display: Display = Display((800, 800), "pygameRpg")
assets: Assets = Assets()

assetsRegistry: AssetsRegistry = AssetsRegistry()
coreRegistry: CoreRegistry = CoreRegistry()

serializationRegistry: SerializationRegistry = SerializationRegistry(coreRegistry.player)
# print("teams: ", player.teams)

inputRegistry: InputRegistry = InputRegistry(coreRegistry.gameState, serializationRegistry.serializationPlayer)

worldRegistry: WorldRegistry = WorldRegistry(assetsRegistry, display)

simulationRegistry: SimulationRegistry = SimulationRegistry(coreRegistry, assetsRegistry, worldRegistry) 

renderRegistry: RenderRegistry = RenderRegistry(coreRegistry, worldRegistry.world)

gameloop: GameLoop = GameLoop(coreRegistry, inputRegistry, renderRegistry)
gameloop.startGameloop()


pygame.quit()
sys.exit()
