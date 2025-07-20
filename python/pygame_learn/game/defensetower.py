import pygame
import math
import os

class DefenseTower(pygame.sprite.Sprite):
    def __init__(self, x, y, settings, enemies_group, bullet_group, data):
        super().__init__()
        self.settings = settings
        self.enemies = enemies_group
        self.bullets = bullet_group

        image_path = os.path.join("assets", "buildings", data["image"])
        size = tuple(data["size"])
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect(center=(x + size[0] // 2, y + size[1] // 2))


        self.range = data.get("range", settings.tower_range)
        self.cooldown = data.get("cooldown", settings.tower_cooldown)
        self.damage = data.get("damage", 1)
        self.last_shot = 0

    def update(self, current_time):

        if current_time - self.last_shot < self.cooldown:
            return

        target = self.find_target()
        if target:
            self.shoot(target)
            self.last_shot = current_time


    def find_target(self):
        for enemy in self.enemies:
            dist = math.hypot(enemy.rect.centerx - self.rect.centerx,
                              enemy.rect.centery - self.rect.centery)
            if dist <= self.range:
                return enemy
        return None

    def shoot(self, target):
        print(f"🧨 Пуля: из {self.rect.center} в {target.rect.center}")
        bullet = Bullet(self.rect.center, target, self.settings, self.damage)
        self.bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, target, settings, damage):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((6, 6))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=pos)

        self.target = target
        self.speed = settings.bullet_speed
        self.damage = damage

    def update(self):
        if not self.target or not self.target.alive():
            self.kill()
            return

        dx = self.target.rect.centerx - self.rect.centerx
        dy = self.target.rect.centery - self.rect.centery
        dist = math.hypot(dx, dy)

        if dist < 4:
            self.target.health -= self.damage
            if self.target.health <= 0:
                self.target.kill()
            self.kill()
            return

        dx, dy = dx / dist, dy / dist
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
