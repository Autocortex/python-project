import pygame_learn

class Slime():
    """Задает параметры слайма"""
    def __init__(self, ap5):
        """Инициирует все необходимое для работы со слаймом"""
        self.screen = ap5.screen
        self.screen_rect = ap5.screen.get_rect()
        self.image = pygame.image.load('images/slime.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1

    def blitme(self):
        """Рисует слайма"""
        self.screen.blit(self.image, self.rect)