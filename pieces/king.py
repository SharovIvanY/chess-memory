from .piece import Piece
import pygame


class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def draw(self, screen, square_size):
        """Отрисовка короля."""
        center_x = self.col * square_size + square_size // 2
        center_y = self.row * square_size + square_size // 2
        color = (255, 0, 0) if self.color == 'white' else (0, 0, 255)
        pygame.draw.circle(screen, color, (center_x, center_y), square_size // 6)
        pygame.draw.line(screen, color, (center_x, center_y - square_size // 4), (center_x, center_y + square_size // 4), 3)