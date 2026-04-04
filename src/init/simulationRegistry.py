from pygame_gui import UIManager
from init.gameStateRegistry import StateRegistry
from inputs.inputHandler import  InputHandler 
from inputs.inputRegistry import InputRegistry
from loadedAssets import assetsRegistry
from loadedAssets.assetsRegistry import AssetsRegistry
from game.state.gameState import GameState
from core.display import Display
from world.traveler import Traveler
from init.coreRegistry import CoreRegistry
from init.worldRegistry import WorldRegistry
from render.camera import Camera
from simulation.cameraSystem import CameraSystem
from simulation.simulationCombat import SimulationCombat 
from simulation.simulationMovement import SimulationMovement
from simulation.simulationSpawn import SpawnSystem
from simulation.simulationMovement import SimulationMovement
from game.state.player import Player
from ui.uiRegistry import UIRegistry
from world.world import World


class SimulationRegistry: 

    def __init__(self, 
                 coreRegistry:CoreRegistry,
                 stateRegistry: StateRegistry,
                 assetsRegistry: AssetsRegistry,
                 worldRegistry: WorldRegistry,
                 inputRegistry: InputRegistry,
                 uiRegistry: UIRegistry
     ):
        self.simulationMovement: SimulationMovement = self.initSimulationMovement(worldRegistry.world, assetsRegistry.textures)
        self.spawnSystem: SpawnSystem = self.initSpawnSystem(assetsRegistry.textures)
        self.simulationCombaht: SimulationCombat = self.initCombatSystem(stateRegistry.gameState, coreRegistry.display, coreRegistry.player)
        self.eventHandler: InputHandler = self.initEventHandler(stateRegistry.gameState, uiRegistry, inputRegistry) 
        pass

    def initSimulationMovement(self, world: World, textures: dict):
        return SimulationMovement(world, textures)

    def initSpawnSystem(self, assets: dict):
        return SpawnSystem()
                
    def initCombatSystem(self, gameState: GameState, display: Display, player: Player): 
        return SimulationCombat(gameState, self.spawnSystem, display, player)

    def initEventHandler(self, gameState: GameState, uiRegistry: UIRegistry, inputRegistry: InputRegistry): 
        return InputHandler(gameState, uiRegistry, inputRegistry) 
    pass
