from . import Widget
from ..common import DrawRect, Point

class Label(Widget):
    def __init__(self, text='') -> None:
        self.text = text

    def render(self, rect: DrawRect):

        rect.textout(Point(0,0), self.text)