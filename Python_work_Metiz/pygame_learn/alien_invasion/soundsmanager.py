import pygame

class SoundsManager():

    def __init__(self):
        """Initial resouses for SoundsManager"""
        self.shoot_sound = pygame.mixer.Sound("sounds/bullet.mp3")
        self.shoot_sound.set_volume(0.3)
        self.ship_left_sound = pygame.mixer.Sound("sounds/ship_left.mp3")
        self.ship_left_sound.set_volume(0.3)
