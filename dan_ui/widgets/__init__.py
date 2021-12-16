from abc import ABC, abstractmethod
from typing import Iterable, Union
from ..common import Rect, Point, DrawRect

class Childed:
    def __init__(self,*, child: 'Widget') -> None:
        self.child = child
        super().__init__()

class Childrened:
    def __init__(self,*, children: Iterable['Widget']) -> None:
        self.children = children
        super().__init__()
    

class Widget(ABC):
    @abstractmethod
    def render(self, rect: DrawRect):
        ...

    