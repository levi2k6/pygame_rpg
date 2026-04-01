
from typing import Dict, List
import pygame
from pygame import Event
from pygame_gui import UIManager
import pygame_gui

from core.gameState import GameState
from enums.enumScene import EnumScene
from init.coreRegistry import CoreRegistry
from init.renderRegistry import RenderRegistry
from inputs.inputFunction import InputFunction
from inputs.inputRegistry import InputRegistry
from ui import uiMenu
from ui.uiMenu import UIMenu
from ui.uiRegistry import UIRegistry
from ui.uiWorld import UIWorld


class EventHandler:

    def __init__(self, gameState: GameState, uiRegistry: UIRegistry, inputRegistry: InputRegistry):
        self.gameState: GameState = gameState 
        self.uiManager: UIManager = uiRegistry.uiManager
        self.uiMenu: UIMenu = uiRegistry.uiMenu
        self.uiWorld: UIWorld = uiRegistry.uiWorld
        self.inputRegistry = inputRegistry

    def processEvent(self, events: List[Event]):
        for event in events:
            if event.type == pygame.QUIT:
                print("quit")
                return False 

            print("currentScene: ", self.gameState.currentScene)

            self.eventInput(event)
            self.uiManager.process_events(event)

        return True

    def eventInput(self, event): 
        if event.type == pygame.KEYDOWN:
            inputFunc: InputFunction | None

            if self.gameState.currentScene == EnumScene.MENU: 
                inputFunc = self.inputRegistry.menuInputs.get(event.key)
            elif self.gameState.currentScene == EnumScene.WORLD:
                inputFunc = self.inputRegistry.worldInputs.get(event.key)

            if inputFunc == None:
                print("key does not exists")
                return

            inputFunc.func()

        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            inputFunc: InputFunction | None

            print("ui_element: ", event.ui_element)

            if self.gameState.currentScene == EnumScene.MENU:
                inputFunc = self.uiMenu.uis.get(event.ui_element)
            if self.gameState.currentScene == EnumScene.WORLD:
                inputFunc = self.uiWorld.uis.get(event.ui_element)

            if inputFunc == None:
                print("ui input does not exists")
                return

            inputFunc.func()







