import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Describe raindrop."""

    def __init__(self,rain_sim):
        """Initial resourses for class raindrop."""
        super().__init__()
        self.screen = rain_sim.screen
        self.settings = rain_sim.settings
        self.image = pygame.image.load('images/drop_30x30.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def update(self):
        """Update raindrop."""
        self.y += 0.2
        self.rect.y = self.y
