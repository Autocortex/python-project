import sys
from random import randint
from time import sleep

import pygame

from settings import Settings
from slime import Slime
from bullet import Bullet
from game_stats import GameStats
from enemy import Enemy

class SlimeGame():
    """Class for managing game resources and behavior."""

    def __init__(self):
        """Initiating game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption('SlimeGame')
        self.gamestats = GameStats(self)
        self.slime = Slime(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Creates a loop and tracks actions, updates the screen."""
        while True:
            self._update_events()
            if self.gamestats.counter_slime:
                self.slime.update()
                self._update_bullets()
                self._update_enemies()
            self._update_screen()

    def _update_events(self):
        """Tracks actions."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._update_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._update_events_keyup(event)

    def _update_events_keydown(self,event):
        """Keydown events."""
        if event.key == pygame.K_s:
            self.slime.moving_bottom = True
        elif event.key == pygame.K_w:
            self.slime.moving_top = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _fire_bullet(self):
        """Создание нового снаряда и включение в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Обновляет позиции снарядов и удаляет старые снаряды."""
        #Обновляет позицию снарядов
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.x >= self.settings.width:
                self.bullets.remove(bullet)
        self._check_bullet_enemy_collisions()


    def _check_bullet_enemy_collisions(self):
        """Проверяет столкновение снарядов и врагов, создает новых врагов."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.enemies, True, True
        )
        self.gamestats.enemies_score += sum(len(v) for v in collisions.values())
        print("Попаданий:", self.gamestats.enemies_score)

        if not self.enemies:
            self.bullets.empty()
            self._create_fleet()

    def _update_events_keyup(self,event):
        """Keyup events."""
        if event.key == pygame.K_s:
            self.slime.moving_bottom = False
        elif event.key == pygame.K_w:
            self.slime.moving_top = False

    def _update_enemies(self):
        """Update position all enemies."""
        self._check_fleet_edges()
        self.enemies.update()
        if pygame.sprite.spritecollideany(self.slime, self.enemies):
            self._slime_hit()
        self._check_enemies_edges()
        print(self.gamestats.health_slime)

    def _check_enemies_edges(self):
        """Enemies collisions with edge of the screen. """
        screen_rect = self.screen.get_rect()
        for enemy in self.enemies.sprites():
            if enemy.rect.left <= screen_rect.left:
                self._slime_hit()
                break



    def _slime_hit(self):
        """Slime hit."""
        if self.gamestats.health_slime > 1 :
            self.gamestats.health_slime -= 1
            self.bullets.empty()
            self.enemies.empty()
            self._create_fleet()
            self.slime.slime_center()
            sleep(0.7)
        else:
            self.gamestats.counter_slime = False

    def _create_fleet(self):
        """Create fleet."""
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        available_space_y = self.settings.height - (2 * enemy_height)
        enemy_number_y = available_space_y // (2 * enemy_height)
        available_space_x = self.settings.width - (4 * enemy_width)
        enemy_rows = available_space_x // (2 * enemy_width)
        for row_enemy in range(enemy_rows):
            for number_enemy in range(enemy_number_y):
                self._create_enemy(number_enemy, row_enemy)


    def _create_enemy(self, number_enemy, row_enemy):
        """Create_enemy"""
        enemy = Enemy(self)
        enemy_width, enemy_height = enemy.rect.size
        enemy.rect.x = randint(3,6
                               ) * enemy_width + (2 * enemy_width * row_enemy)
        enemy.y = enemy_height + randint(20,50) + (2 * enemy_height * number_enemy)
        enemy.rect.y = enemy.y
        self.enemies.add(enemy)

    def _check_fleet_edges(self):
        """Check edges for enemies."""
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Change fleet direction"""
        for enemy in self.enemies.sprites():
            enemy.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        """Updates the screen."""
        self.screen.fill(self.settings.bg_color)
        self.slime.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemies.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    sg = SlimeGame()
    sg.run_game()