"""
Program Name: alien_invasion.py
Author: Natan Ejigu 
Purpose: Main driver file for the Alien Invasion game, Track 1
         (Custom Game Mechanics) - Milestone 1. The ship is
         positioned at the top of the screen, moves left and right,
         and fires bullets downward.
Starter code: Based on the Alien Invasion project from Python Crash
    Course, 3rd Edition, by Eric Matthes
Date: July,24 2026
"""

import sys
from time import sleep
import pygame

import alien
from settings import Settings
from ship import Ship
from bullet import Bullet 
from alien import Alien
from game_stats import GameStats


class AlienInvasion:
    """Overall class to manage game assets and behavior."""
 
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
 
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion - Track 1")

        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        # Start Alien Invasion in an active state.
        self.game_active = True

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        # Respond to keypresses.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
 
    def _check_keyup_events(self, event):
        # Respond to key releases.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group, up to the number allowed at once."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
 
    def _update_bullets(self):
        """Update bullet positions and remove bullets that have
        traveled off the bottom of the screen."""
        self.bullets.update()
 
        for bullet in self.bullets.copy():
            if bullet.rect.top > self.settings.screen_height:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens and if that is the case,  get rid of the bullet and the alien.
        self._check_bullet_alien_collisions()
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisionsand and remove any bullets and aliens that have collided."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
 
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
    
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the top of the screen (behind ship).
        self._check_aliens_top()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_top(self):
        """Check if any aliens have reached the top of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.top <= 0:
                self._ship_hit()
                break

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no
        # room left. Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x = alien_width

        # Start the first row near the BOTTOM of the screen and build rows upward from there. 

        current_y = self.settings.screen_height - 2 * alien_height
        while current_y > 3 * alien_height:
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
 
            # Finished a row; reset x value, and decrement y value
            # so the next row is placed further UP the screen.
            current_x = alien_width
            current_y -= 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond  if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
 
    def _change_fleet_direction(self):
        """Rise the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

      
 
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
