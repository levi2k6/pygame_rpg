from Entity.entity import Entity
from GameState.gameState import GameState
from Initialization.assets import Assets
from Initialization.display import Display
from Scene.CombatScene.combatScene import CombatScene
from Scene.CombatScene.combatSystem import CombatSystem
from Scene.CombatScene.spawnSystem import SpawnSystem
from Scene.MainMenuScene.mainMenuScene import MainMenuScene
from Scene.WorldScene.worldScene import WorldScene
from Scene.scene import Scene
from util.enums.SceneEnum import SceneEnum

class SceneFactory:

    def __init__(self, display: Display, gameState: GameState, assets: Assets):
        self.gameState = gameState
        self.assets = assets
        self.display = display

    def create(self, sceneEnum: SceneEnum ) -> Scene | None:
        if sceneEnum == SceneEnum.MAINMENU:
            return MainMenuScene(self.assets)
        elif sceneEnum == SceneEnum.WORLD:
            return WorldScene()
        elif sceneEnum == SceneEnum.COMBAT:
            combatSystem: CombatSystem = CombatSystem()
            spawnSystem: SpawnSystem = SpawnSystem(self.assets)
            return CombatScene(self.gameState, combatSystem, spawnSystem, self.display);
        return None

