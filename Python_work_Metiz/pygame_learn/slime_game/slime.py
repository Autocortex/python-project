import pygame

class Slime():
    """Class describing slime."""

    def __init__(self,slimegame):
        """Initializing Slime Information"""
        self.screen = slimegame.screen
        self.screen_rect = slimegame.screen.get_rect()
        self.settings = slimegame.settings
        self.image = pygame.image.load('images/slime.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.moving_bottom = False
        self.moving_top = False

    def update(self):
        """Slime movements."""
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.slime_speed
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.slime_speed
        self.rect.y = self.y


    def blitme(self):
        """Draws slime"""
        self.screen.blit(self.image, self.rect)