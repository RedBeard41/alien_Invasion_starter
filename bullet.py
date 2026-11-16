"""
Program Name: Neon Space Shooter - Track 2
Author: Colin Lee
Purpose: Manage the custom laser projectiles fired by the spaceship.
Starter Code Links: https://github.com/RedBeard41/alien_invasion_starter
Project Repository: https://github.com/clee0106/alien_Invasion_starter/tree/track_2_assets
Date Updated: November 15, 2026
"""
import pygame
from pathlib import Path
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        laser_path = Path(__file__).resolve().parent / "Assets" / "images" / "laserBlast.png"
        self.image = pygame.image.load(str(laser_path)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (12, 35))

        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the custom laser image to the screen."""
        self.screen.blit(self.image, self.rect)