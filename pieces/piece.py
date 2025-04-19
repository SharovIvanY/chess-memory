import pygame

class Piece:
    def __init__(self, color, row, col):
        self.color = color  # Цвет фигуры ('white' или 'black')
        self.row = row
        self.col = col

    def draw(self, screen, square_size, available_pieces=None):
        """Отрисовка фигуры."""
        if self.row == -1 and self.col == -1:  # Если фигура справа от доски
            if available_pieces is None or self not in available_pieces:
                return  # Не рисуем фигуру, если она не в списке available_pieces
            piece_index = available_pieces.index(self)
            piece_center_x = 8 * square_size + square_size // 2  # Центр последней колонки
            piece_center_y = piece_index * square_size + square_size // 2  # Центр текущей строки
            print(f"Отрисовка справа: x={piece_center_x}, y={piece_center_y}")  # Отладка
        elif 0 <= self.row < 8 and 0 <= self.col < 8:  # Если фигура на доске
            piece_center_x = self.col * square_size + square_size // 2
            piece_center_y = self.row * square_size + square_size // 2
            print(f"Отрисовка на доске: x={piece_center_x}, y={piece_center_y}")  # Отладка
        else:
            print(f"Невалидные координаты фигуры: строка={self.row}, столбец={self.col}")  # Отладка
            return  # Не рисуем фигуру с невалидными координатами

        radius = square_size // 4
        color = (255, 0, 0) if self.color == 'white' else (0, 0, 255)
        pygame.draw.circle(screen, color, (piece_center_x, piece_center_y), radius)