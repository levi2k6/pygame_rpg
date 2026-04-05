
from enums.enumActionMenu import EnumActionMenu
from enums.enumScene import EnumScene
from game.state.gameState import GameState
from init.serializationRegistry import SerializationRegistry
from inputs.inputFunction import InputFunction
from serialization.serializationPlayer import SerializationPlayer


class InputMenu:

    def __init__(self, gameState: GameState, serializationPlayer: SerializationPlayer ):
        self.gameState: GameState = gameState
        self.serializationPlayer: SerializationPlayer = serializationPlayer 
        self.inputs = {
            EnumActionMenu.CREATE_CHARACTER: InputFunction("Create Character", self.serializationPlayer.saveTeam), 
            EnumActionMenu.TEST: InputFunction("menuSomething", self.menuSomething),
        }

    def menuSomething(self): 
        self.gameState.currentScene = EnumScene.WORLD 



