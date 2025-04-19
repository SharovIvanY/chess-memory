import pygame
from settings import ASSETS_PATH, SQUARE_SIZE

def load_piece_images():
    """
    Загрузка изображений всех шахматных фигур.
    :return: Словарь с загруженными изображениями фигур.
    """
    # Список всех возможных фигур (буквы обозначают цвет и тип фигуры)
    pieces = ['bK', 'wK', 'bQ', 'wQ', 'bR', 'wR', 'bB', 'wB', 'bN', 'wN', 'bP', 'wP']
    images = {}

    for piece in pieces:
        try:
            # Путь к изображению
            image_path = f"{ASSETS_PATH}{piece}.png"
            # Загрузка изображения
            image = pygame.image.load(image_path)
            # Масштабирование изображения под размер клетки
            image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
            # Добавление изображения в словарь
            images[piece] = image
        except pygame.error as e:
            print(f"Ошибка загрузки изображения {piece}.png: {e}")
            return None  # Возвращаем None, если произошла ошибка

    return images