import pyglet
from utils import Utils

utils = Utils()


class Score:
    def __init__(self):
        score_x = utils.walls_padding + 50
        self._score_count = 0
        score_y = utils.window_height - (utils.walls_padding * 2)
        self._score = self.createLabel(self._score_count, score_x, score_y)

        self._score.visible = False
        self._can_update = False

    def draw(self):
        self._score.draw()

    @classmethod
    def createLabel(self, label, x, y):
        return pyglet.text.Label(
            "Score: {}".format(label),
            font_name="Arial",
            font_size=15,
            x=x,
            y=y,
            anchor_x="center",
            anchor_y="center",
        )

    @property
    def visible(self):
        return self._score.visible

    @visible.setter
    def visible(self, bool):
        self._score.visible = bool

    @property
    def score_count(self):
        return self._score_count

    @score_count.setter
    def score_count(self, num):
        self._score_count = num
        self._score.text = "Score: {}".format(self._score_count)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, scr):
        self._score = scr

    def __repr__(self):
        return f'Score: {self.score_count}'
