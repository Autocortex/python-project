import pygame

class Slime():
    """Инициализируем слайма и задаем его начальную позицию."""
    def __init__(self, bs_game):
        """

        :rtype: None
        """
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        #Загружаем изображение слайма и получаем прямоугольник.
        self.image = pygame.image.load('images/slime.bmp')
        self.rect = self.image.get_rect()
        #Каждый новый слайм появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует слайм  в текущей позиции."""
        self.screen.blit(self.image, self.rect)
