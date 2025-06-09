import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Describe star."""

    def __init__(self, bluesky):
        """Initializes the star and sets its starting position."""
        super().__init__()
        self.screen = bluesky.screen
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)