
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
        self.inputBasic: InputBasic = inputRegistry.inputBasic
        self.inputMenu = inputRegistry.inputMenu
        self.inputWorld = inputRegistry.inputWorld 

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
            #key input
            inputFunc: InputFunction | None

            customKeymaps: dict = self.settingsState.keymapsSettings.customKeymaps
            defaultKeymaps: dict = self.settingsState.keymapsSettings.defaultKeymaps

            keyAction = None
            if len(customKeymaps):
                keyAction = customKeymaps.get(event.key) 
                if keyAction == None:
                    keyAction = defaultKeymaps.get(event.key)
                    if keyAction == None:
                        print("key is not tied to any action")
                        return
            else:
                keyAction = defaultKeymaps.get(event.key)
                if keyAction == None:
                    print("key is not tied to any action")
                    return

            if self.gameState.currentScene == EnumScene.MENU: 
                inputFunc: InputFunction | None = self.inputMenu.inputs.get(keyAction)
            elif self.gameState.currentScene == EnumScene.WORLD:
                inputFunc: InputFunction | None = self.inputWorld.inputs.get(keyAction)

            if inputFunc == None:
                print("Action does not point to any input")
                return

            inputFunc.func()

        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            #ui input
            inputFunc: InputFunction | None

            print("ui_element: ", event.ui_element)

            if self.gameState.currentScene == EnumScene.MENU:
                actionMenu: EnumActionMenu | EnumActionBasic | None = self.uiMenu.actions.get(event.ui_element)
                if(actionMenu == None): 
                    print("Action does not point to any menu input")
                    return

                inputFunc = self.inputMenu.inputs.get(actionMenu)

            if self.gameState.currentScene == EnumScene.WORLD:
                actionWorld: EnumActionWorld | EnumActionBasic | None = self.uiWorld.actions.get(event.ui_element)
                if(actionWorld == None):
                    print("Action does not point to any world input")
                    return

                inputFunc = self.inputWorld.inputs.get(actionWorld)

            if inputFunc == None:
                print("ui input does not exists")
                return

            inputFunc.func()







