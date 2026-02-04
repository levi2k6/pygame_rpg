import pygame
from Initialization import gameloop 
from Gamestate import LoadedEntities
from System import SceneSystem

class InputSystem:

    def __init__(
        self,
        gameloop: gameloop.GameLoop | None = None, 
    ):
        self.gameloop = gameloop

    def detectInput(self, event):
        if(self.gameloop == None):
            raise ValueError("Health cannot be negative")

        if event.type == pygame.QUIT:
            self.gameloop.isRunning = False
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



            

