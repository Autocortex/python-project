class Settings():

    def __init__(self):
        """Initial resourse for Settings"""
        self.width = 1200
        self.height = 800
        self.bg_color = (255, 165, 0)
        # Bullet parameters
        self.bullet_width = 15
        self.bullet_height = 7
        self.bullet_color = (60, 60, 60)
        # Pace of the game
        self.speed_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Dynamic settings."""
        self.player_speed_factor = 1.5
        self.speed_target_factor = 0.5
        self.bullet_speed_factor = 1.5
        # Target parameters
        self.direction_target = 1
        self.last_difficulty_trigger = 0

    def increase_speed(self):
        """Increase speed."""
        self.player_speed_factor *= self.speed_scale
        self.speed_target_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale

    def easy_difficulty(self):
        """Easy difficulty."""
        self.player_speed_factor = 1.5
        self.speed_target_factor = 0.2
        self.bullet_speed_factor = 2

    def hard_difficulty(self):
        """Hard difficulty."""
        self.player_speed_factor = 1
        self.speed_target_factor = 1.5
        self.bullet_speed_factor = 1

