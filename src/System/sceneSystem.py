from Scene.sceneFactory import SceneFactory
from Scene.CombatScene.combatScene import CombatScene
from System.renderSystem import RenderSystem

class SceneSystem:
    def __init__(self, renderSystem: RenderSystem, sceneFactory: SceneFactory):
        self.renderSystem = renderSystem 
        self.sceneFactory = sceneFactory 

        self.currentScene: str = ""

    def sceneChecker(self):
        scene = self.sceneFactory.create("CombatScene")
        if scene == None: raise RuntimeError("Scene not found in SceneFactory") 
        self.renderSystem.renderScene(scene)

