
from types import FunctionType
from typing import Any, Callable


class InputFunction:

    def __init__(self, inputName: str, func: Callable[..., Any]):
        self.inputName: str = inputName
        self.func: FunctionType = func 

