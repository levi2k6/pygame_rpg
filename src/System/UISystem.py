# import os
# import pygame
# import pygame_gui
# from Initialization import Display
# from pygame_gui.elements import UIPanel 
# from System import UISystem
#
# ASSETS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'assets'))
# THEME_PATH = os.path.join(ASSETS_PATH, 'theme.json')
#
# UIManager = pygame_gui.UIManager((Display.width, Display.height), THEME_PATH)
# def checkEventUI(event):
#     UIManager.process_events(event)
#
#
# def drawUI(time_delta):
#     UIManager.update(time_delta)
#     UIManager.draw_ui(Display.screen)
#
#
# def createPanel(position: tuple, size: tuple):
#     panel = pygame_gui.elements.UIPanel(
#         relativeRect = pygame.Rect(position, size),
#         layerHeight = 1,
#         manager = UISystem.UIManager
#     )
#     return panel
#
# def createLabel(position: tuple, size: tuple, text: str, panel: UIPanel): 
#     label = pygame_gui.elements.UILabel(
#         relativeRect = pygame.Rect(position, size),
#         labelText = text,
#         manager = UISystem.UIManager,
#         container = panel
#     )
#     return label
