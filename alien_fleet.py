import pygame
from typing import TYPE_CHECKING

from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
   

class AlienFleet: 
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.aliens = pygame.sprite.Group()  # Group to hold all aliens in the fleet
        self.fleet_direction = self.settings.fleet_direction  # 1 for right, -1 for left
        self.fleet_drop_speed = self.settings.fleet_drop_speed  # Speed at which the fleet drops down

        self.create_fleet()  # Create the initial fleet of aliens

    def create_fleet(self):
        self.aliens.empty()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        alien_width = self.settings.alien_width
        alien_height = self.settings.alien_height
        screen_width = self.screen.get_rect().width
        screen_height = self.screen.get_rect().height

        fleet_width, fleet_height = self.calculate_fleet_size(alien_width, screen_width, alien_height, screen_height)
        x_offset, y_offset = self.calculate_offsets(alien_width, alien_height, screen_width, screen_height, fleet_width, fleet_height)

        
        self._create_rectangle_fleet(alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset):
        for row in range(fleet_height):
            for col in range(fleet_width):
                current_x = alien_width * col + x_offset
                current_y = alien_height * row + y_offset
                # Alternate columns between rows to create a staggered effect
                if (col + row) % 2 == 0:
                    continue
                self.create_alien(current_x, current_y)

    def calculate_offsets(self, alien_width, alien_height, screen_width, screen_height, fleet_width, fleet_height):
        fleet_horizontal_spacing = fleet_width * alien_width
        fleet_vertical_spacing = fleet_height * alien_height
        x_offset = (screen_width - fleet_horizontal_spacing) // 2
        y_offset = self.settings.hud_height + 20
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_width, screen_width, alien_height, screen_height):
        fleet_width = (screen_width//alien_width)
        fleet_height = (screen_height // 2) // alien_height

        if fleet_width % 2 == 0:
            fleet_width -= 1  
        else:
            fleet_width -= 2 
        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2
        
        return fleet_width, fleet_height


    def create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self, current_x, current_y)
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        alien: 'Alien'
        for alien in self.aliens:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet (self):
        for alien in self.aliens:
            alien.y += self.fleet_drop_speed
            alien.rect.y = alien.y
    def update_fleet(self):
        self._check_fleet_edges()  # Check if any alien has reached the edge of the screen
        self.aliens.update()  # Update the position of the fleet based on the current direction


    def draw(self):
        alien: 'Alien'
        for alien in self.aliens:
            alien.draw_alien()

    def check_collisions(self, othergroup):
        return pygame.sprite.groupcollide(self.aliens, othergroup, True, True)
