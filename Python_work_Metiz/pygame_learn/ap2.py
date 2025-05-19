import sys
import pygame_learn

class Ap2():
    """Создает окно"""

    def __init__(self):
        """Инициирует pygame и игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((800,600))
        self.bg_color = (35,40,80)

    def run_game(self):
        """Запускает окно, отслеживает нжатия и обновляет экран."""
        while True:
            #Отслеживает нажатие выхода
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Цвет заднего фона
            self.screen.fill(self.bg_color)
            #Обновляет экран
            pygame.display.flip()

ap2 = Ap2()
ap2.run_game()