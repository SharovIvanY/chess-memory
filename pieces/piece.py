import pygame

class Piece:
    def __init__(self, color, row, col):
        self.color = color  # Цвет фигуры ('white' или 'black')
        self.row = row
        self.col = col

    def draw(self, screen, square_size):
        """Отрисовка фигуры на экране (заглушка)."""
        pass  # Реализация будет в подклассах

    def get_valid_moves(self, board):
        """Получение списка допустимых ходов (заглушка)."""
        return []  # Реализация будет в подклассах