"""
Program Name: alien.py
Author: Natan Ejigu
Purpose: Represents a single alien in the fleet, for Track 1
         (Custom Game Mechanics). Since the ship is positioned at
         the top of the screen and fires downward, the fleet is
         inverted: aliens start near the bottom of the screen and
         will advance upward toward the ship (rather than starting
         at the top and moving down, as in the base book tutorial).
Starter code: Alien class structure based on the Alien Invasion
    project from Python Crash Coursse, Starting position changed
    from near the top-left to near the bottom-left of the screen,
    and alien drawn as a placeholder shape instead of loaded from
    a file, per Track 1 requirements.
Date: July 29, 2026
"""


from pathlib import Path
import pygame
from pygame.sprite import Sprite
 
 
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
 
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
 
        # Load the alien image using pathlib, so the file path
        # works correctly on both Windows and macOS.
        image_path = Path(__file__).parent / 'Assets' / 'images' / 'alien.bmp'
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.rotate(original_image, 180)
        self.rect = self.image.get_rect()
 
        self.rect.x = self.rect.width
        self.rect.y = self.screen.get_rect().height - 2 * self.rect.height
 
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    def update(self):
        """Move the alien to the right  or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x