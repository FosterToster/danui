from .widgets import Widget
from .common import Rect, Point, DrawRect
import os
import sys
from time import sleep
from datetime import datetime




class Screen(Widget):
    def __init__(self, widget: Widget, frame_time) -> None:
        self.widget = widget
        self.life = 0
        self.frame_time = frame_time
        
    def update(self):
        self.widget.update()

    def draw(self):
        screen_array = ''
        for line in self.screen:
            for char in line:
                screen_array += char

        sys.stdout.write('\n'+screen_array)
        # sys.stdout.flush()

    def render(self):
        self.life += 1
        if self.life == 10000:
            self.life = 0

        term = os.get_terminal_size()
        self.screen = list(list(' '*term.columns) for _ in range(term.lines-1))
        self.widget.render(
            DrawRect(
                screen=self.screen,
                offset=Point(0,0),
                size=Point(term.columns-1, term.lines-2),
                life=self.life
            )
        )
        
    
    def __call__(self, *args, **kwds):
        self.update()
        self.render()
        self.draw()
        sleep(.1)