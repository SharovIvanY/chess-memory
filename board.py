from square import Square
from settings import BOARD_SIZE, LIGHT_SQUARE, DARK_SQUARE

class Board:
    def __init__(self, size=BOARD_SIZE):
        self.size = size
        self.squares = [[None for _ in range(size)] for _ in range(size)]
        self.initialize_board()

    def initialize_board(self):
        """Инициализация доски: создание клеток."""
        for row in range(self.size):
            for col in range(self.size):
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                self.squares[row][col] = Square(row, col, color)

    def draw(self, screen, square_size):
        """Отрисовка доски."""
        for row in range(self.size):
            for col in range(self.size):
                self.squares[row][col].draw(screen, square_size)