import sys
import pygame

from settings import Settings

class GameS():

    def __init__(self):
        """Resourses for GamseS."""
        pygame.init()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings = Settings()
        pygame.display.set_caption('GameS')

    def run_game(self):
        """Start game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Check all evenets with mouse and keyboard."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._check_keydowns_events(event)

    def _check_keydowns_events(self, event):
        """Keydown events."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit() # Next time, key for menu.

    def _update_screen(self):
        """Update screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


