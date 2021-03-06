from . import Widget, DrawRect, Rect, Point
from .. import Childrened

class Cols(Childrened, Widget):
    def render(self, rect: DrawRect):
        for num, child in enumerate(self.children):
            new_rect = rect.child(
                offset=Point(
                    x=num * round(rect.size.x/len(self.children)),
                    y=0
                ),
                size=Point(
                    x=round(rect.size.x / len(self.children)) if num != (len(self.children) - 1) else rect.size.x - num * round(rect.size.x/len(self.children)),
                    y=rect.size.y
                )
            )
            child.render(new_rect)


class Rows(Childrened, Widget):
    def render(self, rect: DrawRect):
        for num, child in enumerate(self.children):
            new_rect = rect.child(
                offset=Point(
                    x=0,
                    y=num * round(rect.size.y / len(self.children))
                ),
                size=Point(
                    x=rect.size.x,
                    y=round(rect.size.y/len(self.children)) if num != len(self.children) - 1 else rect.size.y - num * round(rect.size.y / len(self.children))
                )
            )
            child.render(new_rect)
