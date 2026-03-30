
from enums.enumScene import EnumScene
from core.gameState import GameState
from init.serializationRegistry import SerializationRegistry
from serialization.serializationPlayer import SerializationPlayer


class InputMenu:

    def __init__(self, gameState: GameState, serializationPlayer: SerializationPlayer ):
        self.gameState: GameState = gameState
        self.serializationPlayer: SerializationPlayer = serializationPlayer 

    def playGame(self):
        print("play game")
    
    def navigateWorld(self): 
        self.gameState.currentScene = EnumScene.WORLD 



    




