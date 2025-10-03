class Settings():
    """A class to store all settings for Alien Invasion, including ship_limit (lives)."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

#speed
        self.ship_speed_factor = 1
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 5

        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (0,0,0)
        self.bullets_amount = 3

        # 1 = right, -1 = left
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Ship limit (lives)
        self.ship_limit = 3

        # How much to speed up per level
        self.speedup_scale = 1.1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale


