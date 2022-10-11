import pyglet
from classes.paddle import Paddle
from utils import Utils


class Ball:
    def __init__(self):
        utils = Utils()
        self.ball_x = (utils.window_width / 2) - (5)
        self.ball_y = utils.window_height - (utils.walls_padding * 2)
        self.ball = pyglet.shapes.Circle(self.ball_x,
                                         self.ball_y,
                                         10,
                                         color=(255, 255, 255))
        self.ball.visible = False
        self.dx = -2.0
        self.dy = -2.0

    def draw(self):
        self.ball.draw()

    @property
    def visible(self):
        return self.ball.visible

    @visible.setter
    def visible(self, bool):
        self.ball.visible = bool

    def moviment(self):
        self.ball_x = self.ball_x + self.dx
        self.ball.x = self.ball_x
        self.ball_y = self.ball_y + self.dy
        self.ball.y = self.ball_y

    #tentando implementar movimento da bola
    def update(self, dt):
        if self.ball.visible == True:
            self.moviment()
            if self.ball.x < 20 or self.ball.x > 780:
                self.dx = -self.dx
            elif self.ball.y > 580:
                self.dy = -self.dy
            elif self.ball.y < 10:
                self.ball.x = 400
                self.ball.y = 580

            #if self.ball.y == 20 and Paddle.x == self.ball.x:
                #self.dy = -self.dy