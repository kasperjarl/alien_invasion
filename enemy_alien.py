import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet """
    def __init__(self, ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the ship's exact horizontal and vertical position.
        self.x = float(self.rect.x)

    def update(self):
        """ Update the alien position based on location """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """ Return True if alien is at the edge of the screen. """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def blitme(self):
        """ Draw the ship at it's current location """
        self.screen.blit(self.image, self.rect)
