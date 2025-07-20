import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target, settings):
        super().__init__()
        self.settings = settings

        self.image = pygame.Surface((settings.bullet_size, settings.bullet_size), pygame.SRCALPHA)
        self.image.fill(settings.bullet_color)
        self.rect = self.image.get_rect(center=(x, y))

        self.pos = pygame.Vector2(x, y)
        self.target = target
        self.speed = settings.bullet_speed
        self.damage = settings.bullet_damage

        # Вычисление направления
        direction = pygame.Vector2(target.rect.center) - self.pos
        if direction.length() != 0:
            self.velocity = direction.normalize() * self.speed
        else:
            self.velocity = pygame.Vector2(0, 0)

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos

        # Проверка на столкновение с целью
        if self.target.rect.collidepoint(self.rect.center):
            self.target.take_damage(self.damage)  # нужно реализовать у цели
            self.kill()

        # Опционально: уничтожение пули, если она ушла за экран
        if not pygame.Rect(0, 0, self.settings.screen_width, self.settings.screen_height).collidepoint(self.rect.center):
            self.kill()
