import pygame

from GameState import gameState
from GameState.gameState import GameState
from System.sceneSystem import SceneSystem
from util.enums.SceneEnum import SceneEnum


class InputSystem:
    def __init__(
        self,
        gameState: GameState,
        sceneSystem: SceneSystem,
    ):
        self.gameState  = gameState
        self.sceneSystem = sceneSystem
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
                if event.key == pygame.K_g:
                    print("g pressed")
                    self.gameState.setIsPositionShow()
                if event.key == pygame.K_q:
                    print("q pressed")
                    self.sceneSystem.changeScene(SceneEnum.MAINMENU)
                if event.key == pygame.K_w:
                    print("e pressed")
                    self.sceneSystem.changeScene(SceneEnum.WORLD)
                if event.key == pygame.K_e:
                    print("w pressed")
                    self.sceneSystem.changeScene(SceneEnum.COMBAT)

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





            

