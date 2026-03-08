from Scene.MainMenuScene.mainMenuScene import MainMenuScene
from Scene.WorldScene.worldScene import WorldScene
from Scene.scene import Scene
from Scene.sceneFactory import SceneFactory
from Scene.CombatScene.combatScene import CombatScene
from System.renderSystem import RenderSystem
from render.rendererScene import RendererScene
from util.enums.SceneEnum import SceneEnum

class SceneSystem:

    def __init__(self, sceneFactory: SceneFactory, rendererScene: RendererScene):
        self.sceneFactory = sceneFactory 
        self.rendererScene = rendererScene

        self.currentScene: Scene | None  
        self.changeScene(SceneEnum.COMBAT)

    def changeScene(self, sceneEnum: SceneEnum):
        self.currentScene = self.sceneFactory.create(sceneEnum)

    def sceneChecker(self):
        if self.currentScene is None: raise RuntimeError("Scene not found in SceneFactory")
        if type(self.currentScene) == CombatScene:
            self.rendererScene.renderCombatScene(self.currentScene)
        elif type(self.currentScene) == MainMenuScene:
            self.rendererScene.renderScene(self.currentScene)
        elif type(self.currentScene) == WorldScene:
            self.rendererScene.renderWorldScene(self.currentScene)

