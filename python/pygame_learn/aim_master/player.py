import pygame

class Player():

    def __init__(self, aimmaster):
        """Initial resourse for class Player"""
        self.screen = aimmaster.screen
        self.settings = aimmaster.settings
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_top = False
        self.moving_bottom = False
        self.y = float(self.rect.y)

    def update(self):
        """Movement player."""
        if self.moving_top == True and self.rect.top > 0:
            self.y -= self.settings.player_speed_factor
            self.rect.y = self.y
        elif self.moving_bottom == True and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.player_speed_factor
            self.rect.y = self.y


    def blitme(self):
        """Draw player."""
        self.screen.blit(self.image, self.rect)
