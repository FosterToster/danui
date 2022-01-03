from abc import ABC, abstractmethod
from typing import Iterable, Union
from ..common import Rect, Point, DrawRect

class Childed:
    focused_child = None

    def __init__(self,*, child: 'Widget') -> None:
        self.child = child
        super().__init__()

    def focus(self):
        if self.child.focus():
            self.focused_child = self.child
            return True
        else:
            self.focused_child = None
            return False

    def update(self):
        self.child.update()

class Childrened(Childed):
    focused_child_index = None
    
    def __init__(self,*, children: Iterable['Widget']) -> None:
        self.children: Iterable['Widget'] = children

    def update(self):
        for child in self.children:
            child.update()

    def focus(self):
        for i, child in enumerate(self.children):
            if not child.focused:
                if self.focused_child_index is None or i == self.focused_child_index + 1:
                    if child.focus():
                        self.focused_child_index = i
                        self.focused_child = child
                        return True
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            self.focused_child_index = None
            self.focused_child = None
            return False

class Widget(ABC):

    focused = False

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def render(self, rect: DrawRect):
        ...

    def blur(self) -> bool: # True if BLUR is consumed
        if self.focused == True:
            self.focused = False
            return True
        else:
            return False
        
    def focus(self) -> bool: # returns if FOCUS is consumed
        if self.focused == True:
            self.focused = False
        else:
            self.focused = True

        return self.focused


class AnimatedWidget(Widget):
    animation_stage = 0

    def update(self):
        self.animation_stage = self.animation_stage + 1