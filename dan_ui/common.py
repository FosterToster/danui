from dataclasses import dataclass
from typing import Generator, Iterable, List, Tuple, Union
from math import sqrt

@dataclass
class Point:
    x: int
    y: int

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Point') -> 'Point':
        return Point(
            x=self.x+other.x,
            y=self.y+other.y
        )

    def distance(self, to: 'Point'):
        if self < to:
            raise CantContainException('To point is less than from point')
        
        return round(sqrt((to.x - self.x)^2 + (to.y - self.y)^2))

    def clone(self) -> 'Point':
        return Point(self.x, self.y)

@dataclass
class Rect:
    ul: Point
    br: Point

    @property
    def width(self):
        return self.br.x - self.ul.x

    @property
    def height(self):
        return self.br.y - self.ul.y

    def contain(self, other: 'Rect'):
        return self.ul <= other.ul and self.br >= other.br



class DrawRectException(Exception):
    ...

class CantContainException(DrawRectException):
    ...

class DrawRect:
    def __init__(self, screen: List[List[str]], offset: Point, size: Point, *, life=0) -> None:
        self.screen = screen
        self.offset: Point = offset
        self.size = size
        self.life = life

    def child(self, offset: Point, size: Point) -> 'DrawRect':
        if not Rect(ul=self.offset, br=self.size).contain(Rect(ul=self.offset+offset, br=size)):
            raise CantContainException('Child rect does not fit to parent')
        
        return DrawRect(self.screen, self.offset+offset, size, life=self.life)

    def draw_rect(self, rect: Rect, *, pen:str = "*"):
        self.line(rect.ul, Point(rect.br.x, 0), pen=pen) # upper
        self.line(rect.ul, Point(0, rect.br.y), pen=pen) # left
        self.line(Point(rect.ul.x, rect.br.y), rect.br, pen=pen) # bottom
        self.line(Point(rect.br.x, rect.ul.y), rect.br, pen=pen) # right

    @staticmethod
    def line_generator(from_: Point, to: Point):
        point:Point = from_.clone()
        x_distance = to.x - from_.x
        y_distance = to.y - from_.y
        steps = max(x_distance, y_distance)

        for step in range(steps):
            yield Point(
                x=from_.x + round(min(step / steps * x_distance, x_distance)),
                y=from_.y + round(min(step / steps * y_distance, y_distance))
            )
            
        yield to
        
    def line(self, from_: Point, to: Point, *, pen="*"):
        for point in self.line_generator(from_, to):
            self.set(point, pen)

    def set(self, where:Point, what:str):
        if (where.x > self.size.x):
            where.x = self.size.x
        elif where.x < 0:
            where.x = 0

        if (where.y > self.size.y):
            where.y = self.size.y
        elif where.y < 0:
            where.y = 0

        end_x = where.x+self.offset.x
        end_y = where.y+self.offset.y

        
       
        if end_y >= len(self.screen):
            end_y = len(self.screen) - 1
        elif end_y < 0:
            end_y = 0

        if end_x >= len(self.screen[0]):
            end_x = len(self.screen[0])-1
        
        elif end_x < 0:
            end_x = 0

        self.screen[end_y][end_x] = what

    def textout(self, where: Point, text:str):
        x = where.x
        y = where.y
        for char in text:
            if char == '\n':
                y += 1
                x = where.x
                continue
        
            if x > self.size.x:
                self.set(Point(self.size.x, y), '>')
                break
            if x < 0:
                self.set(Point(0, y), '<')
                break

            if y < 0 or y > self.size.y:
                break

            self.set(Point(x, y), char)
            x += 1
