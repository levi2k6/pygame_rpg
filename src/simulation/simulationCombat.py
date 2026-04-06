from game.state.game.gameState import GameState
from game.state.settings.display import Display
from simulation.simulationSpawn import SimulationSpawn 
from game.state.game.player import Player
from game.state.game.team import Team


class SimulationCombat:

    def __init__(self, gameState: GameState, simulationSpawn: SimulationSpawn, display: Display, player: Player):
        super().__init__()
        self.gameState = gameState
        self.team1: dict = {"player": None, "companion": None}
        self.team2: dict = {"enemy1": None, "enemy2": None}
        self.turnQueue = []


        self.simulationSpawn = simulationSpawn 
        self.display = display
        self.player = player

    def spawnEntities(self):
        #init entities
        playerCurrentTeam: Team | None = self.player.currentTeam
        if playerCurrentTeam == None:
            raise RuntimeError("Player entity is empty")

        self.team1["player"] = playerCurrentTeam.player
        self.team1["companion"] = playerCurrentTeam.companion

        self.team2["enemy1"] = self.simulationSpawn.spawnGoblin()
        self.team2["enemy2"] = self.simulationSpawn.spawnGoblin()
        pass


