from pygame.color import Color
from pygame.math import Vector2

from Entity.marker import Marker
from Properties.form import Form
from Scene.scene import Scene
from Prop.prop import Prop
from Initialization.assets import Assets


class MainMenuScene(Scene):
    def __init__(self, assets: Assets):
        super().__init__()
        self.assets = assets
        self.setProps()
        pass

    def setProps(self):
        position: Vector2 = Vector2(300, 300)
        size: Vector2 = Vector2(400, 400)
        form: Form = Form(position, size, self.assets.data["forsen"])
        prop: Prop = Prop("testProp", form)
        self.props.append(prop)

        markerPosition: Vector2 = Vector2(500, 500)
        self.markers.append(Marker("markerTest", markerPosition))
        pass

    pass
