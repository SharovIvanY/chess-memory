import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)
        self.is_hovered = False

    def draw(self, screen):
        """Отрисовка кнопки."""
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        """Проверка, находится ли курсор над кнопкой."""
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos):
        """Проверка, была ли кнопка нажата."""
        return self.rect.collidepoint(mouse_pos)