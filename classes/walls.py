import pyglet
from pyglet import shapes
from utils import Utils


class Walls():
    def __init__(self):
        utils = Utils()
        self._wall_left = shapes.Line(0,
                                      0,
                                      0,
                                      utils.window_height,
                                      utils.walls_padding,
                                      color=(255, 255, 255))
        self._wall_right = shapes.Line(utils.window_width,
                                       0,
                                       utils.window_width,
                                       utils.window_height,
                                       utils.walls_padding,
                                       color=(255, 255, 255))
        self._wall_top = shapes.Line(0,
                                     utils.window_height,
                                     utils.window_width,
                                     utils.window_height,
                                     utils.walls_padding,
                                     color=(255, 255, 255))

    def draw(self):
        self._wall_left.draw()
        self._wall_right.draw()
        self._wall_top.draw()
