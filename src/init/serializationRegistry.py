import platform
import os
import sys

from serialization.serializationPlayer import SerializationPlayer
from serialization.serializationUtil import SerializationUtil
from state.game.player import Player


class SerializationRegistry:
    def __init__(self, player: Player):
        self.serializationUtil: SerializationUtil = self.initSerializationUtil()
        self.serializationPlayer = self.initSerializationPlayer(self.serializationUtil, player)
        pass

    def initSerializationUtil(self):
        serializationUtil: SerializationUtil = SerializationUtil()
        serializationUtil.initSaveDirectories()
        return serializationUtil

    def initSerializationPlayer(self, serializationUtil: SerializationUtil, player: Player): 
        serializationPlayer: SerializationPlayer = SerializationPlayer(serializationUtil, player)
        serializationPlayer.loadTeams()
        return serializationPlayer



