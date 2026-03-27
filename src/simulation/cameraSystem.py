from Scene.WorldScene.traveler import Traveler
from render.camera import Camera


class CameraSystem:
    def __init__(self, camera: Camera, traveler: Traveler):
        self.camera = camera
        self.traveler = traveler 


    def simulateWorld(self):
        self.camera.position = self.traveler.form.position


    def resetCamera(self): 
        self.camera.position.x = 0 
        self.camera.position.y = 0



