from .. import Widget, DrawRect, Rect, Point, Childed

class Panel(Widget, Childed):
    def update(self):
        return super().update()

    def render(self, rect: DrawRect):
        rect.draw_rect(Rect(
            ul=Point(0,0),
            br=rect.size
        ), pen="█")

        self.child.render(rect.child(offset=Point(1,1), size=Point(rect.size.x-2, rect.size.y-2)))
        