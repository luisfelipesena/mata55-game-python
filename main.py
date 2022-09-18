import pyglet
from pyglet.window import key
from pyglet import shapes

# create a batch class
batch = pyglet.graphics.Batch()

# Window
width = 800
height = 600
window = pyglet.window.Window(width, height, "One Player Ping Pong", resizable=False)
window.set_caption("One Player Ping Pong")

# Key Handler
keys = key.KeyStateHandler()
window.push_handlers(keys)

# create a walls class
walls_padding = 10
class Walls:
    def __init__(self):
        self.wall_left = shapes.Line(0, 0, 0, height, walls_padding, color=(255, 255, 255), batch=batch)
        self.wall_right =  shapes.Line(width, 0, width, height, walls_padding, color=(255, 255, 255), batch=batch)
        self.wall_top = shapes.Line(0, height, width, height, walls_padding, color=(255, 255, 255), batch=batch)
        self.wall_bottom = shapes.Line(0, 0, width, 0, walls_padding, color=(255, 255, 255), batch=batch)


    def draw(self):
        self.wall_left.draw()
        self.wall_right.draw()
        self.wall_top.draw()
        self.wall_bottom.draw()

# create a walls object
walls = Walls()

# create a paddle class
class Paddle:
    def __init__(self, x, y, width, height):
        self.paddle = pyglet.shapes.Rectangle(x, y, width, height, color = (255, 0, 0), batch = batch)

    def draw(self):
        self.paddle.draw()

    def update(self):
        addPosition = 100
        print(self.paddle.x)

        if keys[key.RIGHT] and self.paddle.x + addPosition < width - 10:
            self.paddle.x += addPosition
        elif keys[key.LEFT] and self.paddle.x - addPosition > -10:
            self.paddle.x -= addPosition
        

# create a paddle object
paddle = Paddle(360, 20, 100 - walls_padding, 10)

# create a ball class
class Ball:
    def __init__(self, x, y):
        self.ball = pyglet.shapes.Circle(x, y, 10, color = (255, 255, 255), batch = batch)

    def draw(self):
        self.ball.draw()

    def update(self):
        addPosition = 100

        # create ball movement
        if keys[key.LEFT]:
            self.ball.x -= addPosition + pyglet.clock.tick()
        if keys[key.RIGHT]:
            self.ball.x += addPosition + pyglet.clock.tick()


# create a ball object
ball = Ball(width / 2, height - 40)
    
# create a start menu class
class StartMenu:
    def __init__(self):
        self.menu = pyglet.text.Label("One Player Ping Pong", font_name="Arial", font_size=36, x=window.width / 2, y=window.height / 2, anchor_x="center", anchor_y="center")
        self.start = pyglet.text.Label("Iniciar", font_name="Arial", font_size=24, x = window.width / 2, y=window.height/ 2-80, anchor_x="center", anchor_y="center")
        self.exit = pyglet.text.Label("Sair", font_name="Arial", font_size=24, x = window.width / 2, y=window.height / 2- 130, anchor_x="center", anchor_y="center")

        self.selected = 0
        self.menu_items = [self.start, self.exit]
        self.menu_items[self.selected].color = (255, 0, 0, 255)

    def draw(self):
        self.menu.draw()
        self.start.draw()
        self.exit.draw()

    def update(self):
        if keys[key.UP]:
            self.menu_items[self.selected].color = (255, 255, 255, 255)
            self.selected -= 1
            if self.selected < 0:
                self.selected = len(self.menu_items)-1
            self.menu_items[self.selected].color = (255, 0, 0, 255)

        if keys[key.DOWN]:
            self.menu_items[self.selected].color = (255, 255, 255, 255)
            self.selected += 1
            if self.selected > len(self.menu_items)-1:
                self.selected = 0
            self.menu_items[self.selected].color = (255, 0, 0, 255)

        if keys[key.ENTER]:
            if self.selected == 0:
                self.menu.visible = False
                self.start.visible = False
                self.exit.visible = False
                
            if self.selected == 1:
                pyglet.app.exit()

# create a start menu object
start_menu = StartMenu()

# on draw function
@window.event
def on_draw():
    window.clear()

    start_menu.draw()
    walls.draw()
    paddle.draw()
    ball.draw()

def update(dt):
    if  start_menu.menu.visible == True:
        start_menu.update()
    else: 
        ball.update()
        paddle.update()
       

if __name__ == '__main__':
    if start_menu.menu.visible == True:
        pyglet.clock.schedule_interval(update, 1 / 10)
    else:
        pyglet.clock.schedule_interval(update, 1 / 60)

    pyglet.app.run()

