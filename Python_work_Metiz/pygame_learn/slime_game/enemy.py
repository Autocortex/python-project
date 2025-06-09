import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    """Описывает врага"""

    def __init__(self, slimegame):
        """Задаем начальные значения обьекту Враг."""
        super().__init__()
        self.screen = slimegame.screen
        self.settings = slimegame.settings
        self.screen_width = self.screen.get_width()
        self.image = pygame.image.load('images/enemy_01.png').convert_alpha() #convert_alpha - обрабатывает прозрачность
        self.rect = self.image.get_rect()
        self.rect.topright = (self.screen_width, 0)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Возвращает True, если враг у края."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top < screen_rect.top:
            return True

    def update(self):
        "Движение врага"
        self.y += (self.settings.enemy_speed * self.settings.fleet_direction)
        self.rect.y = self.y
