from init.gameStateRegistry import StateRegistry
from inputs.inputRegistry import InputRegistry
from loadedAssets.assetsRegistry import AssetsRegistry
from game.state.gameState import GameState
from game.state.display import Display
from simulation.eventHandler import EventHandler
from simulation.simulationState import SimulationState
from simulation.simulationUi import SimulationUi
from init.worldRegistry import WorldRegistry
from simulation.simulationCombat import SimulationCombat 
from simulation.simulationMovement import SimulationMovement
from simulation.simulationSpawn import SimulationSpawn 
from simulation.simulationMovement import SimulationMovement
from game.state.player import Player
from ui.uiRegistry import UIRegistry
from world.world import World


class SimulationRegistry: 

    def __init__(self, 
                 stateRegistry: StateRegistry,
                 assetsRegistry: AssetsRegistry,
                 worldRegistry: WorldRegistry,
                 uiRegistry: UIRegistry
     ):
        self.simulationMovement: SimulationMovement = self.initSimulationMovement(worldRegistry.world, assetsRegistry.textures)
        self.simulationUi: SimulationUi = self.initSimulationUi(stateRegistry, uiRegistry)
        self.simulationState: SimulationState = self.initSimulationState(stateRegistry, self.simulationUi)

        self.simulationSpawn: SimulationSpawn = self.initSimulationSpawn()
        self.simulationCombat: SimulationCombat = self.initSimulationCombat(
                stateRegistry.gameState,
                self.simulationSpawn,
                stateRegistry.settingsState.display,
                stateRegistry.gameState.player
        )
        pass

    def initSimulationMovement(self, world: World, textures: dict):
        return SimulationMovement(world, textures)

    def initSimulationUi(self, stateRegistry: StateRegistry, uiRegistry: UIRegistry):
        return SimulationUi(stateRegistry, uiRegistry) 

    def initSimulationState(self, stateRegistry: StateRegistry, simulationUi: SimulationUi):
        return SimulationState(stateRegistry, simulationUi) 

    def initSimulationSpawn(self):
        return SimulationSpawn()
                
    def initSimulationCombat(self, gameState: GameState, spawnSystem: SimulationSpawn, display: Display, player: Player): 
        return SimulationCombat(gameState, spawnSystem, display, player)

    def initEventHandler(self, gameState: GameState, uiRegistry: UIRegistry, inputRegistry: InputRegistry): 
        return EventHandler(gameState, uiRegistry, inputRegistry) 
