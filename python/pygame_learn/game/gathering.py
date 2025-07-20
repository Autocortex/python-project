import pygame

class GatheringManager:
    def __init__(self, player, resource_group, inventory):
        self.player = player
        self.resources = resource_group
        self.inventory = inventory

        self.target = None
        self.timer = 0
        self.time_per_health = 400  # мс за 1 HP (пример)

    def start(self):
        for res in self.resources:
            if self.player.rect.colliderect(res.rect) and res.harvestable:
                self.target = res
                self.timer = 0
                self.time_required = res.health * self.time_per_health
                break

    def stop(self):
        self.target = None
        self.timer = 0

    def update(self, delta_time):
        if not self.target:
            return

        self.timer += delta_time
        if self.timer >= self.time_required:
            for item, amount in self.target.get_drops().items():
                self.inventory.add(item, amount)

            self.target.kill()  # ← сразу убираем ресурс
            self.stop()

    def is_active(self):
        return self.target is not None

    def get_progress(self):
        if not self.target:
            return 0
        return min(self.timer / self.time_required, 1.0)
