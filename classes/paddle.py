import pyglet
from pyglet.window import key
from utils import Utils


class Paddle:
    def __init__(self):
        utils = Utils()
        paddle_width = utils.window_width / 10
        paddle_height = 10
        paddle_x = (utils.window_width / 2) - (paddle_width / 2)
        paddle_y = 5
        self._paddle = pyglet.shapes.Rectangle(
            paddle_x, paddle_y, paddle_width, paddle_height, color=(255, 0, 0)
        )
        self._paddle.visible = False

        self.keys_handler = key.KeyStateHandler()

    @property
    def x(self):
        return self._paddle.x

    @x.setter
    def x(self, nx):
        self._paddle.x = nx

    @property
    def visible(self):
        return self._paddle.visible

    @visible.setter
    def visible(self, bool):
        self._paddle.visible = bool

    def update(self):
        if self.keys_handler[key.RIGHT]:
            self._paddle.x = self.x + 10
        elif self.keys_handler[key.LEFT]:
            self._paddle.x = self.x - 10

    def draw(self):
        self._paddle.draw()
