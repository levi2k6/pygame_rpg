
from typing import List
from pygame import Event
from pygame_gui import UIManager

from Initialization.display import Display


class RendererUI:
    def __init__(self, uiManager: UIManager):
        self.uiManager = uiManager

    def renderUi(self, uiManager: UIManager, event: Event | None,  display: Display, delta: float):
        if event:
            uiManager.process_events(event)

        uiManager.update(delta)
        uiManager.draw_ui(display.screen)


    def render

        














