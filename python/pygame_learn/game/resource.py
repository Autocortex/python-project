import pygame
import os
import random

class Resource(pygame.sprite.Sprite):
    RESOURCE_TYPES = {
        "oak_tree": "oak_tree.png",
        "fruit_tree": "fruit_tree.png",
        "pine_tree": "pine_tree.png",
        "large_tree": "large_tree.png",
        # В будущем: "rock": "rock.png", "bush": "bush.png", и т.д.
    }

    IMAGE_FOLDER = os.path.join("assets", "resources")
    loaded_images = {}

    def __init__(self, x, y, resource_type=None):
        super().__init__()
        self.type = resource_type or random.choice(list(self.RESOURCE_TYPES.keys()))
        self.image = self.load_image(self.type)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)  # Привязка к земле

    @classmethod
    def load_image(cls, name):
        if name not in cls.loaded_images:
            path = os.path.join(cls.IMAGE_FOLDER, cls.RESOURCE_TYPES[name])
            image = pygame.image.load(path).convert_alpha()
            cls.loaded_images[name] = image
        return cls.loaded_images[name]
