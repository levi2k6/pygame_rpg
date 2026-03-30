
from Initialization.assets import Assets
from assets.assetsRegistry import AssetsRegistry
from core.gameState import GameState
from Initialization.display import Display
from Scene.WorldScene.traveler import Traveler
from init.coreRegistry import CoreRegistry
from init.worldRegistry import WorldRegistry
from render.camera import Camera
from simulation.cameraSystem import CameraSystem
from simulation.combatSystem import CombatSystem
from simulation.spawnSystem import SpawnSystem
from simulation.tilesSystem import TileSystem
from core.player import Player
from world.world import World


class SimulationRegistry: 

    def __init__(self, coreRegistry: CoreRegistry,  assetsRegistry: AssetsRegistry, worldRegistry: WorldRegistry):
        self.tilesSystem: TileSystem = self.initTileSystem(worldRegistry.world, assetsRegistry.textures)
        self.spawnSystem: SpawnSystem = self.initSpawnSystem(assetsRegistry.textures)
        self.combatSystem: CombatSystem = self.initCombatSystem(coreRegistry.gameState, coreRegistry.display, coreRegistry.player)
        pass

    def initTileSystem(self, world: World, textures: dict):
        return TileSystem(world, textures)

    def initSpawnSystem(self, assets):
        return SpawnSystem(assets)
                
    def initCombatSystem(self, gameState: GameState, display: Display, player: Player): 
        return CombatSystem(gameState, self.spawnSystem, display, player)


    pass
