from .piece import Piece


class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)