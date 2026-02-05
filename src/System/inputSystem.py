import pygame
from Initialization.gameloop import GameLoop 
from Gamestate import LoadedEntities
from System import SceneSystem

class InputSystem:

    def __init__(
        self,
    ):

    def detectInput(self, event, gameloop: GameLoop):
        if event.type == pygame.QUIT:
            gameloop.isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                print("f pressed")
                LoadedEntities.spawnPlayer()
            if event.key == pygame.K_g:
                print("g is pressed")
                if not SceneSystem.currentScene == "CombatScene":
                    SceneSystem.currentScene = "CombatScene"
                else:
                    SceneSystem.currentScene = "MainMenu"

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            print("d pressed")
            LoadedEntities.player.x += 10
        if keys[pygame.K_a]:
            print("a pressed")
            LoadedEntities.player.x -= 10



            

