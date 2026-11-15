import pygame
from pathlib import Path
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        ship_path = Path(__file__).resolve().parent / "Assets" / "images" / "ship2(no bg).png"
        self.image = pygame.image.load(str(ship_path)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 100
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 100
        self.x = float(self.rect.x)
         


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)