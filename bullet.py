"""Program Name: Neon Defender Laser
Author: Xavier Chitison
Purpose: Display and animate original custom laser artwork.
Starter Code Links: https://github.com/XavierChitison/alien_Invasion_starter
Date Updated: 2026-11-13
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Represent a moving neon laser projectile."""

    def __init__(self, game):
        """Create a laser at the ship's nose."""
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.image = pygame.image.load(str(self.settings.bullet_file)).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, (self.settings.bullet_width, self.settings.bullet_height))
        self.rect = self.image.get_rect()
        self.rect.midbottom = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move the laser upward."""
        self.y -= self.settings.bullet_speed
        self.rect.y = round(self.y)

    def draw_bullet(self):
        """Draw the laser sprite."""
        self.screen.blit(self.image, self.rect)
