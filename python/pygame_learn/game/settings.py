class Settings:
    def __init__(self):
        # --- Экран ---
        self.screen_width = 800
        self.screen_height = 600
        self.fps = 60

        # --- Цвета ---
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # --- Игрок ---
        self.player_width = 40  # масштаб спрайта
        self.player_height = 40
        self.player_speed = 2
        # --- Пули ---
        self.bullet_size = 60
        self.bullet_speed = 4
        self.bullet_damage = 1
        self.bullet_color = (255, 200, 0)
        # --- Враги ---
        self.enemy_size = 32
        self.enemy_speed = 1.0
        self.enemy_health = 5
        self.enemy_color = (0, 0, 0)  # чёрный
        # Башни
        self.tower_range = 300  # радиус атаки
        self.tower_cooldown = 1000  # мс между выстрелами
        self.bullet_speed = 6  # скорость пули
        self.bullet_damage = 1
