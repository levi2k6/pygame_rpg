import pygame
from pygame import Vector2
import sys

from GameState.gameState import GameState
from Initialization.display import Display 
from Initialization.gameloop import GameLoop 
from Initialization.assets import Assets
from Scene.WorldScene.tileSystem import TileSystem
from Scene.sceneFactory import SceneFactory
from System.camera import Camera
from System.inputSystem import InputSystem
from System.renderSystem import RenderSystem
from System.sceneSystem import SceneSystem
from System.world import World
from input.playerInput import PlayerInput

pygame.init()

display: Display = Display( Vector2(800, 800), "pygameRpg")
assets: Assets = Assets()
gameState: GameState = GameState(assets)
camera: Camera = Camera(display)
world: World = World()
tileSystem: TileSystem = TileSystem(assets, camera)
renderSystem: RenderSystem = RenderSystem(display, gameState, camera, tileSystem)

sceneFactory: SceneFactory = SceneFactory(display, gameState, assets, tileSystem)
sceneSystem: SceneSystem = SceneSystem(renderSystem, sceneFactory)
playerInput: PlayerInput = PlayerInput(tileSystem)
inputSystem: InputSystem = InputSystem(gameState, sceneSystem, camera, playerInput)


gameloop: GameLoop = GameLoop(display, inputSystem, sceneSystem)

gameloop.startGameloop()

pygame.quit()
sys.exit()
