class Settings():
    """Game settings."""

    def __init__(self):
        """Initiating game settings."""
        self.bg_color = (30,30,30)
        self.width = 800
        self.height = 600
        #Slime settings
        self.slime_speed = 0.8
        self.score_enemies = 0
        self.slime_counter = True
        self.slime_health = 5
        #Setting bullet
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 5
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3 
        #Enemy speed
        self.enemy_speed = 0.2
        self.fleet_drop_speed = 25
        self.fleet_direction = 1