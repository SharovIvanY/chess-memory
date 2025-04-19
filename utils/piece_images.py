import os
import pygame
from settings import ASSETS_PATH, SQUARE_SIZE
from utils.draw_utils import resource_path  # Импортируем функцию

# Константы для обозначений фигур
PIECE_TYPES = ['K', 'Q', 'R', 'B', 'N', 'P']  # Король, ферзь, ладья, слон, конь, пешка
COLORS = ['b', 'w']  # Черные и белые фигуры

def load_piece_images():
    """
    Загрузка изображений всех шахматных фигур.
    :param square_size: Размер клетки (для масштабирования изображений).
    :return: Словарь с загруженными изображениями фигур или None в случае ошибки.
    """
    images = {}
    all_pieces_loaded = True  # Флаг для проверки успешности загрузки

    for color in COLORS:
        for piece_type in PIECE_TYPES:
            piece_id = f"{color}{piece_type}"  # Например, 'bK' для черного короля
            try:
                # Путь к изображению через resource_path
                image_path = resource_path(os.path.join(ASSETS_PATH, f"{piece_id}.png"))
                # Загрузка изображения
                image = pygame.image.load(image_path)
                # Масштабирование изображения под размер клетки
                image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
                # Добавление изображения в словарь
                images[piece_id] = image
            except pygame.error as e:
                print(f"Ошибка загрузки изображения {piece_id}.png: {e}")
                all_pieces_loaded = False

    return images if all_pieces_loaded else None