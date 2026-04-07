from typing import List
from serialization import serializationUtil
from serialization.messages import FileCorruptedException
from serialization.serializationUtil import SerializationUtil
from world.entities.human import Human
from state.game.player import Player
from core.team import Team
import os
import struct 

class SerializationPlayer:

    def __init__(self, serializationUtil: SerializationUtil, player: Player):
        self.serializationUtil = serializationUtil
        self.player = player


    def saveTeam(self):
        savePath = self.serializationUtil.getPlayerSavePath()

        teams: List[Team] = self.player.teams

        for i in range(9999): 
            newFilename = f"char{i:04d}.dat"
            newFilePath = os.path.join(self.serializationUtil.getPlayerSavePath(), newFilename)
            # print("newFilePath: ", newFilePath)
            if not os.path.exists(newFilePath):

                name = "save_team" 
                encodedName = name.encode("utf-8")

                with open(newFilePath, "wb") as f:
                    f.write(struct.pack("i", len(name)))
                    f.write(encodedName)
                    print("Successfully saved ", name)
                break


    def updateTeam(self): 
        savePath = self.serializationUtil.getPlayerSavePath()

        currentTeam: Team | None = self.player.currentTeam
        if currentTeam == None:
            raise RuntimeError("Current team is empty")

        filePath = f"{savePath}/{currentTeam.filename}"
        if os.path.exists(filePath):
            with open(filePath, "wb") as f:
                name = currentTeam.player.name 
                encodedName = name.encode("utf-8")

                f.write(struct.pack("i", len(name)))
                f.write(encodedName)

               
    def updateTeams(self, team: Team):
        savePath = self.serializationUtil.getSavePath()
        currentTeam = self.player.currentTeam
        if currentTeam == None: 
            raise RuntimeError("player currentTeam is None")

        name = currentTeam.player.name 
        encodedName = name.encode("utf-8")

        for team in self.player.teams: 
            filePath = f"s{savePath}/{team.filename}"

            if os.path.exists(filePath):
                with open(f"{savePath}/filename", "wb") as f:
                   
                    f.write(struct.pack("i", len(name)))
                    f.write(struct.pack(encodedName))


    def loadTeams(self):
        savePath = self.serializationUtil.getPlayerSavePath()

        for file in os.scandir(savePath):
            print("file: ", file.name)
            if file.is_file():
                with open(file, "rb") as f:
                    nameLengthBytes = f.read(4)
                    if len(nameLengthBytes) != 4:
                        FileCorruptedException("name length bytes", file.name)
                    (nameLength,) = struct.unpack("i", nameLengthBytes) 

                    nameBytes = f.read(nameLength)
                    if len(nameBytes) != nameLength:
                        FileCorruptedException("name bytes", file.name)
                    name = nameBytes.decode("utf-8")
                    print("name: ", name)

                    player: Human = Human(name)
                    team: Team = Team(player, None, file.name)

                    self.player.teams.append(team)

        pass
         




