import pygame
import sys
import random

from settings import Settings
from player import Player
from camera import Camera
from generated_world import GeneratedWorld
from gathering import GatheringManager
from ui.progress_bar import ProgressBar
from ui.inventory_ui import InventoryUI
from ui.build_ui import BuildUI
from builder import Builder
from wave_timer import WaveTimer
from enemy import Enemy
from pasabilitymanager import PassabilityManager


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Моя Игра")
        self.clock = pygame.time.Clock()
        self.running = True

        # Камера
        self.camera = Camera(self.settings)

        # Игрок
        self.player = Player(100, 100, self.settings)
        self.all_sprites = pygame.sprite.Group(self.player)
        self.gather_bar = ProgressBar(width=40, height=6)

        # Мир
        self.tile_size = 40
        self.chunk_size = 8
        self.world = GeneratedWorld(tile_size=self.tile_size, chunk_size=self.chunk_size)

        # PassabilityManager
        self.passability_manager = PassabilityManager(
            self.world.resources.sprites() + self.world.static_objects.sprites()
        )

        # Сбор ресурсов
        self.gathering = GatheringManager(
            player=self.player,
            resource_group=self.world.resources,
            inventory=self.player.inventory
        )

        # Интерфейсы
        self.inventory_ui = InventoryUI(self.player.inventory, self.settings)
        self.show_inventory = False

        # Пули
        self.bullets = pygame.sprite.Group()

        # Постройки
        self.builder = Builder(
            self.player.inventory,
            self.world,
            tile_size=self.tile_size,
            settings=self.settings,
            bullets=self.bullets
        )
        self.build_ui = BuildUI(self.builder, self.settings)

        # Волны
        self.wave_font = pygame.font.SysFont(None, 28)
        self.wave_timer = WaveTimer(self.wave_font)
        self.enemies = pygame.sprite.Group()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.gathering.start()
                elif event.key == pygame.K_r:
                    self.show_inventory = not self.show_inventory
                elif event.key == pygame.K_TAB:
                    self.build_ui.toggle()
                elif event.key == pygame.K_ESCAPE:
                    self.builder.is_placing = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    self.gathering.stop()

            if self.build_ui.active:
                self.build_ui.handle_input(event)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.builder.is_placing:
                    world_pos = self.camera.reverse_apply(pygame.mouse.get_pos())
                    if self.builder.build(*world_pos):
                        self.builder.is_placing = False
                        self.update_passability()

    def update_passability(self):
        """Обновление данных о проходимости после строительства"""
        self.passability_manager.map_objects = (
            self.world.resources.sprites() + self.world.static_objects.sprites()
        )

    def update(self):
        delta = self.clock.get_time()
        current_time = pygame.time.get_ticks()

        self.player.update(self.passability_manager)
        self.all_sprites.update()
        self.camera.update(self.player.rect)
        self.world.update_around_player(self.player.rect)
        self.gathering.update(delta)

        self.wave_timer.update()
        if self.wave_timer.is_wave_triggered():
            self.spawn_wave()

        for tower in self.world.tower_group:
            tower.update(current_time)

        self.enemies.update()
        self.bullets.update()

    def spawn_wave(self):
        if not self.world.main_base:
            print("⚠ Нет главного здания для атаки")
            return

        tile_size = self.tile_size
        chunk_size = self.chunk_size

        min_x = min(x for (x, y) in self.world.chunks) * chunk_size * tile_size
        max_x = (max(x for (x, y) in self.world.chunks) + 1) * chunk_size * tile_size
        min_y = min(y for (x, y) in self.world.chunks) * chunk_size * tile_size
        max_y = (max(y for (x, y) in self.world.chunks) + 1) * chunk_size * tile_size

        for _ in range(5):
            side = random.choice(["top", "bottom", "left", "right"])
            if side == "top":
                x = random.randint(min_x, max_x)
                y = min_y - 40
            elif side == "bottom":
                x = random.randint(min_x, max_x)
                y = max_y + 40
            elif side == "left":
                x = min_x - 40
                y = random.randint(min_y, max_y)
            elif side == "right":
                x = max_x + 40
                y = random.randint(min_y, max_y)

            enemy = Enemy(x, y, self.world.main_base, self.settings)
            self.enemies.add(enemy)
            self.world.enemies.add(enemy)

    def draw(self):
        self.screen.fill(self.settings.black)

        for tile in self.world.get_all_tiles():
            self.screen.blit(tile.image, self.camera.apply(tile.rect))

        for res in self.world.resources:
            self.screen.blit(res.image, self.camera.apply(res.rect))

        for obj in self.world.static_objects:
            self.screen.blit(obj.image, self.camera.apply(obj.rect))

        if self.gathering.is_active() and self.gathering.target:
            progress = self.gathering.get_progress()
            bar_x = self.gathering.target.rect.centerx - self.gather_bar.width // 2
            bar_y = self.gathering.target.rect.top - 10
            self.gather_bar.draw(self.screen, (bar_x, bar_y), progress, camera=self.camera)

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite.rect))

        if self.show_inventory:
            self.inventory_ui.draw(self.screen)

        self.build_ui.draw(self.screen)
        if self.builder.is_placing:
            self.builder.draw_preview(self.screen, self.camera)

        self.wave_timer.draw(self.screen, self.settings.screen_width)

        for enemy in self.enemies:
            self.screen.blit(enemy.image, self.camera.apply(enemy.rect))
        for bullet in self.bullets:
            self.screen.blit(bullet.image, self.camera.apply(bullet.rect))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.settings.fps)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
