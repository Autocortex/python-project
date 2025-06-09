import pygame
import sys
from random import randint

from star import Star

class Sky():

    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        star = Star(self)
        star_width = star.rect.width
        available_space_x = self.width - (2  * star_width)
        number_stars_x = available_space_x // (2 * star_width)
        star_height = star.rect.height
        available_space_y = self.height
        number_rows = available_space_y // ( 2 * star_height)
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                star = Star(self)
                star.x = star_width + 2 * randint(40, 80) * star_number
                star.rect.x = star.x
                star.rect.y = star_height + 2 * randint(30, 80) * row_number
                self.stars.add(star)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((30,30,30))
            self.stars.draw(self.screen)
            pygame.display.flip()

if __name__ == '__main__':
    sky = Sky()
    sky.run()