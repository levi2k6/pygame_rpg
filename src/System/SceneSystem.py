from Initialization import Display

from Scene.CombatScene import CombatScene

currentScene: str = ""

def sceneChecker():
    if currentScene == "MainMenu":
        pass
    if currentScene == "CombatScene":
        CombatScene.drawScene()


