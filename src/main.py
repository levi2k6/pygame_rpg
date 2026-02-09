import pygame
from pygame import Vector2
import sys

from Initialization.display import Display 
from Initialization.gameloop import GameLoop 
from Initialization.assets import Assets
from System.inputSystem import InputSystem
from System.sceneSystem import SceneSystem

pygame.init()

display: Display = Display( Vector2(800, 800), "pygameRpg")
assets: Assets = Assets()


sceneSystem: SceneSystem = SceneSystem()


inputSystem: InputSystem = InputSystem()
gameloop: GameLoop = GameLoop(display, inputSystem)

assets.loadAssets()
display.setColor((30, 30, 30))
gameloop.startGameloop()

pygame.quit()
sys.exit()
