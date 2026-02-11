from Entity.entity import Entity
from GameState.gameState import GameState
from Initialization.assets import Assets
from Scene.CombatScene.combatScene import CombatScene
from Scene.CombatScene.combatSystem import CombatSystem
from Scene.CombatScene.spawnSystem import SpawnSystem
from Scene.MainMenuScene.mainMenuScene import MainMenuScene
from Scene.scene import Scene
from util.enums.SceneEnum import SceneEnum

class SceneFactory:

    def __init__(self, gameState: GameState, assets: Assets):
        self.gameState = gameState
        self.assets = assets

    def create(self, sceneEnum: SceneEnum ) -> Scene | None:
        if sceneEnum == SceneEnum.MAINMENU:
            return MainMenuScene()
        elif sceneEnum == SceneEnum.COMBAT:
            combatSystem: CombatSystem = CombatSystem()
            spawnSystem: SpawnSystem = SpawnSystem(self.assets)
            return CombatScene(self.gameState, combatSystem, spawnSystem); 
        return None

