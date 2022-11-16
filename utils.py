class Utils:
    window_width = 800
    window_height = 600
    window_caption = "One Player Pong"
    walls_padding = 10
    fps = 60.0

    def __init__(self, window_height=None, window_width=None, window_caption=None, walls_padding=None, fps=None):
        self.window_width = Utils.window_width
        self.window_height = Utils.window_height
        self.window_caption = Utils.window_caption
        self.walls_padding = Utils.walls_padding
        self.fps = Utils.fps
