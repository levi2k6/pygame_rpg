import pygame

from GameState import gameState
from GameState.gameState import GameState
from System.camera import Camera
from System.sceneSystem import SceneSystem
from input import playerInput
from input.playerInput import PlayerInput
from util.enums.SceneEnum import SceneEnum


class InputSystem:
    def __init__(
        self,
        gameState: GameState,
        sceneSystem: SceneSystem,
        camera: Camera,
        playerInput: PlayerInput 
    ):
        self.gameState  = gameState
        self.sceneSystem = sceneSystem
        self.camera = camera
        self.playerInput = playerInput
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
                if event.key == pygame.K_1:
                    self.gameState.setIsPositionShow()
                if event.key == pygame.K_2:
                    self.sceneSystem.changeScene(SceneEnum.MAINMENU)
                if event.key == pygame.K_3:
                    self.sceneSystem.changeScene(SceneEnum.WORLD)
                if event.key == pygame.K_4:
                    self.sceneSystem.changeScene(SceneEnum.COMBAT)
                if event.key == pygame.K_a:
                    self.playerInput.moveLeft()
                if event.key == pygame.K_d:
                    self.playerInput.moveRight()
                if event.key == pygame.K_w:
                    self.playerInput.moveUp()
                if event.key == pygame.K_s:
                    self.playerInput.moveDown()




            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                print("d pressed")
                if self.gameState.player == None: 
                    raise RuntimeError("Game state player not found")
                self.gameState.player.form.position.x += 100 * delta
            if keys[pygame.K_a]:
                print("a pressed")
                # LoadedEntities.player.x -= 10
            if keys[pygame.K_RIGHT]:
                print("going right")
                self.camera.position.x += 40 
            if keys[pygame.K_LEFT]:
                print("going left")
                self.camera.position.x -= 40
        return True

