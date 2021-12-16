from dan_ui.screen import Screen
from dan_ui.widgets.label import Label
from dan_ui.widgets.layouts.panel import Panel
from dan_ui.widgets.layouts.tiles import Cols, Rows

from dan_ui.widgets import Widget, DrawRect, Point

class Diagonal(Widget):
    def render(self, rect: DrawRect):
        rect.line(Point(1,1), rect.size)



def main():
    # screen = Screen(Diagonal())
    screen = Screen(
        Cols(children=[
            Rows(
                children=[
                    Panel(child=Label("Hello, world!")),
                    Panel(child=Label("Hello, world!")),
                    Panel(child=Label("Hello, world!")),
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