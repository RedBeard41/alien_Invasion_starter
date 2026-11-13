import pygame


class HUD:
    # Display live game statistics, including the record loaded by GameStats.

    def __init__(self, game):
        self.screen = game.screen
        self.stats = game.stats
        self.settings = game.settings
        self.label_font = pygame.font.Font(self.settings.font_name, 24)
        self.value_font = pygame.font.Font(self.settings.font_name, 36)
        self.ship_icon = pygame.transform.smoothscale(game.ship.image, (36, 36))

    def draw(self):
        width = self.screen.get_width()
        height = self.settings.hud_height
        pygame.draw.rect(self.screen, (12, 20, 35), (0, 0, width, height))
        pygame.draw.line(self.screen, (70, 160, 200),
                         (0, height - 1), (width, height - 1), 2)
        columns = ((20, 'CURRENT SCORE', f'{self.stats.score:,}'),
                   (width // 3, 'MAX / HIGH SCORE', f'{self.stats.high_score:,}'),
                   (width * 2 // 3, 'LEVEL', str(self.stats.level)))
        for x, label, value in columns:
            self.screen.blit(self.label_font.render(label, True, (155, 190, 210)), (x, 12))
            self.screen.blit(self.value_font.render(value, True, (255, 255, 255)), (x, 40))
        lives_x = width - max(160, self.stats.ship_limit * 40 + 20)
        self.screen.blit(self.label_font.render('LIVES', True, (155, 190, 210)),
                         (lives_x, 12))
        for life in range(self.stats.lives_remaining):
            self.screen.blit(self.ship_icon, (lives_x + life * 40, 36))
