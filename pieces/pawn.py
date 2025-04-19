from .piece import Piece


class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)