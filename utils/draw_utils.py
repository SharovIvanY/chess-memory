import pygame
from settings import SQUARE_SIZE

def draw_text(screen, text, size, color, x, y):
    """
    Отрисовка текста на экране.
    :param screen: Объект pygame.Surface (экран).
    :param text: Текст для отрисовки.
    :param size: Размер шрифта.
    :param color: Цвет текста.
    :param x: Координата X центра текста.
    :param y: Координата Y центра текста.
    """
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def highlight_square(screen, row, col, square_size):
    """
    Подсветка клетки на доске.
    :param screen: Объект pygame.Surface (экран).
    :param row: Строка клетки.
    :param col: Столбец клетки.
    :param square_size: Размер одной клетки.
    """
    if row == -1 or col == -1:  # Если фигура справа от доски
        return
    highlight_color = (255, 255, 0, 100)  # Полупрозрачный жёлтый цвет
    rect = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    rect.fill(highlight_color)
    screen.blit(rect, (col * square_size, row * square_size))