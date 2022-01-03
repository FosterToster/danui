from dan_ui.screen import Screen
from dan_ui.widgets.label import Label
from dan_ui.widgets.layouts.panel import Panel
from dan_ui.widgets.layouts.tiles import Cols, Rows

from dan_ui.widgets import Widget, DrawRect, Point

from layoits import Main, SidebaredMain, List, ActiveChat, TextInput, Messages
from components import ConnectionStatus, Loader


class Dot(Widget):
    def update(self):
        ...

    def render(self, rect: DrawRect):
        rect.set(Point(0,0), '0')
        rect.set(rect.size, '0')

def main():
    screen = Screen(Main(
        header=ConnectionStatus(),
        main=SidebaredMain(
            List(),
            ActiveChat(Messages(), TextInput()),
        ),
        footer=Loader(),
    ), frame_time=0.1)

    while True:
        screen()

if __name__ == '__main__':
    main()