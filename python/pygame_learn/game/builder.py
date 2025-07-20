from building_data import BuildingData
import pygame
import os

from defensetower import DefenseTower

class Builder:

    def __init__(self, inventory, world, tile_size, settings, bullets):
        self.inventory = inventory
        self.world = world
        self.tile_size = tile_size
        self.settings = settings
        self.bullets = bullets
        self.building_data = BuildingData()
        self.selected_building = None
        self.is_placing = False
        self.cache = {}

    def select(self, building_type):
        self.selected_building = building_type

    def get_preview_image(self, building_type):
        if building_type in self.cache:
            return self.cache[building_type]

        data = self.building_data.get(building_type)
        if not data:
            return None

        path = os.path.join("assets", "buildings", data["image"])
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, tuple(data["size"]))

        self.cache[building_type] = image
        return image

    def build(self, x, y):
        if not self.selected_building:
            return False

        data = self.building_data.get(self.selected_building)
        if not data:
            return False

        tile_x = (x // self.tile_size) * self.tile_size
        tile_y = (y // self.tile_size) * self.tile_size

        existing = [obj for obj in self.world.static_objects
                    if hasattr(obj, "building_type") and obj.building_type == self.selected_building]

        limit = data.get("limit")
        if limit is not None and len(existing) >= limit:
            print(f"Превышен лимит для {self.selected_building}: максимум {limit}")
            return False

        cost = data.get("cost", {})
        for item, amount in cost.items():
            if self.inventory.get(item) < amount:
                print("Недостаточно ресурсов")
                return False

        for item, amount in cost.items():
            self.inventory.remove(item, amount)

        img = self.get_preview_image(self.selected_building)

        from pygame.sprite import Sprite
        class StaticBuilding(Sprite):
            def __init__(self, image, x, y, building_type, passable=False):
                super().__init__()
                self.image = image
                self.rect = self.image.get_rect(topleft=(x, y))
                self.building_type = building_type
                self.passable = passable  # ← добавили ключевой флаг

        building_type = data.get("type", "static")

        if building_type == "tower":
            center_x = tile_x + self.tile_size // 2
            center_y = tile_y + self.tile_size // 2
            building = DefenseTower(center_x, center_y, self.settings, self.world.enemies, self.bullets, data)

            self.world.tower_group.add(building)
            self.world.static_objects.add(building)
        else:
            building = StaticBuilding(img, tile_x, tile_y, self.selected_building)
            self.world.static_objects.add(building)

            if building_type == "main_base":
                self.world.main_base = building

        return True

    def get_available_buildings(self):
        result = []
        for building_type in self.building_data.all_types():
            data = self.building_data.get(building_type)
            if not data:
                continue

            limit = data.get("limit")
            if limit is not None:
                count = sum(1 for obj in self.world.static_objects
                            if getattr(obj, "building_type", None) == building_type)
                if count >= limit:
                    continue

            result.append(building_type)
        return result

    def check_limit(self,data):
        existing = [obj for obj in self.world.static_objects
                    if hasattr(obj, "building_type") and obj.building_type == self.selected_building]

        limit = data.get("limit")
        if limit is not None and len(existing) >= limit:
            print(f"Превышен лимит для {self.selected_building}: максимум {limit}")
            return False

    def draw_preview(self, surface, camera):
        if not self.is_placing or not self.selected_building:
            return

        preview = self.get_preview_image(self.selected_building)
        if not preview:
            return

        mouse_x, mouse_y = pygame.mouse.get_pos()
        world_x, world_y = camera.reverse_apply((mouse_x, mouse_y))

        tile_x = (world_x // self.tile_size) * self.tile_size
        tile_y = (world_y // self.tile_size) * self.tile_size

        ghost = preview.copy()
        ghost.set_alpha(150)

        surface.blit(ghost, camera.apply(ghost.get_rect(topleft=(tile_x, tile_y))))


