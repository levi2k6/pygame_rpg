
from enum import Enum
from typing import List
from pygame import Event
from pygame_gui import UIManager

from game.state.settings.display import Display
from enums.enumScene import EnumScene
from init.coreRegistry import CoreRegistry
from init.gameStateRegistry import StateRegistry
from ui import uiWorld
from ui.uiRegistry import UIRegistry


class RendererUI:
    def __init__(self, uiRegistry: UIRegistry, stateRegistry: StateRegistry ):
        self.uiManager = uiRegistry.uiManager 
        self.gameState = stateRegistry.gameState
        self.uiMenu = uiRegistry.uiMenu 
        self.uiWorld = uiRegistry.uiWorld

    def renderUi(self, uiManager: UIManager, display: Display, delta: float):
        uiManager.update(delta)
        uiManager.draw_ui(display.screen)

