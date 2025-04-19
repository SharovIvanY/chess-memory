import pygame
from settings import BLACK, SQUARE_SIZE

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


def highlight_square(screen, row, col, square_size, color=(128, 0, 128), alpha=128):
    """
    Подсвечивает клетку на доске.
    :param screen: Объект pygame.Surface (экран).
    :param row: Номер строки клетки.
    :param col: Номер столбца клетки.
    :param square_size: Размер клетки.
    :param color: Цвет подсветки (по умолчанию фиолетовый).
    :param alpha: Прозрачность подсветки (0-255).
    """
    # Создаем поверхность для подсветки
    highlight = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    highlight.fill((*color, alpha))  # Цвет с прозрачностью

    # Рисуем подсветку на экране
    screen.blit(highlight, (col * square_size, row * square_size))
    

def draw_right_area(screen, square_size):
    """
    Рисует правую область (9-й столбец) как сетку с чёрными клетками.
    :param screen: Объект pygame.Surface (экран).
    :param square_size: Размер клетки.
    """
    for row in range(8):  # 8 строк
        pygame.draw.rect(
            screen,
            BLACK,
            (8 * square_size, row * square_size, square_size, square_size)
        )