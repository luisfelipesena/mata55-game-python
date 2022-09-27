import pyglet

class Score:
    def __init__(self, x, y):   
        self._score = pyglet.text.Label("Score: {}".format(0), font_name="Arial", font_size=15, x=x, y=y, anchor_x="center", anchor_y="center")
        self.score_count = 0;
        self._score.visible = False  
      
    def draw(self):
        self._score.draw()

    @property
    def visible(self):
        return self._score.visible
    @visible.setter
    def visible(self, bool):
        self._score.visible = bool

    def update(self):
        pass
