import pyglet
import random
from typing import Tuple
from utils import Utils


class Ball:
    def __init__(self):
        utils = Utils()
        ball_width = 10
        ball_x = (utils.window_width / 2) - (ball_width / 2)
        ball_y = utils.window_height - (utils.walls_padding * 2)
        self._ball = pyglet.shapes.Circle(
            ball_x, ball_y, ball_width, color=(255, 255, 255)
        )
        self._ball.visible = False

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.color = (255, 180, 0)

    def draw(self):
        self._ball.draw()

    @property
    def visible(self):
        return self._ball.visible

    @visible.setter
    def visible(self, bool):
        self._ball.visible = bool

    @property
    def x(self):
        return self._ball.x

    @x.setter
    def x(self, value):
        self._ball.x = value

    @property
    def y(self):
        return self._ball.y

    @y.setter
    def y(self, value):
        self._ball.y = value

    # WIP - Entender Lógica
    def update(self, win_size: Tuple, border: Tuple, other_object, dt):
        speed = [
            2.37,
            2.49,
            2.54,
            2.62,
            2.71,
            2.85,
            2.96,
            3.08,
            3.17,
            3.25,
        ]  # more choices more randomness
        rn = random.choice(speed)
        newx = self.x + self.velocity_x
        newy = self.y + self.velocity_y
        # Entender essa lógica
        if newx < border + self.radius or newx > win_size[0] - border - self.radius:
            self.velocity_x = -(self.velocity_x / abs(self.velocity_x)) * rn
        elif newy > win_size[1] - border - self.radius:
            self.velocity_y = -(self.velocity_y / abs(self.velocity_y)) * rn
        elif (newy - self.radius < other_object.height) and (
            other_object.x <= newx <= other_object.rightx
        ):
            self.velocity_y = -(self.velocity_y / abs(self.velocity_y)) * rn
        else:
            self.x = newx
            self.y = newy
