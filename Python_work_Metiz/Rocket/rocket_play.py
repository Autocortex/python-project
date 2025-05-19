import pygame
import sys
from settings import Settings
from rocket import Rocket

class RocketGame():
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))

        self.rocket = Rocket(self)


    def run_game(self):
        """Запускает игру."""
        while True:
            self._update_events()
            self.rocket.update()
            self._update_screen()

    def _update_events(self):
        """Обрабатывает нажатия."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._update_event_keydown(event)
            self._update_event_keyup(event)

    def _update_event_keydown(self, event):
        """Реакция на нажатие клавиши."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.rocket.moving_left = True
            elif event.key == pygame.K_UP:
                self.rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.rocket.moving_down = True

    def _update_event_keyup(self, event):
        """Реакция на отпускание клавиши"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.rocket.moving_left = False
            elif event.key == pygame.K_UP:
                self.rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.rocket.moving_down = False




    def _update_screen(self):
        """Обновляет экран"""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    rocketgame = RocketGame()
    rocketgame.run_game()

