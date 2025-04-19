from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)

    def draw(self, screen, square_size):
        """Отрисовка пешки."""
        # Пример отрисовки круга для пешки
        center_x = self.col * square_size + square_size // 2
        center_y = self.row * square_size + square_size // 2
        radius = square_size // 3
        pygame.draw.circle(screen, (255, 0, 0), (center_x, center_y), radius)