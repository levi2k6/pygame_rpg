
from world.traveler import Traveler
from render.camera import Camera
from world.entities.human import Human
from game.state.player import Player
from game.state.team import Team


class SimulationBasic:
    def __init__(self, camera: Camera, traveler: Traveler):
        self.camera = camera
        self.traveler = traveler 


    def simulateWorldCamera(self):
        self.camera.position = self.traveler.form.position


