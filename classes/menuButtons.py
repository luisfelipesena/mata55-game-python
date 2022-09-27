import pyglet

class MenuButtons:
    def __init__(self, start_x, start_y, exit_x, exit_y):
        self.start = pyglet.text.Label("Iniciar", font_name="Arial", font_size=24, x=start_x,
                                         y=start_y, anchor_x="center", anchor_y="center")
        self.exit = pyglet.text.Label("Sair", font_name="Arial", font_size=24, x=exit_x,
                                        y=exit_y, anchor_x="center", anchor_y="center")

        self.selected = 0
        self.menu_items = [self.start, self.exit]
        self.menu_items[self.selected].color = (255, 0, 0, 255)

    def draw(self):
        self.start.draw()
        self.exit.draw()

    def onEnter(self):
      if self.selected == 0:
        self.start.visible = False
        self.exit.visible = False
        
        pass
      else:
        pyglet.app.exit()

    def update(self, menu_visible,up_arrow_pressed, down_arrow_pressed, enter_pressed):
      self.menu_items[self.selected].color = (255, 255, 255, 255)
      if up_arrow_pressed:
        self.selected -= 1;
      if down_arrow_pressed:
        print(self.selected)
        self.selected += 1;
      if enter_pressed:
        self.onEnter()
      self.menu_items[self.selected].color = (255, 0, 0, 255)