from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.king import King
from pieces.queen import Queen
from settings import LIGHT_SQUARE, DARK_SQUARE
from square import Square

class Board:
    def __init__(self, size=8):
        self.size = size
        self.squares = [[None for _ in range(size)] for _ in range(size)]
        self.initialize_board()

    def initialize_board(self):
        """Инициализация доски: создание клеток и размещение фигур."""
        # Создаем клетки
        for row in range(self.size):
            for col in range(self.size):
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                self.squares[row][col] = Square(row, col, color)

        # # Расставляем белые фигуры
        # self.place_piece(Rook('white', 0, 0))
        # self.place_piece(Knight('white', 0, 1))
        # self.place_piece(Bishop('white', 0, 2))
        # self.place_piece(Queen('white', 0, 3))
        # self.place_piece(King('white', 0, 4))
        # self.place_piece(Bishop('white', 0, 5))
        # self.place_piece(Knight('white', 0, 6))
        # self.place_piece(Rook('white', 0, 7))
        # for col in range(8):
        #     self.place_piece(Pawn('white', 1, col))

        # # Расставляем черные фигуры
        # self.place_piece(Rook('black', 7, 0))
        # self.place_piece(Knight('black', 7, 1))
        # self.place_piece(Bishop('black', 7, 2))
        # self.place_piece(Queen('black', 7, 3))
        # self.place_piece(King('black', 7, 4))
        # self.place_piece(Bishop('black', 7, 5))
        # self.place_piece(Knight('black', 7, 6))
        # self.place_piece(Rook('black', 7, 7))
        # for col in range(8):
        #     self.place_piece(Pawn('black', 6, col))

    def place_piece(self, piece):
        """Размещение фигуры на доске."""
        self.squares[piece.row][piece.col].piece = piece

    def draw(self, screen, square_size):
        """Отрисовка доски и фигур."""
        for row in range(self.size):
            for col in range(self.size):
                self.squares[row][col].draw(screen, square_size)
                if self.squares[row][col].piece:
                    self.squares[row][col].piece.draw(screen, square_size)