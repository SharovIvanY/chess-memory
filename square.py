import pygame

class Square:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.piece = None  # Фигура, которая стоит на клетке (изначально пусто)

    def draw(self, screen, square_size):
        """Отрисовка клетки на экране."""
        pygame.draw.rect(
            screen,
            self.color,
            pygame.Rect(self.col * square_size, self.row * square_size, square_size, square_size)
        )