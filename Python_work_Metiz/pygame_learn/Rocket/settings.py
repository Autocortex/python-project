class Settings():
    """Содержит настройки игрыю"""

    def __init__(self):
        """Иницилизирует настройки"""
        self.width = 800
        self.height = 600
        self.bg_color = (0, 0, 30)
        self.speed = 0.4
        #Settings bullet
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_alowed = 1