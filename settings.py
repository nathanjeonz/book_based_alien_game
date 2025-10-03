class Settings():
    """A class to store all settings for Alien Invasion."""
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

#1 = right, -1 = left
        self.fleet_drop_speed = 1
        self.fleet_direction = 1

       
