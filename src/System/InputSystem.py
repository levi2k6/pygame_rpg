import pygame
from Initialization import Gameloop 
from Gamestate import LoadedEntities
from System import SceneSystem


def detectInput(event):
    if event.type == pygame.QUIT:
        Gameloop.running = False
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



        

