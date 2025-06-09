import pygame
import sys
from random import randint

from settings import Settings
from raindrop import Raindrop

class RainSimulator():
    """Rain simulator"""

    def __init__(self):
        """Initial resourses for rain simulator."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption('RAIN SIMULATOR')
        self.raindrops = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """Create fleet."""
        raindrop = Raindrop(self)
        raindrop_width,raindrop_height = raindrop.rect.size
        available_space_x = self.settings.width
        number_raindrop = available_space_x //  raindrop_width
        available_space_y = self.settings.height
        number_rows = available_space_y // raindrop_height
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrop):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self,raindrop_number,row_number):
        """Create raindrop."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        raindrop.y = raindrop_height + 2 * raindrop_height * row_number
        raindrop.rect.y = raindrop.y
        self.raindrops.add(raindrop)



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            for raindrop in self.raindrops.sprites():
                screen_rect = self.screen.get_rect()
                if raindrop.rect.bottom >= screen_rect.bottom:
                    raindrop.y = 30
                    raindrop.rect.y = 30
            self.raindrops.update()
            self.raindrops.draw(self.screen)

            pygame.display.flip()

if __name__ == '__main__':
    rs = RainSimulator()
    rs.run()

