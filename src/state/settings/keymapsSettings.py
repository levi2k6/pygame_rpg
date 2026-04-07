
import pygame

from enums.enumActionBasic import EnumActionBasic

class KeymapsSettings: 
    customKeymaps = {}

    defaultKeymaps = {
            pygame.K_w: EnumActionBasic.UP, 
            pygame.K_a: EnumActionBasic.LEFT,
            pygame.K_s: EnumActionBasic.DOWN,
            pygame.K_d: EnumActionBasic.RIGHT,
            pygame.K_j: EnumActionBasic.OK,
            pygame.K_k: EnumActionBasic.NO,
    }

    pass



