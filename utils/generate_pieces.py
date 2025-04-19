import random
from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn

def generate_available_pieces(difficulty):
    """
    Генерирует список доступных фигур в зависимости от уровня сложности.
    :param difficulty: Уровень сложности (от 1 до 8).
    :return: Список фигур.
    """
    if isinstance(difficulty, str):
        difficulty = int(difficulty)
        
    piece_classes = [King, Queen, Rook, Bishop, Knight, Pawn]
    num_pieces = min(difficulty, len(piece_classes))  # Количество фигур зависит от сложности
    selected_classes = random.sample(piece_classes, num_pieces)

    available_pieces = []
    for PieceClass in selected_classes:
        color = random.choice(['white', 'black'])
        piece = PieceClass(color=color, row=-1, col=-1)  # Фигуры начинаются справа от доски
        available_pieces.append(piece)

    return available_pieces