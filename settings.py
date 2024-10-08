class Settings:
    """ A class to store all settings for Alien Invasion. """

    def __init__(self) -> None:
        """ Initialize the game's settings """
        # --- Screen settings ---
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # --- Ship settings ---
        self.ship_speed = 3
        self.ship_limit = 3

        # --- Bullet settings ---
        self.bullet_speed = 2.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5

        # --- Alien settings ---
        self.alien_speed = 1
        self.fleet_drop_speed = 100
        # fleet direction of 1 represents right; -1 represent left.
        self.fleet_direction = 1

