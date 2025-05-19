import pygame_learn

class Slime():
    """Описывает слайма."""

    def __init__(self, ap4):
        """Иницилизируем все необходимое для класса слайм"""
        self.screen = ap4.screen
        self.screen_rect = ap4.screen.get_rect()
        self.image = pygame.image.load('images/slime.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует слайм в текущей позиции."""
        self.screen.blit(self.image, self.rect)