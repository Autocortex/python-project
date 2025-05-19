import pygame_learn
import sys

class Ap1():
    """Создает экран и обновляет его"""

    def __init__(self):
        """Инициализирует pygame"""
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.bg_color = (65, 105, 225)

    def run_game(self):
        """Запускает цикл и обрабатывает."""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Отслеживает действия."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _update_screen(self):
        """Обновляет экран"""
        self.screen.fill(self.bg_color)
        pygame.display.flip()


ap1 = Ap1()
ap1.run_game()

