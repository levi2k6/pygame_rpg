


from game.state.gameState import GameState
from enums.enumActionBasic import EnumActionBasic
from enums.enumActionWorld import EnumActionWorld
from enums.enumScene import EnumScene


class InputBasic:

    def __init__(self, gameState: GameState):

        self.gameState = gameState

        self.actions = {
            EnumActionBasic.NAVIGATE_MENU: self.navigateMenu, 
            EnumActionBasic.NAVIGATE_WORLD: self.navigateWorld,
            EnumActionBasic.NAVIGATE_SETTINGS: self.navigateSettings
        }

        pass
        

    def navigateMenu(self):
        self.gameState.currentScene = EnumScene.MENU
        pass

    def navigateWorld(self):
        self.gameState.currentScene = EnumScene.WORLD
        pass

    def navigateSettings(self):
        self.gameState.currentScene = EnumScene.SETTINGS
        pass

    pass


