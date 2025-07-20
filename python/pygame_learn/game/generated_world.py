import random
import pygame

from chunk import Chunk
from resource import Resource


class GeneratedWorld:
    def __init__(self, tile_size, chunk_size):
        self.tile_size = tile_size
        self.chunk_size = chunk_size
        self.chunks = {}  # ключ: (chunk_x, chunk_y), значение: Chunk
        self.resources = pygame.sprite.Group()
        self.static_objects = pygame.sprite.Group()
        self.tower_group = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

    def get_chunk_key(self, x, y):
        """Вычисляем ключ чанка по мировой позиции"""
        chunk_x = x // (self.tile_size * self.chunk_size)
        chunk_y = y // (self.tile_size * self.chunk_size)
        return (chunk_x, chunk_y)

    def generate_chunk_if_needed(self, chunk_x, chunk_y):
        if (chunk_x, chunk_y) not in self.chunks:
            new_chunk = Chunk(chunk_x, chunk_y, self.tile_size, self.chunk_size)
            self.chunks[(chunk_x, chunk_y)] = new_chunk
            for tile in new_chunk.tiles:
                if tile.type == "grass" and random.random() < 0.1:
                    resource = Resource(tile.rect.centerx, tile.rect.bottom)
                    self.resources.add(resource)

    def update_around_player(self, player_rect):
        """Обновляет чанки вокруг текущего местоположения игрока"""
        player_chunk = self.get_chunk_key(player_rect.centerx, player_rect.centery)

        # Подгружаем чанки в радиусе 1 от текущего
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                cx, cy = player_chunk[0] + dx, player_chunk[1] + dy
                self.generate_chunk_if_needed(cx, cy)

    def get_all_tiles(self):
        """Возвращает все тайлы из всех чанков"""
        tiles = []
        for chunk in self.chunks.values():
            tiles.extend(chunk.tiles)
        return tiles

    def get_all_objects(self):
        """Объединяет все рисуемые объекты: ресурсы, башни и постройки"""
        return self.resources.sprites() + self.tower_group.sprites() + self.static_objects.sprites()
