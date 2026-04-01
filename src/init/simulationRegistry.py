
from pygame_gui import UIManager
from Initialization.assets import Assets
from core.eventHandler import EventHandler
from inputs.inputRegistry import InputRegistry
from loadedAssets.assetsRegistry import AssetsRegistry
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
from ui.uiRegistry import UIRegistry
from world.world import World


class SimulationRegistry: 

    def __init__(self, coreRegistry: CoreRegistry,  assetsRegistry: AssetsRegistry, worldRegistry: WorldRegistry, inputRegistry: InputRegistry, uiRegistry: UIRegistry):
        self.tilesSystem: TileSystem = self.initTileSystem(worldRegistry.world, assetsRegistry.textures)
        self.spawnSystem: SpawnSystem = self.initSpawnSystem(assetsRegistry.textures)
        self.combatSystem: CombatSystem = self.initCombatSystem(coreRegistry.gameState, coreRegistry.display, coreRegistry.player)
        self.eventHandler: EventHandler = self.initEventHandler(coreRegistry.gameState, uiRegistry, inputRegistry) 
        pass

    def initTileSystem(self, world: World, textures: dict):
        return TileSystem(world, textures)

    def initSpawnSystem(self, assets):
        return SpawnSystem(assets)
                
    def initCombatSystem(self, gameState: GameState, display: Display, player: Player): 
        return CombatSystem(gameState, self.spawnSystem, display, player)

    def initEventHandler(self, gameState: GameState, uiRegistry: UIRegistry, inputRegistry: InputRegistry): 
        return EventHandler(gameState, uiRegistry, inputRegistry) 
    pass
