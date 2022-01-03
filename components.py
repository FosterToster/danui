from dan_ui.widgets import AnimatedWidget
from dan_ui.widgets.label import Label
    
class Loader(Label, AnimatedWidget):
    def __init__(self) -> None:
        self.frames = [
            
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
        super().__init__(self.frames[0])

    def update(self):
        super().update()
        self.text = self.frames[self.animation_stage % len(self.frames)]


class ConnectionStatus(Loader):
    def __init__(self) -> None:
        self.frames = [
            '| Connecting',
            '/ Connecting.',
            '- Connecting..',
            '\ Connecting...',
        ]