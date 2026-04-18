
from enum import Enum
from typing import Dict, List
import pygame
from pygame import Event
from pygame_gui import UIManager
import pygame_gui

from enums import enumActionWorld
from enums.enumActionBasic import EnumActionBasic
from enums.enumActionMenu import EnumActionMenu
from enums.enumActionWorld import EnumActionWorld
from state.game.gameState import GameState
from enums.enumScene import EnumScene
from state.settings.settingsState import SettingsState
from init.stateRegistry import StateRegistry
from inputs.inputBasic import InputBasic
from inputs.inputFunction import InputFunction
from init.inputRegistry import InputRegistry
from ui import uiMenu
from ui.uiCombat import UICombat
from ui.uiMenu import UIMenu
from ui.uiRegistry import UIRegistry
from ui.uiWorld import UIWorld


class EventHandler:

    def __init__(self, stateRegistry: StateRegistry, uiRegistry: UIRegistry, inputRegistry: InputRegistry):
        self.gameState: GameState = stateRegistry.gameState 
        self.settingsState: SettingsState = stateRegistry.settingsState 
        self.uiManager: UIManager = uiRegistry.uiManager
        self.uiMenu: UIMenu = uiRegistry.uiMenu
        self.uiWorld: UIWorld = uiRegistry.uiWorld
        self.uiCombat: UICombat = uiRegistry.uiCombat
        self.inputBasic: InputBasic = inputRegistry.inputBasic
        self.inputMenu = inputRegistry.inputMenu
        self.inputWorld = inputRegistry.inputWorld 
        self.inputCombat = inputRegistry.inputCombat


    def processEvents(self, events):
        if self.gameState.currentScene == EnumScene.MENU:
            self.handleInput(events, self.inputMenu.inputs, self.uiMenu.actions)
        elif self.gameState.currentScene == EnumScene.WORLD:
            self.handleInput(events, self.inputWorld.inputs, self.uiWorld.actions)
        elif self.gameState.currentScene == EnumScene.COMBAT:
            self.handleInput(events, self.inputCombat.inputs, self.uiCombat.actions)

    def handleInput(self, events: List[Event], inputSceneInputs: dict, uiSceneActions: dict):
        for event in events:
            inputFunc: InputFunction | None = None

            if event.type == pygame.KEYDOWN:

                customKeymaps: dict = self.settingsState.keymapsSettings.customKeymaps
                defaultKeymaps: dict = self.settingsState.keymapsSettings.defaultKeymaps

                keyAction = None
                if len(customKeymaps):
                    keyAction = customKeymaps.get(event.key) 
                    if keyAction == None:
                        keyAction = defaultKeymaps.get(event.key)
                        if keyAction == None:
                            print("key is not tied to any action")
                else:
                    keyAction = defaultKeymaps.get(event.key)
                    if keyAction == None:
                        print("key is not tied to any action")


                inputFunc = inputSceneInputs.get(keyAction)

            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                print("ui_element: ", event.ui_element)
                action: Enum | None = uiSceneActions.get(event.ui_element) 
                print("action :", action)
                if action == None:
                    print("UI element does not point to any action")

                inputFunc = inputSceneInputs.get(action)
                print("inputFunc: ", inputFunc)
        
            elif event.type == pygame.QUIT:
                print("quit")
                self.gameState.isRunning = False 


            if inputFunc != None:
                inputFunc.func()
                print("currentScene:", self.gameState.currentScene)


            self.uiManager.process_events(event)

