
from typing import Dict, List
import pygame
from pygame import Event
from pygame_gui import UIManager

from core.gameState import GameState
from enums.enumScene import EnumScene
from init.coreRegistry import CoreRegistry
from init.renderRegistry import RenderRegistry
from inputs.inputFunction import InputFunction
from inputs.inputRegistry import InputRegistry
from ui.uiRegistry import UIRegistry


class EventHandler:

    def __init__(self, gameState: GameState, uiManager: UIManager, inputRegistry: InputRegistry):
        self.gameState: GameState = gameState 
        self.uimanager: UIManager = uiManager
        self.inputRegistry = inputRegistry

    def processEvent(self, events: List[Event]):
        for event in events:
            if event.type == pygame.QUIT:
                print("quit")
                self.isRunning = False

            print("currentScene: ", self.gameState.currentScene)

            self.eventInput(event)
            self.uimanager.process_events(event)

    def eventInput(self, event): 
        inputFunc: InputFunction | None
        if event.type == pygame.KEYDOWN:
            if self.gameState.currentScene == EnumScene.MENU: 
                inputFunc = self.inputRegistry.menuInputs.get(event.key)
    
            elif self.gameState.currentScene == EnumScene.WORLD:
                inputFunc = self.inputRegistry.menuInputs.get(event.key)

        if inputFunc == None:
            print("key does not exists")
            return
        inputFunc.func()




