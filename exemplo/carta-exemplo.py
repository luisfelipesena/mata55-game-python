from enum import Enum
from pyglet import shapes
import pyglet

class CorNaipe(Enum):
    PRETA = 0
    VERMELHA = 1

class Naipe(Enum):
    PAUS = '♣️'
    ESPADAS = '♠️'
    COPAS = '♥️'
    OUROS = '♦️'

    def cor(self):
        if self in [Naipe.ESPADAS, Naipe.PAUS]:
            return CorNaipe.PRETA
        else:
            return CorNaipe.VERMELHA

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        self.image = pyglet.image.load('images/carta.jpg')
        self._sprite = pyglet.sprite.Sprite(self.image, x=50, y=50)
        self._label = pyglet.text.Label(str(self.valor), x=70, y=250,
            color=(255, 0, 0, 255),
            font_name='Times New Roman',
                          font_size=36, anchor_x='center', anchor_y='center')
    
    @property
    def x(self):
        return self._sprite.x
    @x.setter
    def x(self, nx):
        self._sprite.x = nx
        self._label.x = nx + 20
    @property
    def y(self):
        return self._sprite.y
    @y.setter
    def y(self, ny):
        self._sprite.y = ny
        self._label.y = ny + 200

    def inclui_ponto(self, x, y):
        return x >= self._sprite.x and x <= self._sprite.x + self._sprite.width \
            and y >= self._sprite.y and y <= self._sprite.y + self._sprite.height
    
    def draw(self):
        self._sprite.draw()
        self._label.x = self._sprite.x + 20
        self._label.y = self._sprite.y + 200
        self._label.draw()



        
class Baralho:
    def __init__(self):
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        naipes = Naipe.__members__.values()
        self.cartas = []
        for naipe in naipes:
            for valor in valores:
                carta = Carta(valor, naipe)
                self.cartas.append(carta)