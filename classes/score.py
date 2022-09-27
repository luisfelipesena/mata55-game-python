import pyglet

class Score:
    def __init__(self, x, y, width, height):
        self.score = pyglet.shapes.Rectangle(x, y, width, height, color=(0, 0, 0))
        self.score.visible = False
        self.score_count = 0;
        self.score_label = pyglet.text.Label("Score: {}".format(self.score_count), font_name="Arial", font_size=15, x=50, y=580, anchor_x="center", anchor_y="center")


    def draw(self):
        self.score.draw()
        self.score_label.draw()

    @property
    def visible(self):
      return self._paddle.visible
    @visible.setter
    def visible(self, bool):
        self._paddle.visible = bool

    def update(self):
        pass