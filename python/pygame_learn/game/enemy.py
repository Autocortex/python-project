import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, target, settings):
        super().__init__()
        self.settings = settings
        self.image = pygame.Surface((settings.enemy_size, settings.enemy_size))
        self.image.fill(settings.enemy_color)  # временно чёрный
        self.rect = self.image.get_rect(center=(x, y))

        self.pos = pygame.Vector2(x, y)
        self.target = target
        self.speed = settings.enemy_speed
        self.health = settings.enemy_health

    def update(self):
        if self.health <= 0:
            self.kill()
            return

        if not self.target or not self.target.alive():
            return

        direction = pygame.Vector2(self.target.rect.center) - self.pos
        distance = direction.length()

        if distance < 5:  # Радиус контакта с main_base
            if hasattr(self.target, "health"):
                self.target.health -= 1  # Урон базе
                print(f"Базе нанесён урон! Здоровье: {self.target.health}")
                if self.target.health <= 0:
                    print("База разрушена!")
            self.kill()
            return

        if distance != 0:
            direction = direction.normalize()
            self.pos += direction * self.speed
            self.rect.center = self.pos

    def take_damage(self, amount):
        self.health -= amount
