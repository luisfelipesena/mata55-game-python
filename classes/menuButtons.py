import pyglet


class MenuButtons:
    def __init__(self, start_x, start_y, exit_x, exit_y):
        self.start = pyglet.text.Label(
            "Iniciar",
            font_name="Arial",
            font_size=24,
            x=start_x,
            y=start_y,
            anchor_x="center",
            anchor_y="center",
        )
        self.exit = pyglet.text.Label(
            "Sair",
            font_name="Arial",
            font_size=24,
            x=exit_x,
            y=exit_y,
            anchor_x="center",
            anchor_y="center",
        )

        self.selected = 0
        self.menu_items = [self.start, self.exit]
        self.menu_items[self.selected].color = (255, 0, 0, 255)

    def draw(self):
        self.start.draw()
        self.exit.draw()

    @property
    def visible(self):
        return self.start.visible and self.exit.visible

    @visible.setter
    def visible(self, bool):
        self.start.visible = bool
        self.exit.visible = bool

    def onEnter(self):
        if self.selected == 0:
            self.visible = False
        else:
            pyglet.app.exit()

    def inclui_ponto(self, x, y):
        # Ajustes para incluir label - talvez seja melhor rever lógica
        if self.start.visible and self.exit.visible:
            start = (x + 40 >= self.start.x
                     and x + 50 <= self.start.x + self.start.content_width
                     and y + 10 >= self.start.y
                     and y + 10 <= self.start.y + self.start.content_height)

            end = (x + 40 >= self.exit.x
                   and x + 30 <= self.exit.x + self.exit.content_width
                   and y + 10 >= self.exit.y
                   and y + 10 <= self.exit.y + self.exit.content_height)

            if start:
                return "start"
            elif end:
                return "exit"
            else:
                return None

    def update(self, window):
        self.menu_items[self.selected].color = (255, 255, 255, 255)
        if window.up_arrow_pressed:
            newSelected = self.selected - 1
            if newSelected >= 0 and newSelected < len(self.menu_items):
                self.selected = newSelected
            else:
                self.selected = len(self.menu_items) - 1

        if window.down_arrow_pressed:
            newSelected = self.selected + 1
            if newSelected >= 0 and newSelected < len(self.menu_items):
                self.selected = newSelected
            else:
                self.selected = 0

        if window.enter_pressed:
            self.onEnter()

        self.menu_items[self.selected].color = (255, 0, 0, 255)
