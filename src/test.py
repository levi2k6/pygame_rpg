from init.serializationRegistry import SerializationRegistry
from serialization import serializationUtil
from serialization.serializationPlayer import SerializationPlayer
from serialization.serializationUtil import SerializationUtil
from world.entities.human import Human
from core.player import Player
from world.team import Team


player: Player = Player()

serializationRegistry: SerializationRegistry = SerializationRegistry(player) 

serializationRegistry.serializationPlayer.saveTeam()


for team in player.teams: 
    print("team: ", team.player.name) 

