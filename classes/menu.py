import pyglet
from classes.menuButtons import MenuButtons

class Menu:
    def __init__(self, menu_x,menu_y, window_width, window_height):
        self.menu = pyglet.text.Label("One Player Pong", font_name="Arial", font_size=36, x=menu_x,y=menu_y, anchor_x="center", anchor_y="center")
        self.menu.visible = True
        # Menu buttons - Botões do Menu
        menu_start_x = (window_width / 2)
        menu_start_y = (window_height / 2) - 80
        menu_exit_x = (window_width / 2)
        menu_exit_y = (window_height / 2) - 130
        self.menu_buttons = MenuButtons(menu_start_x, menu_start_y, menu_exit_x, menu_exit_y)
  
    def draw(self):
        self.menu.draw()
        self.menu_buttons.draw()

    def update(self, up_arrow_pressed, down_arrow_pressed, enter_pressed):
      self.menu_buttons.update(self.menu.visible, up_arrow_pressed, down_arrow_pressed, enter_pressed)
