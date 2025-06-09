import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Describes the projectile."""
    def __init__(self,  rocketgame):
        """Initialize the object attributes."""
        super().__init__()
        self.screen = rocketgame.screen
        self.settings = rocketgame.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = rocketgame.rocket.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Update actions."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)