import pygame
import time

class WaveTimer:
    def __init__(self, font, wave_interval_sec=30):
        self.font = font
        self.start_time = time.time()
        self.wave_interval = wave_interval_sec  # интервал между волнами (в секундах)
        self.current_wave = 0
        self.wave_triggered = False

    def update(self):
        elapsed = time.time() - self.start_time
        if elapsed >= self.wave_interval:
            self.start_time = time.time()
            self.current_wave += 1
            self.wave_triggered = True
        else:
            self.wave_triggered = False

    def draw(self, surface, screen_width):
        remaining = max(0, int(self.wave_interval - (time.time() - self.start_time)))
        minutes = remaining // 60
        seconds = remaining % 60
        text = f"Следующая волна через: {minutes:02}:{seconds:02} | Волна: {self.current_wave + 1}"
        img = self.font.render(text, True, (255, 255, 255))
        surface.blit(img, (screen_width // 2 - img.get_width() // 2, 10))

    def is_wave_triggered(self):
        return self.wave_triggered
