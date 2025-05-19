import sys

import pygame

from settings import Settings
from slime import Slime


class BlueSky():
    """Создает окно Pygame с синим фоном."""

    def __init__(self):
        """Инициализирует окно pygame"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky")

        self.slime = Slime(self)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            #Отслеживание событий мыши и клавиатуры.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #При каждом проходе цикла прорисовывается экран.
            self.screen.fill(self.settings.bg_color)
            self.slime.blitme()

            #Отображение последнего прорисованного экрана.
            pygame.display.flip()

if __name__ == '__main__':
    #Создание экземпляра и запуск.
    bs = BlueSky()
    bs.run_game()