
from Scene.WorldScene.traveler import Traveler
from render.camera import Camera
from world.entities.human import Human
from core.player import Player
from world.team import Team


class SimulateBasic:
    def __init__(self, camera: Camera, traveler: Traveler):
        self.camera = camera
        self.traveler = traveler 


    def simulateWorldCamera(self):
        self.camera.position = self.traveler.form.position


