class Piece:
    def __init__(self, color, row=-1, col=-1):
        self.color = color  # Цвет фигуры ('white' или 'black')
        self.row = row  # Текущая строка на доске
        self.col = col  # Текущий столбец на доске
        self.initial_row = row  # Начальная строка (для правой области)

    def draw(self, screen, square_size, images=None, available_pieces=None):
        """
        Отрисовка фигуры.
        :param screen: Объект pygame.Surface (экран).
        :param square_size: Размер одной клетки.
        :param images: Словарь с загруженными изображениями фигур.
        :param available_pieces: Список доступных фигур для отрисовки справа от доски.
        """
        if not images:
            raise ValueError("Словарь изображений не передан в метод draw.")

        # Определяем идентификатор фигуры (например, 'bK' для чёрного короля)
        piece_id = f"{'w' if self.color == 'white' else 'b'}{self.__class__.__name__[0]}"

        # Проверяем, есть ли изображение для данной фигуры
        if piece_id not in images:
            print(f"Изображение для фигуры {piece_id} не найдено!")
            return

        # Вычисляем координаты центра фигуры
        if self.col == 8:  # Если фигура справа от доски
            if available_pieces is None or self not in available_pieces:
                return  # Не рисуем фигуру, если она не в списке available_pieces
            piece_center_x = 8 * square_size + square_size // 2  # Центр последней колонки
            piece_center_y = self.initial_row * square_size + square_size // 2  # Фиксированная строка
        elif 0 <= self.row < 8 and 0 <= self.col < 8:  # Если фигура на доске
            piece_center_x = self.col * square_size + square_size // 2
            piece_center_y = self.row * square_size + square_size // 2
        else:
            print(f"Невалидные координаты фигуры: строка={self.row}, столбец={self.col}")
            return  # Не рисуем фигуру с невалидными координатами

        # Отрисовываем изображение фигуры
        image = images[piece_id]
        image_rect = image.get_rect(center=(piece_center_x, piece_center_y))
        screen.blit(image, image_rect)