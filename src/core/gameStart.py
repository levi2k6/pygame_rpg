from init.renderRegistry import RenderRegistry
from init.stateRegistry import StateRegistry
from render.rendererSprite import RendererSprite 
from init.animationRegistry import AnimationRegistry
from init.simulationRegistry import SimulationRegistry
from init.worldRegistry import WorldRegistry
from simulation.simulationMovement import SimulationMovement
from simulation.world.simulationTileGeneration import SimulationTileGeneration
from state.game.gameState import GameState
from world.traveler import Traveler
from world.world import World


class GameStart:
    def __init__(self, stateRegistry: StateRegistry, worldRegistry: WorldRegistry, simulationRegistry: SimulationRegistry, rendererRegistry: RenderRegistry):
        self.startTileGeneration(simulationRegistry.simulationTileGeneration)
        self.startTraveler(worldRegistry.world.traveler, rendererRegistry.rendererSprite, simulationRegistry.simulationMovement)
        pass

    def startTileGeneration(self, simulationTileGeneration: SimulationTileGeneration): 
        simulationTileGeneration.generateTiles()
        
    def startTraveler(self, traveler: Traveler, rendererSprite: RendererSprite, simulationMovement: SimulationMovement):
        rendererSprite.initSprite(traveler.sprite)
        simulationMovement.spawnTravelerInTiles()



