import pygame
import os

class Animator:
    def __init__(self, path, size):
        """
        path — путь до папки со спрайтами
        size — (width, height)
        """
        self.size = size
        self.frames = {
            "down": self.load_image("player_down.png"),
            "top": self.load_image("player_top.png"),
            "left": self.load_image("player_left.png"),
            "right": self.load_image("player_right.png"),
        }
        self.current_direction = "down"

    def load_image(self, filename):
        full_path = os.path.join("assets", "player", filename)
        image = pygame.image.load(full_path).convert_alpha()
        return pygame.transform.scale(image, self.size)

    def set_direction(self, direction):
        if direction in self.frames:
            self.current_direction = direction

    def get_image(self):
        return self.frames[self.current_direction]
