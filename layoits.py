from dan_ui.widgets import AnimatedWidget, Widget, DrawRect, Childrened
from dan_ui.common import Point
from dan_ui.widgets.label import Label
from dan_ui.widgets.layouts.panel import Panel

class SidebaredMain(Childrened, Widget):
    def __init__(self, sidebar: Widget, main: Widget) -> None:
        super().__init__(children=[sidebar, main])

    def draw_frame(self, rect: DrawRect):
        rect.line(rect.top_left, rect.top_right, pen='─')
        rect.line(rect.bottom_left, rect.bottom_right, pen='─')
        rect.line(rect.top_left, rect.bottom_left, pen='│')
        rect.line(rect.top_right, rect.bottom_right, pen='│')
        rect.set(rect.top_left, '┌')
        rect.set(rect.top_right, '┐')
        rect.set(rect.bottom_left, '└')
        rect.set(rect.bottom_right, '┘')

    def draw_merge(self, rect: DrawRect):
        rect.line(rect.top_right, rect.bottom_right, pen='║')
        rect.set(rect.top_right, '╥')
        rect.set(rect.bottom_right, '╨')

    def render(self, rect: DrawRect):
        sidebar = rect.child(offset=Point(0,0), size=Point(rect.size.x // 6, rect.size.y))
        self.draw_frame(sidebar)

        main = rect.child(offset=Point(sidebar.size.x, 0), size=Point(rect.size.x - sidebar.size.x, rect.size.y) )
        self.draw_frame(main)
        self.draw_merge(sidebar)

        self.children[0].render(sidebar.child(offset=Point(1,1), size=Point(sidebar.size.x-2, sidebar.size.y-2)))
        self.children[1].render(main.child(offset=Point(1,1), size=Point(main.size.x-2, main.size.y-2)))

class List(Childrened, Widget):
    def __init__(self) -> None:
        super().__init__(children=[])
        self.update()

    def update(self):
        self.children = list()
        for i in range(10):
            self.children.append(Label(text=f'#{i} Chat User named Jonh Doe'))

    def render(self, rect: DrawRect):
        for i, child in enumerate(self.children):
            child.render(rect.child(offset=Point(0, i), size=Point(rect.size.x, 1)))

class Message(Label):
    def __init__(self, user:str, text:str) -> None:
        super().__init__(text=text)
        self.user = user

    def draw_frame(self, rect: DrawRect):
        rect.line(rect.top_left, rect.top_right, pen='─')
        rect.line(rect.bottom_left, rect.bottom_right, pen='─')
        rect.line(rect.top_left, rect.bottom_left, pen='│')
        rect.line(rect.top_right, rect.bottom_right, pen='│')
        rect.set(rect.top_left, '┌')
        rect.set(rect.top_right, '┐')
        rect.set(rect.bottom_left, '└')
        rect.set(rect.bottom_right, '┘')

    def render(self, rect: DrawRect):
        self.draw_frame(rect)
        rect.textout(Point(1, 0), text=f"Message from: {self.user}")
        rect.textout(Point(1,1), text=self.text)

class Messages(List):
    def update(self):
        self.children = list()

        for i in range(4):
            self.children.append(Message('User #4', text=f"#{i} Just simple placeholder text to show"))

    def render(self, rect: DrawRect):
        for i, child in enumerate(self.children):
            child.render(rect.child(offset=Point(0, i*4), size=Point(rect.size.x, 3)))

class TextInput(AnimatedWidget, Label):
    def __init__(self) -> None:
        super().__init__(text='Hello, my dear friend!')
        self.caret = ''

    def update(self):
        super().update()
        self.caret = '▐' if (self.animation_stage % 4) in [0,1] else ''

    def render(self, rect: DrawRect):
        rect.textout(Point(0,0), self.text+self.caret)

class ActiveChat(Childrened, Widget):
    def __init__(self, messages:Widget, input: Widget) -> None:
        super().__init__(children=[messages, input])

    def focus(self):
        return self.children[1].focus()

    def blur(self) -> bool:
        return self.children[1].blur()

    def render(self, rect: DrawRect):
        messages = rect.child(offset=Point(0,0), size=Point(rect.size.x, (rect.size.y // 10) * 9))
        inp = rect.child(offset=Point(0, messages.size.y), size=Point(rect.size.x, rect.size.y-messages.size.y))
        inp.line(inp.top_left, inp.top_right, pen="═")

        self.children[0].render(messages)
        self.children[1].render(inp.child(offset=Point(0,1), size=Point(inp.size.x-1, inp.size.y-1)))


class Main(Childrened, Widget):
    def __init__(self, header: Widget, main: Widget, footer: Widget) -> None:

        super().__init__(children=[header, main, footer])
    
    def focus(self) -> bool:
        return self.children[1].focus()

    def blur(self) -> bool:
        return self.children[1].blur()

    def render(self, rect: DrawRect):
        header = rect.child(offset=Point(0,0), size=Point(rect.size.x, 1))
        footer = rect.child(offset=Point(0,rect.size.y), size=Point(rect.size.x, 1))
        main = rect.child(offset=Point(0,1), size=Point(rect.size.x, rect.size.y - 2))

        self.children[0].render(header)
        self.children[1].render(main)
        self.children[2].render(footer)

    