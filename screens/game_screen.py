import pygame
import random
from settings import WINDOW_SIZE, SQUARE_SIZE, LIGHT_SQUARE_COLOR, DARK_SQUARE_COLOR, BUTTON_COLOR, BUTTON_HOVER_COLOR, TEXT_COLOR, WHITE, BLACK
from utils.draw_utils import draw_text, highlight_square
from utils.generate_pieces import generate_available_pieces
from utils.button import Button
from utils.board import Board

def play_game(screen, difficulty):
    # Создание доски
    board = Board()

    # Генерация фигур в зависимости от сложности
    all_pieces = generate_available_pieces(difficulty)

    # Размещение фигур на случайных клетках доски
    initial_positions = {}  # Словарь для хранения начальных позиций фигур
    for piece in all_pieces:
        row, col = random.randint(0, 7), random.randint(0, 7)
        piece.row, piece.col = row, col
        initial_positions[piece] = (row, col)

    # Два списка для игры
    pieces_on_right = all_pieces[:]  # Фигуры справа от доски
    pieces_on_board = []  # Фигуры на доске

    selected_piece = None  # Текущая выбранная фигура

    # Кнопка "Проверить"
    check_button = Button(
        x=0,  # Начинается с левого края
        y=WINDOW_SIZE - SQUARE_SIZE,  # Последняя строка
        width=WINDOW_SIZE,  # Занимает всю ширину экрана
        height=SQUARE_SIZE,
        text="Проверить",
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    # Показ фигур на доске (показ на 5 секунд)
    show_piece = True
    start_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Выбор фигуры справа от доски
            if event.type == pygame.MOUSEBUTTONDOWN and not show_piece:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(f"Клик мыши: ({mouse_x}, {mouse_y})")  # Отладка: координаты клика

                for i, piece in enumerate(pieces_on_right):
                    piece_center_x = 8 * SQUARE_SIZE + SQUARE_SIZE // 2  # Центр последней колонки
                    piece_center_y = i * SQUARE_SIZE + SQUARE_SIZE // 2  # Центр текущей строки
                    print(f"Центр фигуры: ({piece_center_x}, {piece_center_y})")  # Отладка: центр фигуры

                    # Проверяем, попал ли клик в центр клетки
                    if abs(mouse_x - piece_center_x) < SQUARE_SIZE // 4 and abs(mouse_y - piece_center_y) < SQUARE_SIZE // 4:
                        selected_piece = piece  # Выбираем фигуру
                        print(f"Выбрана фигура: {selected_piece}")  # Отладка: выбранная фигура
                        break

            # Размещение выбранной фигуры на доске
            if event.type == pygame.MOUSEBUTTONDOWN and selected_piece:
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE
                print(f"Клик по доске: строка={clicked_row}, столбец={clicked_col}")  # Отладка: координаты клика

                # Проверка, что координаты находятся внутри доски
                if 0 <= clicked_row < 8 and 0 <= clicked_col < 8:
                    print(f"Перемещение фигуры на: строка={clicked_row}, столбец={clicked_col}")  # Отладка: перемещение
                    selected_piece.row = clicked_row
                    selected_piece.col = clicked_col

                    # Перемещаем фигуру из одного списка в другой
                    pieces_on_board.append(selected_piece)
                    pieces_on_right.remove(selected_piece)

                    selected_piece = None  # Сбрасываем выбор после размещения
                else:
                    print("Клик за пределами доски!")  # Отладка: клик вне доски

            # Проверка результата
            if event.type == pygame.MOUSEBUTTONDOWN and check_button.is_clicked(pygame.mouse.get_pos()):
                all_correct = True
                for piece, (initial_row, initial_col) in initial_positions.items():
                    if piece.row != initial_row or piece.col != initial_col:
                        all_correct = False
                        break
                return "win" if all_correct else "lose"

        # Отрисовка фона
        screen.fill(WHITE)

        # Отрисовка доски
        board.draw(screen, SQUARE_SIZE)

        # Отрисовка правой части (чёрный фон)
        pygame.draw.rect(screen, BLACK, (8 * SQUARE_SIZE, 0, SQUARE_SIZE, WINDOW_SIZE))
        
        # Показ фигур на доске (показ на 5 секунд)
        if show_piece and elapsed_time < 5:
            for piece in all_pieces:
                piece.draw(screen, SQUARE_SIZE, available_pieces=[])
        else:
            if show_piece:  # Если таймер только истёк
                print("Таймер истёк! Перемещаем фигуры справа.")  # Отладка
                for piece in all_pieces:
                    piece.row, piece.col = -1, -1  # Перемещаем фигуру справа от доски
                show_piece = False  # Отключаем режим показа фигур

            # Отрисовка фигур справа от доски
            for i, piece in enumerate(pieces_on_right):
                piece_center_x = 8 * SQUARE_SIZE + SQUARE_SIZE // 2  # Центр последней колонки
                piece_center_y = i * SQUARE_SIZE + SQUARE_SIZE // 2  # Центр текущей строки
                piece.draw(screen, SQUARE_SIZE, available_pieces=pieces_on_right)

        # Отрисовка фигур на доске
        for piece in pieces_on_board:
            piece.draw(screen, SQUARE_SIZE, available_pieces=pieces_on_board)

        # Подсветка выбранной фигуры
        if selected_piece:
            highlight_square(screen, selected_piece.row, selected_piece.col, SQUARE_SIZE)

        # Отрисовка кнопки "Проверить"
        if not show_piece:
            check_button.draw(screen)

        # Отображение таймера
        if show_piece:
            draw_text(screen, f"Осталось: {5 - int(elapsed_time)} сек", 36, BLACK, WINDOW_SIZE // 2, 20)

        pygame.display.flip()