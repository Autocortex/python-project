import pygame
import os

class BuildUI:
    ICON_SIZE = 48
    PADDING = 10

    def __init__(self, builder, settings):
        self.builder = builder
        self.settings = settings
        self.buildings = self.builder.building_data.all_types()
        self.font = pygame.font.SysFont(None, 20)
        self.icons = self.load_icons()

        self.active = False
        self.icon_rects = []

    def load_icons(self):
        result = {}
        for name in self.buildings:
            data = self.builder.building_data.get(name)
            path = os.path.join("assets", "buildings", data["image"])
            image = pygame.image.load(path).convert_alpha()
            image = pygame.transform.scale(image, (self.ICON_SIZE, self.ICON_SIZE))
            result[name] = image
        return result

    def toggle(self):
        self.active = not self.active

    def handle_input(self, event):
        if not self.active:
            return

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(self.icon_rects):
                if rect.collidepoint(mouse_pos):
                    selected = self.buildings[i]
                    self.builder.select(selected)
                    self.builder.is_placing = True
                    self.active = False  # Закрыть UI
                    break

    def draw(self, surface):
        self.buildings = self.builder.get_available_buildings()
        if not self.active:
            return

        self.icon_rects = []
        x, y = 50, 100
        for i, name in enumerate(self.buildings):
            if name not in self.icons:
                data = self.builder.building_data.get(name)
                path = os.path.join("assets", "buildings", data["image"])
                image = pygame.image.load(path).convert_alpha()
                image = pygame.transform.scale(image, (self.ICON_SIZE, self.ICON_SIZE))
                self.icons[name] = image

            icon = self.icons[name]

            rect = pygame.Rect(x, y + i * (self.ICON_SIZE + self.PADDING), self.ICON_SIZE, self.ICON_SIZE)
            surface.blit(icon, rect.topleft)
            self.icon_rects.append(rect)

            label = self.font.render(name, True, self.settings.white)
            surface.blit(label, (rect.right + 5, rect.top + 10))
