import pyglet
from pyglet import shapes

class Walls():
    def __init__(self, windowWidth, windowHeight,walls_padding):
        self._wall_left = shapes.Line(0, 0, 0, windowHeight, walls_padding, color=(255, 255, 255))
        self._wall_right =  shapes.Line(windowWidth, 0, windowWidth, windowHeight, walls_padding, color=(255, 255, 255))
        self._wall_top = shapes.Line(0, windowHeight, windowWidth, windowHeight, walls_padding, color=(255, 255, 255))

    def draw(self):
        self._wall_left.draw()
        self._wall_right.draw()
        self._wall_top.draw()