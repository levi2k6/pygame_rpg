from Entity.Player import Player
from Initialization import Display

player: Player = None   

def displayEntities():
    global player
    if player:
        player.draw(Display.screen)

def spawnPlayer():
    global player
    if Player:
        player = Player("forsen")
        print(player.name, "has been spawned")
    
