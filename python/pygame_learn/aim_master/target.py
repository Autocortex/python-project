import pygame

class Target():

    def __init__(self, aimmaster):
        """Resources for target."""
        self.screen = aimmaster.screen
        self.settings = aimmaster.settings
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/target.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

    def update(self):
        """Update target."""
        self.y += self.settings.speed_target_factor * self.settings.direction_target
        self.rect.y = self.y
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top < 0:
            self.settings.direction_target *= -1



    def blittarget(self):
        """Draw target."""
        self.screen.blit(self.image, self.rect)

