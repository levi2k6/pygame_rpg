from Scene.MainMenuScene.mainMenuScene import MainMenuScene
from Scene.WorldScene.worldScene import WorldScene
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
        if self.currentScene is None: raise RuntimeError("Scene not found in SceneFactory")
        if type(self.currentScene) == CombatScene:
            self.renderSystem.renderScene(self.currentScene)
        elif type(self.currentScene) == MainMenuScene:
            self.renderSystem.renderScene(self.currentScene)
        elif type(self.currentScene) == WorldScene:
            self.renderSystem.renderScene(self.currentScene)

