"""Program Name: Neon Defender Arsenal
Author: Xavier Chitison
Purpose: Create and manage custom neon lasers.
Starter Code Links: https://github.com/XavierChitison/alien_Invasion_starter
Date Updated: 2026-11-13
"""
import pygame
from bullet import Bullet


class ShipArsenal:
    """Manage active player projectiles."""

    def __init__(self, game):
        """Store the game reference and bullet sprite group."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Move lasers and remove those outside the display."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Discard projectiles that have passed the top edge."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom < 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Render all active lasers."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Fire if the simultaneous projectile limit has not been reached."""
        if len(self.arsenal) >= self.settings.bullets_allowed:
            return False
        self.arsenal.add(Bullet(self.game))
        return True
