from .piece import Piece
import pygame


class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)