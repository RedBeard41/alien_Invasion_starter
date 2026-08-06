"""
Program Name: game_stats.py
Author: Natan Ejigu
Purpose: Tracks statistics for the Alien Invasion game, for example,how many ships the player
         has remaining.
Starter code: GameStats class based on the Alien Invasion project
    from Python Crash Course, 3rd Edition, by Eric Matthes
Date: August 1, 2026
"""


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit