"""Program Name: Neon Defender Ship
Author: Xavier Chitison
Purpose: Draw and move the original neon ship.
Starter Code Links: https://github.com/XavierChitison/alien_Invasion_starter
Date Updated: 2026-11-13
"""
import pygame


class Ship(pygame.sprite.Sprite):
    """Represent the player ship."""

    def __init__(self, game, arsenal):
        """Load custom ship art and position it along the screen bottom."""
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.arsenal = arsenal
        self.boundaries = self.screen.get_rect()
        self.image = pygame.image.load(str(self.settings.ship_file)).convert_alpha()
        self.image = pygame.transform.smoothscale(
            self.image, (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False

    def _center_ship(self):
        """Place the ship at the bottom center."""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update ship movement without leaving the screen."""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        self.x = max(0, min(self.x, self.boundaries.width - self.rect.width))
        self.rect.x = round(self.x)

    def draw(self):
        """Render the ship."""
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Ask the arsenal to create a new laser."""
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        """Reserve collision support for Milestone 2."""
        return pygame.sprite.spritecollideany(self, other_group) is not None
