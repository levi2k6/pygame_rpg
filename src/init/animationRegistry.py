from animation.animationSprite import AnimationSprite
from animation.animationWorld import AnimationWorld
from init.worldRegistry import WorldRegistry


class AnimationRegistry:

    def __init__(self, worldRegistry: WorldRegistry):
        self.animationSprite: AnimationSprite = self.initAnimationSprite()
        self.animationWorld: AnimationWorld = self.initAnimationWorld(worldRegistry)
        pass
    
    def initAnimationSprite(self): 
        return AnimationSprite() 

    def initAnimationWorld(self, worldRegistry: WorldRegistry):
        return AnimationWorld(worldRegistry)

