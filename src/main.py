from inputs import inputMenu
from inputs.inputRegistry import InputRegistry
import pygame
from pygame import Vector2
import sys

# from gameState.gameState import GameState
from enums.enumScene import EnumScene
from gameState.gameState import GameState
from Initialization.display import Display 
from core.gameloop import GameLoop
from Initialization.assets import Assets
from init.renderRegistry import RenderRegistry
from init.serializationRegistry import SerializationRegistry
from init.simulationRegistry import SimulationRegistry
from init.worldRegistry import WorldRegistry
from render.camera import Camera
from gameState.player import Player

pygame.init()

display: Display = Display( Vector2(800, 800), "pygameRpg")
assets: Assets = Assets()
gameState: GameState = GameState(assets, EnumScene.MENU)
camera: Camera = Camera(display)
player: Player = Player()

serializationRegistry: SerializationRegistry = SerializationRegistry(player)
print("teams: ", player.teams)

inputRegistry: InputRegistry = InputRegistry(gameState, serializationRegistry.serializationPlayer)

worldRegistry: WorldRegistry = WorldRegistry(assets, display)

simulationRegistry: SimulationRegistry = SimulationRegistry(
    display, 
    gameState, 
    assets,
    worldRegistry.world,
    camera,
    worldRegistry.world.traveler,
    player
) 

renderRegistry: RenderRegistry = RenderRegistry(gameState, display, worldRegistry.world, camera)

# tileSystem: TileSystem = TileSystem(assets, camera)
# # renderSystem: RenderSystem = RenderSystem(display, gameState, camera, tileSystem)
# rendererBasic: RendererBasic = RendererBasic(gameState, display, camera, tileSystem)
# rendererEntity: RendererEntity = RendererEntity()
# rendererScene: RendererScene = RendererScene(gameState, display, rendererBasic, world, camera)
#
# sceneFactory: SceneFactory = SceneFactory(display, gameState, assets, tileSystem)
# sceneSystem: SceneSystem = SceneSystem(sceneFactory, rendererScene)
# playerInput: PlayerInput = PlayerInput(tileSystem)
# inputSystem: InputSystem = InputSystem(gameState, sceneSystem, camera, playerInput)

gameloop: GameLoop = GameLoop(display, gameState, inputRegistry, renderRegistry)
gameloop.startGameloop()


pygame.quit()
sys.exit()
