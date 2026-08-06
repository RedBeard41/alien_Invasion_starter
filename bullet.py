"""
Program Name: bullet.py
Author: Natan Ejigu
Purpose: Manages bullets fired from the ship. Because the ship sits
         at the top of the screen for Track 1, bullets are fired
         DOWNWARD (toward where the aliens will appear in Milestone
         2), rather than upward as in the base class discussion.
Starter code: Bullet class structure based on Python Crash Course,
    3rd Edition, Spawn position and direction of
    travel changed to fire downward from the ship's bottom edge,
    per Track 1 requirements.
Date: July 26, 2026
"""
 
import pygame
from pygame.sprite import Sprite
 
 
class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
 
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
 
        # Create a bullet rect at (0, 0) and then set its correct
        # position at the ship's midbottom, since the ship faces
        # downward and that's where its "front" now is.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midbottom
 
        # Store the bullet's position as a float for smooth movement.
        self.y = float(self.rect.y)
 
    def update(self):
        """Move the bullet down the screen."""
        self.y += self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
 
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
 