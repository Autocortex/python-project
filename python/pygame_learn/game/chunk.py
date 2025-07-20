import pygame
from noise import pnoise2

from tile import Tile

class Chunk:
    def __init__(self, chunk_x, chunk_y, tile_size, tiles_per_chunk):
        self.tiles = pygame.sprite.Group()
        start_x = chunk_x * tile_size * tiles_per_chunk
        start_y = chunk_y * tile_size * tiles_per_chunk

        for row in range(tiles_per_chunk):
            for col in range(tiles_per_chunk):
                x = start_x + col * tile_size
                y = start_y + row * tile_size

                # Генерируем шум по координатам чанка
                nx = (x / 100.0)
                ny = (y / 100.0)
                value = pnoise2(nx, ny, octaves=3)

                # Назначаем тип тайла в зависимости от значения шума
                if value < -0.1:
                    tile_type = "grass"
                elif value < 0.3:
                    tile_type = "road"
                else:
                    tile_type = "stone"

                tile = Tile(x, y, tile_size, tile_type)
                self.tiles.add(tile)

    def draw(self, surface):
        self.tiles.draw(surface)
