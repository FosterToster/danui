from dan_ui.screen import Screen
from dan_ui.widgets.label import Label
from dan_ui.widgets.layouts.panel import Panel
from dan_ui.widgets.layouts.tiles import Cols, Rows

from dan_ui.widgets import Widget, DrawRect, Point

class Diagonal(Widget):
    def render(self, rect: DrawRect):
        rect.line(Point(1,1), rect.size)


class Loader(Label):
    def render(self, rect: DrawRect):
        states = [
            
            '▓         ',
            '▒▓        ',
            '▒▒▓       ',
            '░▒▒▓      ',
            ' ░▒▒▓     ',
            '  ░▒▒▓    ',
            '   ░▒▒▓   ',
            '    ░▒▒▓  ',
            '     ░▒▒▓ ',
            '      ░▒▒▓',
            '       ░▒▓',
            '        ░▓',
            '         ▓',
            '        ▓▒',
            '       ▓▒▒',
            '      ▓▒▒░',
            '     ▓▒▒░ ',
            '    ▓▒▒░  ',
            '   ▓▒▒░   ',
            '  ▓▒▒░    ',
            ' ▓▒▒░     ',
            '▓▒▒░      ',
            '▓▒░       ',
            '▓░        ',
        ]

        self.text = states[rect.life % len(states)]

        rect.textout(Point(
            x=rect.size.x // 2 - len(self.text) // 2,
            y=rect.size.y // 2,
            
        ),
        self.text)


def main():
    # screen = Screen(Diagonal())
    screen = Screen(
        Cols(children=[
            Rows(
                children=[
                    Panel(child=Loader("Hello, world!")),
                    Panel(child=Label("Hello,\n world!")),
                    Panel(child=Label("Hello, super long string world!")),
                    Panel(child=Label("Hello, world!")),
                ]
            ),
            Rows(
                children=[
                    Panel(child=Label("Hello, world!")),
                    Panel(child=Label("Hello, world!")),
                ]
            ),
            Rows(
                children=[
                    Panel(child=Label("Hello, world!")),
                    Panel(child=Label("Hello, world!")),
                    Panel(child=Label("Hello, world!")),
                    Panel(child=Label("Hello, world!")),
                ]
            )            
        ])
        
    )

    while True:
        screen()

if __name__ == '__main__':
    main()