class GameStats():

    def __init__(self):
        """Resourses for GameStats"""
        # Count collisions parameters
        self.reset_stats()
        # Game active parameters
        self.game_active = False

    def reset_stats(self):
        """Reset stats."""
        self.available_miss_counter = 3
        self.count_collisions = 0
