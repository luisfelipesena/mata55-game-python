import pyglet
from classes.paddle import Paddle
from utils import Utils


class Ball:
    def __init__(self, paddle, score, menu):
        utils = Utils()
        self._paddle = paddle
        self._score = score
        self._menu = menu

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

    def draw(self):
        self.ball.draw()

    @property
    def visible(self):
        return self.ball.visible

    @visible.setter
    def visible(self, bool):
        self.ball.visible = bool

    def moviment(self):
        self.ball.x = self.ball.x + self.dx
        self.ball.y = self.ball.y + self.dy

    # resetar a bola
    def reset(self, window):
        self.ball.x = self._base_x
        self.ball.y = self._base_y
        self.dx = -self._base_velocity
        self.dy = -self._base_velocity

        self._paddle._can_update = False
        self._score._can_update = False
        self._menu.visible = True
        self._menu.restart_menu_buttons.visible = True
        window.show_restart = True

    # Movimento da bola - Alterar velocidade conforme o score
    def update(self, window):
        if self.ball.visible == True and window.show_restart == False:
            self.moviment()

            if self.ball.x < 20 or self.ball.x > 780:
                self.dx = -self.dx
            elif self.ball.y > 580:
                self.dy = -self.dy

            # Colisão com a raquete
            if self.ball.x > self._paddle.x and self.ball.x < self._paddle.x + self._paddle.width and self.ball.y <= 20 and self.ball.y >= 10:
                self.dy = -self.dy
                self._score.score_count += 1
                self.dy *= 1.10
                self.dx *= 1.10
            elif self.ball.y < 10:
                self.reset(window)
