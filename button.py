import pygame

class Button: 
    def __init__(self, game, msg):
        self.screen = game.screen
        settings = game.settings
        self.color = settings.button_color
        self.font = pygame.font.Font(settings.font_name, settings.button_font_size)
        self.rect = pygame.Rect(0, 0, settings.button_width, settings.button_height)
        self.rect.center = self.screen.get_rect().center
        self.msg_image = self.font.render(msg, True, settings.button_text_color)

    def draw_button(self):
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=10)
        self.screen.blit(self.msg_image, self.msg_image.get_rect(center=self.rect.center))

    def is_clicked(self, position):
        return self.rect.collidepoint(position)
