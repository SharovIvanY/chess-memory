class Piece:
    def __init__(self, color, row, col):
        self.color = color  # Цвет фигуры ('white' или 'black')
        self.row = row
        self.col = col

    def draw(self, screen, square_size):
        """Отрисовка фигуры на экране (заглушка)."""
        pass  # Реализация будет в подклассах