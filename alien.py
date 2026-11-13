import pygame
from pygame.draw import rect
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        super().__init__()
        self.fleet = fleet
        self.settings = fleet.settings
        self.boundaries = fleet.screen.get_rect()
        self.screen = fleet.screen

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_width, self.settings.alien_height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        temp_speed = self.settings.fleet_speed
            
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
       return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
