
from gameState.gameState import GameState
from Initialization.assets import Assets
from Initialization.display import Display
from Scene.WorldScene.traveler import Traveler
from render.camera import Camera
from simulation.cameraSystem import CameraSystem
from simulation.combatSystem import CombatSystem
from simulation.spawnSystem import SpawnSystem
from simulation.tilesSystem import TileSystem
from gameState.player import Player
from world.world import World


class SimulationRegistry: 

    def __init__(self, display: Display, gameState: GameState, assets: Assets, world: World, camera: Camera, traveler: Traveler, player: Player):
        self.cameraSystem: CameraSystem = self.initCameraSystem(camera, traveler)
        self.tilesSystem: TileSystem = self.initTileSystem(world, assets)
        self.spawnSystem: SpawnSystem = self.initSpawnSystem(assets)
        self.combatSystem: CombatSystem = self.initCombatSystem(gameState, display, player)
        pass

    def initCameraSystem(self, camera: Camera, traveler: Traveler):
        return CameraSystem(camera, traveler)

    def initTileSystem(self, world: World, assets: Assets):
        return TileSystem(world, assets)

    def initSpawnSystem(self, assets):
        return SpawnSystem(assets)
                
    def initCombatSystem(self, gameState: GameState, display: Display, player: Player): 
        return CombatSystem(gameState, self.spawnSystem, display, player)


    pass
