import pyglet
from classes.paddle import Paddle
from utils import Utils


class Ball:
    def __init__(self, paddle, score):
        utils = Utils()
        self._paddle = paddle
        self._score = score

        # Valores base da bola
        self._base_x = (utils.window_width / 2) - (5)
        self._base_y = utils.window_height - (utils.walls_padding * 2)
        self._base_velocity = 4.0

        self.ball_x = self._base_x
        self.ball_y = self._base_y
        self.ball = pyglet.shapes.Circle(self.ball_x,
                                         self.ball_y,
                                         10,
                                         color=(255, 255, 255))
        self.ball.visible = False

        self.dx = -self._base_velocity
        self.dy = -self._base_velocity

        self._is_reseted = False

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

    # resetar a bola
    def reset(self):
        self.ball.x = self._base_x
        self.ball.y = self._base_y
        self.dx = -2.0
        self.dy = -2.0
        self._is_reseted = True

    # Movimento da bola - Alterar velocidade conforme o score
    def update(self, dt):
        if self.ball.visible == True and self._is_reseted == False:
            self.moviment()

            if self.ball.x < 20 or self.ball.x > 780:
                self.dx = -self.dx
            elif self.ball.y > 580:
                self.dy = -self.dy

            # Colisão com a raquete
            if self.ball.x > self._paddle.x and self.ball.x < self._paddle.x + self._paddle.width and self.ball.y <= 20 and self.ball.y >= 10:
                self.dy = -self.dy
                self._score.score_count += 1
                self.dy *= 1.05
                self.dx *= 1.05
            elif self.ball.y < 10:
                self.reset()
