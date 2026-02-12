import pygame

from GameState import gameState
from GameState.gameState import GameState

class InputSystem:

    def __init__(
        self,
        gameState: GameState
    ):
        self.gameState  = gameState
        pass

    def detectInput(self, delta) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if self.gameState.player == None: 
                        raise RuntimeError("Game state player  not found")
                    print("f pressed")
                    self.gameState.player.form.rotateSprite(180)                     

            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                print("d pressed")
                if self.gameState.player == None: 
                    raise RuntimeError("Game state player not found")
                self.gameState.player.form.position.x += 100 * delta
            if keys[pygame.K_a]:
                print("a pressed")
                # LoadedEntities.player.x -= 10
        return True



            

