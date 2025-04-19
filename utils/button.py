import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font_size = font_size
        self.is_hovered = False

    def draw(self, screen):
        """Отрисовка кнопки."""
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)

        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        """Проверка, был ли клик по кнопке."""
        return self.rect.collidepoint(pos)

    def update_hover(self, pos):
        """Обновление состояния наведения."""
        self.is_hovered = self.rect.collidepoint(pos)