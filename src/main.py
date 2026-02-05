import pygame
import sys

from Initialization.display import Display 
from Initialization.gameloop import GameLoop 
from Initialization.assets import Assets
from System.inputSystem import InputSystem

pygame.init()

display: Display = Display(800, 800, "pygameRpg")
assets: Assets = Assets()


inputSystem: InputSystem = InputSystem()
gameloop: GameLoop = GameLoop(display, inputSystem)

assets.loadAssets()
display.setColor((30, 30, 30))
gameloop.startGameloop()

pygame.quit()
sys.exit()
