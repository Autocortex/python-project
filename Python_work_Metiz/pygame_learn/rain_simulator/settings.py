class Settings():
    """Settings for Rain simulator."""
    def __init__(self):
        """Initial settings."""
        self.width = 800
        self.height = 600
        self.screen_size = (self.width,self.height)
        self.bg_color = (255,255,255)
        self.raindrop_speed = 0.5