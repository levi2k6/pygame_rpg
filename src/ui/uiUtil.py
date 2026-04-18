


from typing import List
from pygame_gui.core import IContainerLikeInterface, UIElement


class UIUtil:

    def __init__(self):

        pass

    def addUiToPanel(self, uiContainer: IContainerLikeInterface, uis: List[UIElement]): 
        for ui in uis:
            ui.set_container(uiContainer)

