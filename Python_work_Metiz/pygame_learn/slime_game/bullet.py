import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Describes bullet."""
    def __init__ (self, slimegame):
        """Initializing bullet Information."""
        super().__init__()
        self.screen = slimegame.screen
        self.settings = slimegame.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = slimegame.slime.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Updating the projectile position."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw bullet."""
        pygame.draw.rect(self.screen, self.color, self.rect)

