import pygame

from inventory import Inventory
from settings import Settings
from animator import Animator


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, settings: Settings):
        super().__init__()
        self.settings = settings
        self.inventory = Inventory()

        self.animator = Animator("assets/player", (settings.player_width, settings.player_height))
        self.image = self.animator.get_image()
        self.rect = self.image.get_rect(topleft=(x, y))

        self.speed = self.settings.player_speed

    def handle_keys(self, passability_manager=None):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_w]:
            dy = -self.speed
            self.animator.set_direction("top")
        elif keys[pygame.K_s]:
            dy = self.speed
            self.animator.set_direction("down")
        elif keys[pygame.K_a]:
            dx = -self.speed
            self.animator.set_direction("left")
        elif keys[pygame.K_d]:
            dx = self.speed
            self.animator.set_direction("right")

        if dx != 0 or dy != 0:
            new_rect = self.rect.move(dx, dy)
            if not passability_manager or passability_manager.is_position_passable(new_rect):
                self.rect = new_rect  # Двигаемся только если проходимо

    def update(self, passability_manager=None):
        self.handle_keys(passability_manager)
        self.image = self.animator.get_image()
