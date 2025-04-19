import pygame
import random
from settings import BOARD_SIZE, WINDOW_SIZE, SQUARE_SIZE, LIGHT_SQUARE_COLOR, DARK_SQUARE_COLOR, BUTTON_COLOR, BUTTON_HOVER_COLOR, TEXT_COLOR, WHITE, BLACK
from utils.draw_utils import draw_text, highlight_square
from utils.generate_pieces import generate_available_pieces
from utils.button import Button
from utils.board import Board

def play_game(screen, difficulty, piece_images):
    # Создание доски
    board = Board()

    # Генерация фигур в зависимости от сложности
    all_pieces = generate_available_pieces(difficulty)

    # Размещение фигур в правой области
    for i, piece in enumerate(all_pieces):
        piece.row = i  # Начальная строка в правой области
        piece.col = 8  # Столбец правой области
        piece.initial_row = i  # Фиксируем начальную строку
        # Размещение фигур на случайных клетках доски
        initial_positions = {}  # Словарь для хранения начальных позиций фигур
        
    for piece in all_pieces:
        row, col = random.randint(0, 7), random.randint(0, 7)
        piece.row, piece.col = row, col
        initial_positions[piece] = (row, col)

    # Два списка для игры
    pieces_on_board = all_pieces[:]  # Фигуры на доске
    pieces_on_right = []  # Фигуры справа от доски

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

    # Показ фигур на доске (показ на 3 секунды)
    start_time = pygame.time.get_ticks()
    show_right_area = False

    while True:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'menu'  # Возвращаемся в главное меню

            # Выбор фигуры справа от доски
            if event.type == pygame.MOUSEBUTTONDOWN and not selected_piece and show_right_area:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE

                for piece in pieces_on_right + pieces_on_board:
                    if piece.row == clicked_row and piece.col == clicked_col:
                        selected_piece = piece
                        print(f"Подсветка клетки: row={selected_piece.row}, col={selected_piece.col}")
                        break
                


            # Размещение выбранной фигуры на доске
            if event.type == pygame.MOUSEBUTTONDOWN and selected_piece:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE

                # Проверка, что координаты находятся внутри доски
                if 0 <= clicked_row < BOARD_SIZE and 0 <= clicked_col < BOARD_SIZE:
                    # Проверка, что клетка свободна
                    if all(piece.row != clicked_row or piece.col != clicked_col for piece in pieces_on_board):
                        selected_piece.row = clicked_row
                        selected_piece.col = clicked_col

                        # Перемещаем фигуру из одного списка в другой
                        if selected_piece not in pieces_on_board:
                            pieces_on_board.append(selected_piece)
                        if selected_piece in pieces_on_right:
                            pieces_on_right.remove(selected_piece)
                        print(f"Размещение фигуры в клетке: row={selected_piece.row}, col={selected_piece.col}")
                        print(f"Фигуры на доске: {pieces_on_board} Фигуры справа: {pieces_on_right}")
                        selected_piece = None  # Сбрасываем выбор после размещения

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
        board.draw(screen)

        # Отрисовка правой части (чёрный фон)
        pygame.draw.rect(screen, BLACK, (8 * SQUARE_SIZE, 0, SQUARE_SIZE, WINDOW_SIZE))

        # Логика показа фигур
        if elapsed_time >= 3:  # Таймер завершен (через 3 секунды)
            if not show_right_area:
                # Перемещаем фигуры на правую область
                for i, piece in enumerate(pieces_on_board[:]):
                    piece.row, piece.col = i, 8  # Размещаем фигуру в правой области
                    pieces_on_right.append(piece)
                    pieces_on_board.remove(piece)
                show_right_area = True
        
        # Отрисовка фигур на доске
        for piece in pieces_on_board:
            piece.draw(screen, SQUARE_SIZE, images=piece_images, available_pieces=pieces_on_board)
        
        
        # Отрисовка фигур справа
        if show_right_area:
            for piece in pieces_on_right:
                piece.draw(screen, SQUARE_SIZE, images=piece_images, available_pieces=pieces_on_right)

        # Подсветка выбранной фигуры
        if selected_piece:
            # print(f"Подсветка клетки: row={selected_piece.row}, col={selected_piece.col}")
            highlight_square(screen, selected_piece.row, selected_piece.col, SQUARE_SIZE)

        # Отрисовка кнопки "Проверить"
        if show_right_area:
            check_button.draw(screen)

        # Отображение таймера
        if not show_right_area:
            draw_text(screen, f"Осталось: {max(0, int(3 - elapsed_time))} сек", 36, BLACK, WINDOW_SIZE // 2, 20)

        pygame.display.flip()