import pyglet
from utils import Utils

utils = Utils()

def getLabel(label, x, y):
    return pyglet.text.Label(
        "Score: {}".format(label),
        font_name="Arial",
        font_size=15,
        x=x,
        y=y,
        anchor_x="center",
        anchor_y="center",
    )

class Score:
    def __init__(self):
        score_x = utils.walls_padding + 50
        self.score_count = 0
        score_y = utils.window_height - (utils.walls_padding * 2)
        self._score = getLabel(self.score_count, score_x, score_y)
        self._score.visible = False

        self.can_update = False

    def draw(self):
        self._score.draw()

    @property
    def visible(self):
        return self._score.visible

    @visible.setter
    def visible(self, bool):
        self._score.visible = bool
      
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, scr):
        self._score = scr

    def update(self, dt):
        if self.can_update:
            oldX = len(str(self.score_count))
            self.score_count += int(dt)
            newX = len(str(self.score_count))
          
            if oldX != newX:
              self.score = getLabel(self.score_count, newX + self.score.x,self.score.y)
            else:
              self.score = getLabel(self.score_count, self.score.x ,self.score.y)
        
    
