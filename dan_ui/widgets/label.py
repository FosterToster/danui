from . import Widget
from ..common import DrawRect, Point

class Label(Widget):
    def __init__(self, text='') -> None:
        self.text = text

    def render(self, rect: DrawRect):
        if rect.life < 128:
            y = round(rect.life * ((rect.size.y - 1) / 128))
        else:
            y = rect.size.y - round((rect.life-128) * ((rect.size.y) / 128)) - 1

        
        if y < 0:
            y = 0
        if y > rect.size.y - 1:
            y = rect.size.y - 1
        rect.textout(Point(0,y), self.text)