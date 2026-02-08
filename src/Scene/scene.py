from typing import List
from pygame import Surface

from Prop.prop import Prop 

class Scene:
    backgrounds: List[Surface] = []
    props: List[Prop] = []
