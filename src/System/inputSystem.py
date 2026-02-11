import pygame
from Initialization.gameloop import GameLoop 

class InputSystem:

    def __init__(
        self
    ):
        pass

    def detectInput(self, gameloop: GameLoop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop.isRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    print("f pressed")
                    gameloop.isRunning = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                print("d pressed")
                # LoadedEntities.player.x += 10
            if keys[pygame.K_a]:
                print("a pressed")
                # LoadedEntities.player.x -= 10



            

