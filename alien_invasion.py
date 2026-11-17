"""Program Name: Neon Defender - Alien Invasion (Track 2, Milestone 1)
Author: Xavier Chitison
Purpose: Run the customized ship, background, laser and laser audio demo.
Starter Code Links: https://github.com/XavierChitison/alien_Invasion_starter
Date Updated: 2026-11-13
"""
import sys
import pygame
from Settings import Settings
from asset_generator import generate_assets
from ship import Ship
from arsenal import ShipArsenal


class AlienInvasion:
    """Run Milestone 1 without later-milestone gameplay features."""

    def __init__(self):
        """Initialize custom assets, player ship, bullets and optional sound."""
        generate_assets()
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.name)
        self.bg = pygame.image.load(str(self.settings.bg_file)).convert()
        self.bg = pygame.transform.scale(self.bg, self.screen.get_size())
        self.clock = pygame.time.Clock()
        self.running = True
        self.arsenal = ShipArsenal(self)
        self.ship = Ship(self, self.arsenal)
        self.laser_sound = None
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
            self.laser_sound.set_volume(0.4)
        except pygame.error:
            print("Audio unavailable; visual demo will continue.")

    def run_game(self):
        """Update the ship and lasers until the player exits."""
        while self.running:
            self._check_events()
            self.ship.update()
            self.arsenal.update_arsenal()
            self._updated_screen()
            self.clock.tick(self.settings.FPS)
        pygame.quit()

    def _updated_screen(self):
        """Draw only the Milestone 1 custom assets and player projectiles."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.arsenal.draw()
        pygame.display.flip()

    def _check_events(self):
        """Process movement, shooting, and quitting."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Start moving or fire a custom laser on key press."""
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = True
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire() and self.laser_sound:
                self.laser_sound.play()
        elif event.key in (pygame.K_q, pygame.K_ESCAPE):
            self.running = False

    def _check_keyup_events(self, event):
        """Stop ship movement when a directional key is released."""
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = False
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = False


if __name__ == "__main__":
    AlienInvasion().run_game()
