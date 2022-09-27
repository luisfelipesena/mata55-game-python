import pyglet
from pyglet.window import mouse
from classes.walls import Walls
from classes.paddle import Paddle
from classes.ball import Ball
from classes.menu import Menu
from classes.score import Score

window_width = 800
window_height = 500
walls_padding = 10
_window_caption = "One Player Pong"

class MainWindow(pyglet.window.Window):
  def __init__(self):
    super().__init__(window_width, window_height, _window_caption, resizable=False)
    
    # Mouse Handler
    self.mouse_handler = mouse.MouseStateHandler()
    # Walls - Parede
    self.walls = Walls(window_width, window_height, walls_padding)
    # Paddle - Raquete
    paddle_width = window_width / 10
    paddle_height = 10
    paddle_x = (window_width / 2) - (paddle_width / 2)
    paddle_y = 5
    self.paddle = Paddle(paddle_x, paddle_y, paddle_width, paddle_height)
    # Ball - Bola
    ball_width = 10
    ball_x = (window_width / 2) - (ball_width / 2)
    ball_y = (window_height - (walls_padding * 2))
    self.ball = Ball(ball_x, ball_y, ball_width)
    # Menu
    menu_x = (window_width / 2)
    menu_y = (window_height / 2)
    self.menu = Menu(menu_x, menu_y, window_width, window_height)
    # Score
    score_x = 5
    score_y = 535
    score_width = 150
    score_height = 60
    self.score = Score(score_x, score_y, score_width, score_height)
    # Teclas Pressionada
    self.right_arrow_pressed = False
    self.left_arrow_pressed = False
    self.up_arrow_pressed = False
    self.down_arrow_pressed = False
    self.enter_pressed = False
    
  def on_draw(self):
    self.clear()

    self.walls.draw()
    self.paddle.draw()
    self.ball.draw()
    self.menu.draw()
    self.score.draw()

    if self.up_arrow_pressed or self.down_arrow_pressed or self.enter_pressed:
      self.update_menu()
    
  def on_key_press(self, symbol, modifiers):
    if symbol == pyglet.window.key.ESCAPE:
        pyglet.app.exit()
    if symbol == pyglet.window.key.RIGHT:
        self.right_arrow_pressed = True
    if symbol == pyglet.window.key.LEFT:
        self.left_arrow_pressed = True
    if symbol == pyglet.window.key.UP:
        self.up_arrow_pressed = True
    if symbol == pyglet.window.key.DOWN:
        self.down_arrow_pressed = True
    if symbol == pyglet.window.key.ENTER:
        self.enter_pressed = True

  def on_key_release(self, symbol, modifiers):
    if symbol == pyglet.window.key.RIGHT:
        self.right_arrow_pressed = False
    if symbol == pyglet.window.key.LEFT:
        self.left_arrow_pressed = False
    if symbol == pyglet.window.key.UP:
        self.up_arrow_pressed = False
    if symbol == pyglet.window.key.DOWN:
        self.down_arrow_pressed = False
    if symbol == pyglet.window.key.ENTER:
        self.enter_pressed = False

  def on_mouse_press(self, x, y, button, modifiers):
    # if self.carta.inclui_ponto(x, y):
    #     print('Clicou na carta')
    pass
    
    #  Será puxada para atualizar o game
  def update_game(self, arg):
    if self.right_arrow_pressed or self.left_arrow_pressed:
      self.paddle.update()
  #  Será puxada para atualizar o menu   
  def update_menu(self):
    if self.up_arrow_pressed or self.down_arrow_pressed or self.enter_pressed:
      self.menu.update(self.up_arrow_pressed, self.down_arrow_pressed, self.enter_pressed)
    if self.enter_pressed and self.menu.visible == False:
      self.paddle.visible = True
      self.ball.visible = True
      self.score.visible = True

if __name__ == '__main__':
    window = MainWindow()

    # Push handlers
    window.push_handlers(window.mouse_handler)
    window.push_handlers(window.paddle.keys_handler)

    # Clock do jogo 
    if window.paddle.visible == True:
      pyglet.clock.schedule_interval(window.update_game, 1 / 60)
  
    pyglet.app.run()