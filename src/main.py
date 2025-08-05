import pygame
import sys

from Initialization import Display, Gameloop, Assets

pygame.init()

Assets.loadAssets()
Display.startDisplay()
Gameloop.startGameloop()

pygame.quit()
sys.exit()
