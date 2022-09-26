import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import shapes

# CRIANDO A JANELA E AS ESPECS
width = 1000
height = 600
window = pyglet.window.Window(width, height, 'PING-PONG', resizable=False)
window.set_caption('PING-PONG')

# LIDAR COM O USO DO TECLADO
keys = key.KeyStateHandler()
window.push_handlers(keys)

# TENTANDO IMPLEMENTAR O MOUSE
mouse = mouse.MouseStateHandler()
window.push_handlers(mouse)

# CRIANDO UM BATCH P RENDER GRAFICO
batch = pyglet.graphics.Batch()

# MARGEM DA PAREDE
walls_padding = 10


# DEFININDO PAREDES PARA O JOGO
class walls:
    def __init__(gameMenu):
        gameMenu.wall_left = shapes.Line(0, 0, 0, height, walls_padding, color=(255, 255, 255), batch=batch)
        gameMenu.wall_right = shapes.Line(width, 0, width, height, walls_padding, color=(255, 255, 255), batch=batch)
        gameMenu.wall_top = shapes.Line(0, height, width, height, walls_padding, color=(255, 255, 255), batch=batch)

    def draw(gameMenu):
        gameMenu.wall_left.draw()
        gameMenu.wall_right.draw()
        gameMenu.wall_top.draw()


# CRIAR UM OBJETO DA CLASSE 'PAREDE'
walls = walls()


# DEFININDO A 'RAQUETE'
class paddle:
    def __init__(gameMenu, x, y, width, height):
        gameMenu.paddle = pyglet.shapes.Rectangle(x, y, width, height, color=(255, 255, 255), batch=batch)

    def draw(gameMenu):
        gameMenu.paddle.draw()

    def update(gameMenu):
        addPosition = 100
        if keys[key.RIGHT] or keys[key.D] and gameMenu.paddle.x + addPosition < width - 10:
            gameMenu.paddle.x += addPosition
        elif keys[key.LEFT] or keys[key.A] and gameMenu.paddle.x - addPosition > -10:
            gameMenu.paddle.x -= addPosition


# CRIANDO UM OBJETO DA CLASSE PADDLE
paddle = paddle(450, 5, 100, 10)


# DEFININDO A CLASSE BOLA
class Ball:
    def __init__(gameMenu, x, y):
        gameMenu.ball = pyglet.shapes.Circle(x, y, 10, color=(255, 255, 255), batch=batch)

    def draw(gameMenu):
        gameMenu.ball.draw()

    def update(gameMenu):
        addPosition = 100


# CRIANDO UM OBJETO BOLA
ball = Ball(width / 2, height - 40)


# CRIANDO A CLASSE DE MENU INICIAL
class StartMenu:
    def __init__(StartMenu):
        StartMenu.menu = pyglet.text.Label("One Player Ping Pong", font_name="Arial", font_size=36, x=window.width / 2,
                                           y=window.height / 2 + 230, anchor_x="center", anchor_y="center")

    def draw(StartMenu):
        StartMenu.menu.draw()


# CRIAR UM OBJETO MENU
start_menu = StartMenu()


# DEFININDO BOTOES
class Button:
    def __init__(button):
        button.start = pyglet.text.Label("Iniciar", font_name="Arial", font_size=24, x=window.width / 2,
                                         y=window.height / 2 - 80, anchor_x="center", anchor_y="center")
        button.exit = pyglet.text.Label("Sair", font_name="Arial", font_size=24, x=window.width / 2,
                                        y=window.height / 2 - 130, anchor_x="center", anchor_y="center")

        button.selected = 0
        button.menu_items = [button.start, button.exit]
        button.menu_items[button.selected].color = (255, 0, 0, 255)

    def draw(button):
        button.start.draw()
        button.exit.draw()


botao = Button()


# DEFININDO A CLASSE SCORE BOX
class score:
    def __init__(gameMenu, x, y, width, height):
        cont = 0
        gameMenu.score = pyglet.shapes.Rectangle(x, y, width, height, color=(0, 0, 0), batch=batch)
        gameMenu.scores = pyglet.text.Label("Score: {}".format(cont), font_name="Arial", font_size=15, x=50,
                                            y=580, anchor_x="center", anchor_y="center")

    def draw(gameMenu):
        gameMenu.score.draw()
        gameMenu.scores.draw()

    def update(gameMenu):
        addPosition = 0


# CRIANDO UM OBJETO DA CLASSE SCORE
score = score(5, 535, 150, 60)


@window.event
def on_draw():
    window.clear()
    start_menu.draw()
    walls.draw()
    paddle.draw()
    ball.draw()
    score.draw()
    botao.draw()


def update(dt):
    if start_menu.menu.visible == True:
        pass
    else:
        ball.update()
        paddle.update()


@window.event
def on_mouse_press(x, y, button, modifiers):
    print('clicou')


if __name__ == '__main__':
    if start_menu.menu.visible == True:
        pyglet.clock.schedule_interval(update, 1 / 10)
    else:
        pyglet.clock.schedule_interval(update, 1 / 60)

    pyglet.app.run()








