from typing import Dict, List
from pygame_gui.core import IContainerLikeInterface, UIElement
from enums.enumScene import EnumScene
from init.stateRegistry import StateRegistry
from ui.uiRegistry import UIRegistry


class SimulationUi:
    def addUiToPanel(self, uiContainer: IContainerLikeInterface, uis: List[UIElement]): 
        for ui in uis:
            ui.set_container(uiContainer)



