from classes.ball import Ball
import pyglet
from utils import Utils
from classes.menuButtons import MenuButtons
from classes.restartMenuButtons import RestartMenuButtons

utils = Utils()


class Menu:
    def __init__(self):
        menu_x = utils.window_width / 2
        menu_y = utils.window_height / 2
        self.menu = pyglet.text.Label(
            "One Player Pong",
            font_name="Arial",
            font_size=36,
            x=menu_x,
            y=menu_y,
            anchor_x="center",
            anchor_y="center",
        )
        self.menu.visible = True
        # Menu buttons - Botões do Menu
        menu_start_x = utils.window_width / 2
        menu_start_y = (utils.window_height / 2) - 80
        menu_exit_x = utils.window_width / 2
        menu_exit_y = (utils.window_height / 2) - 130
        self.menu_buttons = MenuButtons(
            menu_start_x, menu_start_y, menu_exit_x, menu_exit_y
        )
        self.restart_menu_buttons = RestartMenuButtons(Ball, 
            menu_start_x, menu_start_y, menu_exit_x, menu_exit_y
        )

    @property
    def visible(self):
        return self.menu.visible

    @visible.setter
    def visible(self, bool):
        self.menu.visible = bool

    def draw(self):
        self.menu.draw()
        self.menu_buttons.draw()
        self.restart_menu_buttons.draw()

    def update(self, window):
        self.menu_buttons.update(window)
        self.restart_menu_buttons.update(window)

        if window.enter_pressed:
            self.menu.visible = False
            self.menu_buttons.visible = False
            self.restart_menu_buttons.visible = False
