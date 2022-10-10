import pyglet
from pyglet.window import mouse
from classes.menu import Menu
from classes.walls import Walls
from classes.paddle import Paddle
from classes.ball import Ball
from classes.score import Score
from utils import Utils


class MainWindow(pyglet.window.Window):
    def __init__(self):
        utils = Utils()
        super().__init__(
            utils.window_width,
            utils.window_height,
            utils.window_caption,
            resizable=False,
        )

        # Walls - Parede
        self.walls = Walls()
        # Paddle - Raquete
        self.paddle = Paddle()
        pyglet.clock.schedule_interval(self.paddle.update, 1 / utils.fps)
        # Ball - Bola
        self.ball = Ball()
        pyglet.clock.schedule_interval(self.ball.update, 1 / utils.fps)
        # Menu
        self.menu = Menu()
        pyglet.clock.schedule_interval(self.update_menu, 1 / (utils.fps / 10))
        # Score
        self.score = Score()
        pyglet.clock.schedule_interval(self.score.update, 1)
        # Teclas Pressionada
        self.right_arrow_pressed = False
        self.left_arrow_pressed = False
        self.up_arrow_pressed = False
        self.down_arrow_pressed = False
        self.enter_pressed = False
        self.on_ball_hit_bottom = False
        # Handlers
        self.mouse_handler = mouse.MouseStateHandler()

    def on_draw(self):
        self.clear()
        # Draw all classes from classes
        self.walls.draw()
        self.paddle.draw()
        self.ball.draw()
        self.menu.draw()
        self.score.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()
        if symbol == pyglet.window.key.RIGHT:
            self.right_arrow_pressed = True
        if symbol == pyglet.window.key.LEFT:
            self.left_arrow_pressed = True
        if symbol == pyglet.window.key.UP:
            self.up_arrow_pressed = True
        if symbol == pyglet.window.key.DOWN:
            self.down_arrow_pressed = True
        if symbol == pyglet.window.key.ENTER:
            self.enter_pressed = True
        if symbol == pyglet.window.key.K:
            self.on_ball_hit_bottom = True

    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.window.key.RIGHT:
            self.right_arrow_pressed = False
        if symbol == pyglet.window.key.LEFT:
            self.left_arrow_pressed = False
        if symbol == pyglet.window.key.UP:
            self.up_arrow_pressed = False
        if symbol == pyglet.window.key.DOWN:
            self.down_arrow_pressed = False
        if symbol == pyglet.window.key.ENTER:
            self.enter_pressed = False

    def on_mouse_press(self, x, y, button, modifiers):
        res = self.menu.menu_buttons.inclui_ponto(x, y)
        resRestart = self.menu.restart_menu_buttons.inclui_ponto(x, y)

        if res == "start" or resRestart == "start":
            self.on_ball_hit_bottom = False
            self.menu.visible = False
            self.menu.menu_buttons.start.visible = False
            self.menu.menu_buttons.exit.visible = False
            self.menu.restart_menu_buttons.start.visible = False
            self.menu.restart_menu_buttons.exit.visible = False
            self.score.visible = True
            self.paddle.visible = True
            self.ball.visible = True
        elif res == "exit" or resRestart == "exit":
            pyglet.app.exit()

    #  Será puxada para atualizar logicas do menu
    def update_menu(self, dt):
        self.menu.update(self)

        if self.on_ball_hit_bottom == True:
            self.paddle.can_update = False
            self.score.can_update = False

        if self.enter_pressed:
            self.paddle.visible = True
            self.paddle.can_update = True
            self.ball.visible = True
            self.score.visible = True
            self.score.can_update = True


if __name__ == "__main__":
    window = MainWindow()

    # Push handlers
    window.push_handlers(window.mouse_handler)
    window.push_handlers(window.paddle.keys_handler)

    pyglet.app.run()
