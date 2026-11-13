"""Program Name: Neon Defender Settings
Author: Xavier Chitison
Purpose: Configure original Track 2 Milestone 1 assets and gameplay.
Starter Code Links: https://github.com/XavierChitison/alien_Invasion_starter
Date Updated: 2026-11-13
"""
from pathlib import Path


class Settings:
    """Centralize paths and gameplay settings."""

    def __init__(self):
        """Configure original neon visuals, sound, and ship controls."""
        root = Path(__file__).resolve().parent
        self.name = "Neon Defender - Track 2"
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = root / "Assets" / "images" / "neon_background.png"
        self.ship_file = root / "Assets" / "images" / "neon_ship.png"
        self.ship_width = 100
        self.ship_height = 100
        self.bullet_file = root / "Assets" / "images" / "neon_laser.png"
        self.laser_sound = root / "Assets" / "sound" / "neon_laser.wav"
        self.bullet_width = 22
        self.bullet_height = 72
        self.bullets_allowed = 5
        self.ship_speed = 5.0
        self.bullet_speed = 7.0
        # Reserved for Milestones 2 and 3; not active in this milestone.
        self.alien_file = root / "Assets" / "images" / "enemy_4.png"
        self.alien_width = 40
        self.alien_height = 40
        self.ship_lives = 3
        self.fleet_speed = 1.0
        self.fleet_direction = 1
        self.fleet_drop_speed = 20
        self.speedup_scale = 1.1

    def initialize_dynamic_settings(self):
        """Reset movement speeds for later milestones."""
        self.ship_speed = 5.0
        self.bullet_speed = 7.0
        self.fleet_speed = 1.0
        self.fleet_direction = 1

    def increase_difficulty(self):
        """Increase movement speed for later milestones."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.fleet_speed *= self.speedup_scale
