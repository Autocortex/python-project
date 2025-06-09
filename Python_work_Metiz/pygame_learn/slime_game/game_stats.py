class GameStats():
    """Game stats"""
    def __init__(self,slimegame):
        """Initial resourse for gamestats"""
        self.settings = slimegame.settings
        self.reset_stats()

    def reset_stats(self):
        """Initial stats."""
        self.enemies_score =self.settings.score_enemies
        self.counter_slime = self.settings.slime_counter
        self.health_slime = self.settings.slime_health