class Camera:
    def __init__(self, settings):
        self.offset_x = 0
        self.offset_y = 0
        self.settings = settings
        self.screen_width = settings.screen_width
        self.screen_height = settings.screen_height

    def update(self, target_rect):
        self.offset_x = target_rect.centerx - self.screen_width // 2
        self.offset_y = target_rect.centery - self.screen_height // 2

    def reverse_apply(self, pos):
        """Переводит экранные координаты в мировые."""
        x, y = pos
        return (x + self.offset_x, y + self.offset_y)

    def apply(self, rect):
        return rect.move(-self.offset_x, -self.offset_y)
