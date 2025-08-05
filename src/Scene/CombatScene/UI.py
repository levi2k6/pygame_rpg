import pygame
import pygame_gui
from System import UISystem 

from Initialization import Display 


panel = UISystem.createPanel(
    position=(0, 0),
    size=(400, 400)
)

label = UISystem.createLabel(
    position=(400/2, 400/2),
    size=(100, 100),
    text="hello",
    container=panel
)


    
    






