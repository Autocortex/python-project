import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, aimmaster):
        """Resourse for bullet."""
        super().__init__()
        self.screen = aimmaster.screen
        self.settings = aimmaster.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = aimmaster.player.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Update position bullet."""
        self.x += self.settings.bullet_speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw bullet."""
        pygame.draw.rect(self.screen, self.color, self.rect)
