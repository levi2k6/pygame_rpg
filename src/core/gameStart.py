from init.simulationRegistry import SimulationRegistry
from init.worldRegistry import WorldRegistry
from simulation.simulationMovement import SimulationMovement
from simulation.world.simulationTileGeneration import SimulationTileGeneration
from world.world import World


class GameStart:
    def __init__(self, simulationRegistry: SimulationRegistry):
        self.startTileGeneration(simulationRegistry.simulationTileGeneration)
        # self.startTraveler(simulationRegistry.simulationMovement)
        pass

    def startTileGeneration(self, simulationTileGeneration: SimulationTileGeneration): 
        simulationTileGeneration.generateTiles()
        

    def startTraveler(self, simulationMovement: SimulationMovement):
        simulationMovement.spawnTravelerInTiles()



