import pygame_learn
import sys

from settings import Settings

class Ap2():
    """Создает окно."""

    def __init__(self):
        """Инициирует pygame и остальные данные"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.width_height)

    def run_game(self):
        """Запускает и обновляет окно"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

ap2 = Ap2()
ap2.run_game()