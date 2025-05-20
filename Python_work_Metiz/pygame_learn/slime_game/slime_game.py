import pygame
import sys

from settings import Settings
from slime import Slime

class SlimeGame():
    """Class for managing game resources and behavior."""

    def __init__(self):
        """Initiating game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.width_height)
        pygame.display.set_caption('SlimeGame')
        self.slime = Slime(self)

    def run_game(self):
        """Creates a loop and tracks actions, updates the screen."""
        while True:
            self._update_events()
            self.slime.update()
            self._update_screen()

    def _update_events(self):
        """Tracks actions."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._update_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._update_events_keyup(event)

    def _update_events_keydown(self,event):
        """Keydown events."""
        if event.key == pygame.K_s:
            self.slime.moving_bottom = True
        elif event.key == pygame.K_w:
            self.slime.moving_top = True

    def _update_events_keyup(self,event):
        """Keyup events."""
        if event.key == pygame.K_s:
            self.slime.moving_bottom = False
        elif event.key == pygame.K_w:
            self.slime.moving_top = False

    def _update_screen(self):
        """Updates the screen."""
        self.screen.fill(self.settings.bg_color)
        self.slime.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    sg = SlimeGame()
    sg.run_game()