

from init.simulationRegistry import SimulationRegistry
from init.worldRegistry import WorldRegistry
from simulation.simulationMovement import SimulationMovement
from world.world import World


class GameInit:
    def __init__(self, simulationRegistry: SimulationRegistry):
        self.initTraveler(simulationRegistry.simulationMovement)
        pass

    def initTraveler(self, simulationMovement: SimulationMovement):
        simulationMovement.spawnTravelerInTiles



