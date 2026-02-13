import pygame
from pygame import Vector2
import sys

from GameState.gameState import GameState
from Initialization.display import Display 
from Initialization.gameloop import GameLoop 
from Initialization.assets import Assets
from Scene.sceneFactory import SceneFactory
from System.inputSystem import InputSystem
from System.renderSystem import RenderSystem
from System.sceneSystem import SceneSystem

pygame.init()

display: Display = Display( Vector2(800, 800), "pygameRpg")
assets: Assets = Assets()
gameState: GameState = GameState(assets)
renderSystem: RenderSystem = RenderSystem(display, gameState)

sceneFactory: SceneFactory = SceneFactory(display, gameState, assets)
sceneSystem: SceneSystem = SceneSystem(renderSystem, sceneFactory)
inputSystem: InputSystem = InputSystem(gameState, sceneSystem)

gameloop: GameLoop = GameLoop(display, inputSystem, sceneSystem)

gameloop.startGameloop()

pygame.quit()
sys.exit()
