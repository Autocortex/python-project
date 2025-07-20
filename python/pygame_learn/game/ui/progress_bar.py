import pygame

class ProgressBar:
    def __init__(self, width, height, bg_color=(50, 50, 50), fg_color=(0, 200, 0)):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color

    def draw(self, surface, position, progress, camera=None):
        """
        surface     — экран
        position    — (x, y) мировая позиция (верхняя точка бара)
        progress    — от 0.0 до 1.0
        camera      — объект Camera (если есть смещение)
        """
        x, y = position
        if camera:
            x, y = camera.apply(pygame.Rect(x, y, 0, 0)).topleft

        # фон
        bg_rect = pygame.Rect(x, y, self.width, self.height)
        pygame.draw.rect(surface, self.bg_color, bg_rect)

        # передний план
        fg_width = int(self.width * max(0, min(progress, 1)))
        fg_rect = pygame.Rect(x, y, fg_width, self.height)
        pygame.draw.rect(surface, self.fg_color, fg_rect)
