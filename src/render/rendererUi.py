
from enum import Enum
from typing import List
from pygame import Event
from pygame_gui import UIManager

from state.settings.display import Display
from enums.enumScene import EnumScene
from init.coreRegistry import CoreRegistry
from init.stateRegistry import StateRegistry
from ui import uiWorld
from ui.uiRegistry import UIRegistry


class RendererUI:
    def __init__(self, uiRegistry: UIRegistry, stateRegistry: StateRegistry):
        self.uiManager = uiRegistry.uiManager 
        self.gameState = stateRegistry.gameState
        self.uiMenu = uiRegistry.uiMenu 
        self.uiWorld = uiRegistry.uiWorld

        self.lastScene: EnumScene | None = None

    def renderUi(self, display: Display, delta: float):

        if self.gameState.currentScene != self.lastScene: 
            if self.gameState.currentScene == EnumScene.MENU: 
                for ui in self.uiMenu.uis:
                    ui.show()
                for ui in self.uiWorld.uis:
                    ui.hide()
            elif self.gameState.currentScene == EnumScene.WORLD:
                for ui in self.uiWorld.uis:
                    ui.show()
                for ui in self.uiMenu.uis:
                    ui.hide()

            self.lastScene = self.gameState.currentScene


        self.uiManager.update(delta)
        self.uiManager.draw_ui(display.screen)



