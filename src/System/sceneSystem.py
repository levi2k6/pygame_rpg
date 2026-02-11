from Scene.scene import Scene
from Scene.sceneFactory import SceneFactory
from Scene.CombatScene.combatScene import CombatScene
from System.renderSystem import RenderSystem
from util.enums.SceneEnum import SceneEnum

class SceneSystem:

    def __init__(self, renderSystem: RenderSystem, sceneFactory: SceneFactory):
        self.renderSystem = renderSystem 
        self.sceneFactory = sceneFactory 

        self.currentScene: Scene | None  
        self.changeScene(SceneEnum.COMBAT)

    def changeScene(self, sceneEnum: SceneEnum):
        self.currentScene = self.sceneFactory.create(sceneEnum)


    def sceneChecker(self):
        if self.currentScene == None: raise RuntimeError("Scene not found in SceneFactory") 
        self.renderSystem.renderScene(self.currentScene)

