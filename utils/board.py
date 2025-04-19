import pygame
from settings import LIGHT_SQUARE_COLOR, DARK_SQUARE_COLOR, SQUARE_SIZE

class Board:
    def __init__(self):
        self.grid = [[(i + j) % 2 for j in range(8)] for i in range(8)]  # Шахматная раскраска

    def draw(self, screen, square_size):
        """Отрисовка доски."""
        for row in range(8):
            for col in range(8):
                color = LIGHT_SQUARE_COLOR if self.grid[row][col] == 0 else DARK_SQUARE_COLOR
                pygame.draw.rect(
                    screen,
                    color,
                    (col * square_size, row * square_size, square_size, square_size)
                )