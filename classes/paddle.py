import pyglet
from pyglet.window import key

class Paddle():
  def __init__(self, x, y, width, height):
    self._paddle = pyglet.shapes.Rectangle(x, y, width, height, color = (255, 0, 0))
    self._paddle.visible = False
    
    self.keys_handler = key.KeyStateHandler()

  @property
  def x(self):
      return self._paddle.x
  @x.setter
  def x(self, nx):
      self._paddle.x = nx
    
  @property
  def visible(self):
      return self._paddle.visible
  @visible.setter
  def visible(self, bool):
      self._paddle.visible = bool

  def update(self):
    if self.keys_handler[key.RIGHT]:
      self._paddle.x = self.x + 10  
    if self.keys_handler[key.LEFT]:
      self._paddle.x = self.x - 10

  def draw(self):
    self._paddle.draw()

    
