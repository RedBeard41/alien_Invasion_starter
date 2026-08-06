"""
Program Name: ship.py
Author: Natan Ejigu
Purpose: Manages the player's ship for Track 1 (Custom Game
         Mechanics). The ship is loaded from a custom image file
         and positioned at the TOP center of the screen (instead of
         the bottom, as in the base book tutorial), and can move
         left and right in response to player input.
Starter code: Ship class structure based on the Alien Invasion
    project from Python Crash Course, 3rd Edition, by Eric Matthes
    (https://ehmatthes.github.io/pcc_3e). Custom ship artwork
    (ship21.png) supplied by the author and rotated 180 degrees so
    the nose points downward, matching the ship's firing direction.
    Starting position changed from midbottom to midtop, per Track 1
    requirements.
Date: July 25, 2026
"""
from pathlib import Path
 
import pygame
 
 
class Ship:
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
 
        # Load the ship image using pathlib, so the file path works
        # correctly on both Windows and macOS. The image was rotated
        # 180 degrees so its nose points down, since the ship fires
        # downward from the top of the screen.
        image_path = Path(__file__).parent / 'Assets' / 'images' / 'ship21.png'
        original_image = pygame.image.load(image_path).convert_alpha()
 
        # Scale the image down to a game-appropriate size (~80px
        # wide), preserving its original aspect ratio.
        target_width = 80
        scale_factor = target_width / original_image.get_width()
        target_height = int(original_image.get_height() * scale_factor)
        self.image = pygame.transform.smoothscale(
            original_image, (target_width, target_height))
        self.rect = self.image.get_rect()
 
        # Start each new ship at the TOP center of the screen.
        self.rect.midtop = self.screen_rect.midtop
 
        # Store a float for the ship's exact horizontal position, so
        # fractional speed values (e.g. 2.5) aren't lost to integer
        # rounding on every update.
        self.x = float(self.rect.x)
 
        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
 
    def update(self):
        """Update the ship's position based on movement flags,
        without letting it move past the left or right edge of the
        screen."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
 
        # Update rect object from self.x.
        self.rect.x = self.x
 
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centering the ship at the top of the screen."""
        self.rect.midtop = self.screen_rect.midtop
        self.x = float(self.rect.x)