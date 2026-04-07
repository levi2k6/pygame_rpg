from init.stateRegistry import StateRegistry
from loadedAssets.assetsRegistry import AssetsRegistry
from simulation.simulationNavigation import SimulationNavigation
from simulation.world.simulationTileGeneration import SimulationTileGeneration
from state.game.gameState import GameState
from state.settings.display import Display
from simulation.simulationState import SimulationState
from simulation.simulationUi import SimulationUi
from init.worldRegistry import WorldRegistry
from simulation.simulationCombat import SimulationCombat 
from simulation.simulationMovement import SimulationMovement
from simulation.simulationSpawn import SimulationSpawn 
from simulation.simulationMovement import SimulationMovement
from state.game.player import Player
from ui.uiRegistry import UIRegistry
from world.world import World


class SimulationRegistry: 

    def __init__(self, 
                 stateRegistry: StateRegistry,
                 assetsRegistry: AssetsRegistry,
                 worldRegistry: WorldRegistry,
                 uiRegistry: UIRegistry,
     ):
        self.simulationNavigation: SimulationNavigation = self.initSimulationNavigation(stateRegistry.gameState) 
        self.simulationTileGeneration: SimulationTileGeneration = self.initSimulationTileGeneration(worldRegistry, assetsRegistry)
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

    def initSimulationNavigation(self, gameState: GameState):
        return SimulationNavigation(gameState) 

    def initSimulationTileGeneration(self, worldRegistry: WorldRegistry, assetsRegistry: AssetsRegistry):
        return SimulationTileGeneration(worldRegistry, assetsRegistry)

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


