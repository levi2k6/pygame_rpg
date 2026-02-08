from Scene.combatScene import CombatScene
from System.renderSystem import RenderSystem

class SceneSystem:
    def __init__(self, renderSystem: RenderSystem, combatScene: CombatScene):
        self.renderSystem = renderSystem 
        self.combatScene = combatScene

    currentScene: str = ""

    def sceneChecker(self):
        if self.currentScene == "MainMenu":
            pass
        elif self.currentScene == "CombatScene":
            self.renderSystem.renderCombatScene(self.combatScene)
