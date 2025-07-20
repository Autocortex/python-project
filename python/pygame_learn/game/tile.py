import pygame
import random
import os

class Tile(pygame.sprite.Sprite):
    # Путь к папке с тайлами
    TILE_FOLDER = os.path.join("assets", "tiles")

    # Карта соответствия типов и файлов
    TILE_TYPES = {
        "grass": "grass.bmp",
        "stone": "stone.bmp",
        "road": "road.bmp",
    }

    loaded_images = {}

    def __init__(self, x, y, size, tile_type=None):
        super().__init__()
        self.type = tile_type or random.choice(list(self.TILE_TYPES.keys()))
        self.image = self.load_image(self.type, size)
        self.rect = self.image.get_rect(topleft=(x, y))

    @classmethod
    def load_image(cls, tile_type, size):
        if tile_type not in cls.loaded_images:
            path = os.path.join(cls.TILE_FOLDER, cls.TILE_TYPES[tile_type])
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, (size, size))
            cls.loaded_images[tile_type] = image
        return cls.loaded_images[tile_type]
