import pygame

from settings import Settings

class Rocket():
    """Класс для описания ракеты."""

    def __init__(self,rocketgame):
        """Задаем параметры ракеты."""
        self.screen = rocketgame.screen
        self.screen_rect = rocketgame.screen.get_rect()
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.settings = Settings()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed
        self.rect.x = self.x

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.speed
        self.rect.y = self.y

    def blitme(self):
        """Прорисовываем корабль."""
        self.screen.blit(self.image, self.rect)