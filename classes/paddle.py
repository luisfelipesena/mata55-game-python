import pyglet
from pyglet.window import key
from utils import Utils

utils = Utils()


class Paddle:
    def __init__(self):
        paddle_width = utils.window_width / 10
        paddle_height = 10
        paddle_x = (utils.window_width / 2) - (paddle_width / 2)
        paddle_y = 5
        self._paddle = pyglet.shapes.Rectangle(paddle_x,
                                               paddle_y,
                                               paddle_width,
                                               paddle_height,
                                               color=(255, 0, 0))
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

    @property
    def width(self):
        return self._paddle.width

    def update(self, window):
        nextPlusX = self.x + 10
        nextMinusX = self.x - 10

        if window.show_restart == True:
            return

        # move paddle to the right if the right arrow key is pressed and the paddle is not going to go out of the window to the right
        if self.keys_handler[key.RIGHT] and nextPlusX + self.width < utils.window_width:
            self.x = nextPlusX
        # move paddle to the left if the left arrow key is pressed and the paddle is not going to go out of the window to the left
        if self.keys_handler[key.LEFT] and nextMinusX > 0:
            self.x = nextMinusX

    def draw(self):
        self._paddle.draw()
