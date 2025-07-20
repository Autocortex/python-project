import pygame

class InventoryUI:
    def __init__(self, inventory, settings):
        self.inventory = inventory
        self.settings = settings
        self.font = pygame.font.SysFont(None, 24)

        # Размеры окна (можно будет сделать адаптивными)
        self.margin = 10
        self.padding = 8
        self.bg_color = (30, 30, 30)
        self.border_color = (80, 80, 80)
        self.text_color = settings.white

    def draw(self, surface):
        items = list(self.inventory.all_items())
        width = 200
        line_height = 26
        height = line_height * len(items) + self.padding * 2

        x = self.margin
        y = self.margin

        # Фон и рамка
        bg_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(surface, self.bg_color, bg_rect)
        pygame.draw.rect(surface, self.border_color, bg_rect, 2)

        # Текстовые элементы
        text_y = y + self.padding
        for item, count in items:
            text = self.font.render(f"{item}: {count}", True, self.text_color)
            surface.blit(text, (x + self.padding, text_y))
            text_y += line_height
