import sys
import pygame_learn

from ap5_slime import Slime

class Ap5():
    """Создает игру"""

    def __init__(self):
        """Иницилизирует pygame и игровые ресурсы."""
        pygame.init()
        self.width_height = (800,600)
        self.screen = pygame.display.set_mode(self.width_height)
        self.bg_color = (98,112,134)
        pygame.display.set_caption('Ap5')

        self.slime = Slime(self)


    def run(self):
        """Запускает окно и отслеживает нажатия, обновляет экран"""
        while True:
            self._check_events()
            self.slime.update()
            self._update_screen()

    def _check_events(self):
        """Отслеживает нажатия."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            self._check_events_keydown(event)
            self._check_events_keyup(event)

    def _check_events_keydown(self,event):
        """Действия при нажатии клавиши"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.slime.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.slime.moving_left = True
            elif event.key == pygame.K_UP:
                self.slime.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.slime.moving_down = True

    def _check_events_keyup(self,event):
        """Действие при отпускании клавиши"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.slime.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.slime.moving_left = False
            elif event.key == pygame.K_UP:
                self.slime.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.slime.moving_down = False


    def _update_screen(self):
        """Обновляет экран"""
        self.screen.fill(self.bg_color)#Заполняет экран цветом
        self.slime.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ap4 = Ap5()
    ap4.run()