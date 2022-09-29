import pyglet
from utils import Utils


class Score:
    def __init__(self):
        utils = Utils()
        score_x = utils.walls_padding + 50
        score_y = utils.window_height - (utils.walls_padding * 2)
        self._score = pyglet.text.Label(
            "Score: {}".format(0),
            font_name="Arial",
            font_size=15,
            x=score_x,
            y=score_y,
            anchor_x="center",
            anchor_y="center",
        )
        self.score_count = 0
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
