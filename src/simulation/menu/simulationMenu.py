
from init.serializationRegistry import SerializationRegistry
from serialization.serializationPlayer import SerializationPlayer


class SimulationMenu:

    def __init__(self, serializationRegistry: SerializationRegistry):
        self.serializationPlayer: SerializationPlayer = serializationRegistry.serializationPlayer


    def startMenu(self):
        self.serializationPlayer.loadTeams()
        pass


    def endMenu(self):
        pass

