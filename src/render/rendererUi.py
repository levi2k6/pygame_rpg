
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
        self.settingsState = stateRegistry.settingsState
        self.uiMenu = uiRegistry.uiMenu 
        self.uiWorld = uiRegistry.uiWorld
        self.uiCombat = uiRegistry.uiCombat


    def renderUiMenu(self, delta: float): 
        if self.gameState.currentScene != self.gameState.lastScene:
            print("show menu")
            for ui in self.uiMenu.uis:
                ui.show()
            for ui in self.uiWorld.uis:
                ui.hide()
            for ui in self.uiCombat.uis:
                ui.hide()

            self.gameState.lastScene = self.gameState.currentScene

        self.uiManager.update(delta)
        self.uiManager.draw_ui(self.settingsState.display.screen)

    def renderUiWorld(self, delta: float):
        if self.gameState.currentScene != self.gameState.lastScene:
            print("show world")
            for ui in self.uiWorld.uis:
                ui.show()
            for ui in self.uiMenu.uis:
                ui.hide()
            for ui in self.uiCombat.uis:
                ui.hide()

            self.gameState.lastScene = self.gameState.currentScene

        self.uiManager.update(delta)
        self.uiManager.draw_ui(self.settingsState.display.screen)

    
    def renderUICombat(self, delta: float):
        if self.gameState.currentScene != self.gameState.lastScene:
            print("show combat")
            for ui in self.uiCombat.uis:
                ui.show()
            for ui in self.uiMenu.uis:
                ui.hide()
            for ui in self.uiCombat.uis:
                ui.hide()

            self.gameState.lastScene = self.gameState.currentScene

        self.uiManager.update(delta)
        self.uiManager.draw_ui(self.settingsState.display.screen)



            


