from Initialization import Display
from Component.Stats import Stats

class Human:
    name: str = ""  
    x: float = 0
    y: float = 0
    bodyColor = (0, 0, 0)
    body = None
    spriteWidth = 0 
    spriteHeight = 0 
    sprite = None
    
    stats: Stats = None

    def getProperties(self):
        return {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "body_color": self.bodyColor,
            "body": self.body,
            "sprite_width": self.spriteWidth,
            "sprite_height": self.spriteHeight,
            "sprite": self.sprite 
        }
    
    

