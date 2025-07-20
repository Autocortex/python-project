import pygame
import os
from resource_data import ResourceData


class Resource(pygame.sprite.Sprite):
    IMAGE_FOLDER = os.path.join("assets", "resources")
    loaded_images = {}
    resource_data = ResourceData()

    def __init__(self, x, y, resource_type=None):
        super().__init__()
        self.type = resource_type or self.resource_data.random_type()

        data = self.resource_data.get(self.type)
        image_file = data["image"]
        size = tuple(data["size"])

        # Загрузка изображения
        self.image = self.load_image(self.type, image_file, size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

        # Ключевые игровые свойства
        self.passable = data.get("passable", True)               # ← добавлено
        self.health = data.get("health", 1)
        self.harvestable = data.get("harvestable", False)
        self.category = data.get("type", "unknown")
        self.drops = data.get("drops", {})

    def gather(self, damage=1):
        """Наносит урон ресурсу. Возвращает True, если ресурс уничтожен."""
        if not self.harvestable:
            return False

        self.health -= damage
        return self.health <= 0

    def get_drops(self):
        """Возвращает копию ресурсов, выпадающих из объекта."""
        return self.drops.copy()

    @classmethod
    def load_image(cls, res_type, filename, size):
        """Загружает и кэширует изображение ресурса."""
        if res_type not in cls.loaded_images:
            path = os.path.join(cls.IMAGE_FOLDER, filename)
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, size)
            cls.loaded_images[res_type] = image
        return cls.loaded_images[res_type]
