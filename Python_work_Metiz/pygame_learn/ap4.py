import sys
import pygame_learn

from ap2_test_slime import Slime

class Ap4():
    """Создает окно."""

    def __init__(self):
        """Инициализация pygame и других необходимых компонентов."""
        pygame.init()

        self.width_height = (800,600)
        self.screen = pygame.display.set_mode(self.width_height)
        self.bg_color = (30, 120, 56)
        pygame.display.set_caption('Ap4')

        self.slime = Slime(self)

    def run(self):
        """Обноввляет окно и отслеживает нажатия"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.slime.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    ap4 = Ap4()
    ap4.run()
