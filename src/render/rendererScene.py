
from pygame import Color, Rect, Vector2, draw

from gameState.gameState import GameState
from Initialization.display import Display
from Scene.CombatScene.combatScene import CombatScene
from Scene.WorldScene.tileSystem import TileSystem
from Scene.WorldScene.worldScene import WorldScene
from Scene.scene import Scene
from System.camera import Camera
from System.world import World
from render.rendererBasic import rendererBasic
from util.enums.SceneEnum import SceneEnum


class RendererScene:

    def __init__(self, gameState: GameState , display: Display, rendererBasic: rendererBasic, world: World, camera: Camera, combatScene: CombatScene):
        self.gameState = gameState 
        self.display = display
        self.rendererBasic = rendererBasic 
        self.world = world
        self.camera = camera
        self.combatScene = combatScene
        pass

    def renderTransition(self, scene: SceneEnum):
        if scene == SceneEnum.WORLD:
            self.renderWorldScene(self.world)
        elif scene == SceneEnum.COMBAT:
            self.renderCombatScene(self.combatScene)


    def renderScene(self, scene: Scene):
        rectX = self.world.rect.x - self.camera.rect.x
        rectY = self.world.rect.y - self.camera.rect.y
        viewRect: Rect = Rect(rectX, rectY, self.display.size.x, self.display.size.y)

        if not len(scene.props) == 0:
            for prop in scene.props:
                print("name: ", prop.name)
                self.rendererBasic.renderTexture(prop.form.sprite, prop.form.size, prop.form.position)

    def renderCombatScene(self, scene: World): 
        self.renderScene(scene)

        if len(scene.entities["team1"]) != 0:
            for entity in scene.entities["team1"]: 
                self.rendererBasic.renderEntity(entity)

        if len(scene.entities["team2"]) != 0:
            for entity in scene.entities["team2"]: 
                self.rendererBasic.renderEntity(entity)


    def renderWorldScene(self, scene: WorldScene):

        self.renderScene(scene)

        tileSystem: TileSystem = scene.tileSystem 
        if len(tileSystem.tiles) == 0:
            return

        for i in range(len(tileSystem.tiles)):
            for tile in tileSystem.tiles[i]:
                if self.gameState.isPositionShow == True:

                    color: Color = Color(255, 255, 0)
                    topLeft = tile.rect.topleft - self.camera.position 
                    topRight = tile.rect.topright - self.camera.position
                    bottomRight = tile.rect.bottomright - self.camera.position
                    bottomLeft = tile.rect.bottomleft - self.camera.position

                    draw.line(self.display.screen, color, topLeft, topRight)
                    draw.line(self.display.screen, color, topRight, bottomRight)
                    draw.line(self.display.screen, color, bottomRight, bottomLeft)
                    draw.line(self.display.screen, color, bottomLeft, topLeft)

        if tileSystem.traveler != None:
            traveler = tileSystem.traveler
            self.rendererBasic.renderTexture(traveler.form.transformedSprite, traveler.form.size, traveler.form.position)

        self.rendererBasic.renderCamera()

        pass

