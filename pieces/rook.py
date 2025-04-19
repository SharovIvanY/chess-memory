from .piece import Piece
import pygame


class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def draw(self, screen, square_size):
        """Отрисовка ладьи."""
        x = self.col * square_size
        y = self.row * square_size
        color = (255, 0, 0) if self.color == 'white' else (0, 0, 255)
        pygame.draw.rect(screen, color, (x + square_size // 4, y + square_size // 4, square_size // 2, square_size // 2))