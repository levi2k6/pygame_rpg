from enums.enumScene import EnumScene

class GameState: 
    def __init__(self, currentScene: EnumScene):
        self.currentScene: EnumScene = currentScene

        #debugging
        self.isPositionShow: bool = True 


