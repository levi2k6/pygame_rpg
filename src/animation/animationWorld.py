


from core.sprite import Sprite
from init.worldRegistry import WorldRegistry


class AnimationWorld:

    def __init__(self, worldRegistry: WorldRegistry):
        self.world = worldRegistry.world
        pass

    def animateWorld(self):
        self.animateTraveler()

    def animateTraveler(self):
        sprite: Sprite = self.world.traveler.sprite 
        sprite.position = self.world.traveler.position
        pass

