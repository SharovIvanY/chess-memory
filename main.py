import pygame
import sys
import random
from button import Button
from board import Board
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.king import King
from pieces.queen import Queen
from settings import WINDOW_SIZE, SQUARE_SIZE


# Инициализация PyGame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (50, 150, 50)
BUTTON_HOVER_COLOR = (80, 200, 80)
TEXT_COLOR = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Запоминание положения фигур")


# Функция для отрисовки текста
def draw_text(text, font_size, color, x, y):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


# Функция для создания кнопок
def create_buttons():
    return [
        Button(
            x=WINDOW_SIZE // 4,
            y=WINDOW_SIZE // 2 + 20,
            width=WINDOW_SIZE // 2,
            height=50,
            text="Попробовать еще раз",
            color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER_COLOR,
            text_color=TEXT_COLOR,
            font_size=36
        ),
        Button(
            x=WINDOW_SIZE // 4,
            y=WINDOW_SIZE // 2 + 90,
            width=WINDOW_SIZE // 2,
            height=50,
            text="Выйти в главное меню",
            color=BUTTON_COLOR,
            hover_color=BUTTON_HOVER_COLOR,
            text_color=TEXT_COLOR,
            font_size=36
        )
    ]


# Функция для обработки событий стартового экрана
def handle_start_screen_events():
    # Создание кнопок
    start_button = Button(
        x=WINDOW_SIZE // 4,
        y=WINDOW_SIZE // 2 - 50,
        width=WINDOW_SIZE // 2,
        height=50,
        text="Начать игру",
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    exit_button = Button(
        x=WINDOW_SIZE // 4,
        y=WINDOW_SIZE // 2 + 20,
        width=WINDOW_SIZE // 2,
        height=50,
        text="Выход",
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                # Проверка наведения курсора на кнопки
                start_button.check_hover(pygame.mouse.get_pos())
                exit_button.check_hover(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(pygame.mouse.get_pos()):
                    return "start_game"  # Начать игру
                elif exit_button.is_clicked(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()  # Выйти из игры

        # Отрисовка стартового экрана
        screen.fill(WHITE)  # Заливка фона белым цветом
        draw_text("Запоминание положения фигур", 48, BLACK, WINDOW_SIZE // 2, WINDOW_SIZE // 4)
        start_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()


# Основная игра
def play_game():
    # Создание доски
    board = Board()

    # Список всех возможных фигур
    pieces = [Pawn, Rook, Bishop, Knight, King, Queen]

    # Выбор случайной фигуры и её позиции
    PieceClass = random.choice(pieces)
    row, col = random.randint(0, 7), random.randint(0, 7)
    piece = PieceClass('white', row, col)

    # Показ фигуры на 5 секунд
    show_piece = True
    start_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not show_piece and event.type == pygame.MOUSEBUTTONDOWN:
                # Проверка клика игрока
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_col = mouse_x // SQUARE_SIZE
                clicked_row = mouse_y // SQUARE_SIZE

                if clicked_row == row and clicked_col == col:
                    return "win"  # Игрок выиграл
                else:
                    return "lose"  # Игрок проиграл

        # Отрисовка доски
        screen.fill(WHITE)
        board.draw(screen, SQUARE_SIZE)

        if show_piece and elapsed_time < 5:
            # Отрисовка фигуры
            piece.draw(screen, SQUARE_SIZE)
        else:
            show_piece = False

        # Отображение таймера
        if show_piece:
            draw_text(f"Осталось: {5 - int(elapsed_time)} сек", 36, BLACK, WINDOW_SIZE // 2, 20)

        pygame.display.flip()


# Экран победы
def win_screen():
    buttons = create_buttons()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    button.check_hover(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].is_clicked(pygame.mouse.get_pos()):
                    return "restart"
                elif buttons[1].is_clicked(pygame.mouse.get_pos()):
                    return "menu"

        screen.fill(WHITE)
        draw_text("Ты выиграл!", 48, BLACK, WINDOW_SIZE // 2, WINDOW_SIZE // 2 - 50)
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()


# Экран поражения
def lose_screen():
    buttons = create_buttons()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    button.check_hover(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].is_clicked(pygame.mouse.get_pos()):
                    return "restart"
                elif buttons[1].is_clicked(pygame.mouse.get_pos()):
                    return "menu"

        screen.fill(WHITE)
        draw_text("Ты проиграл!", 48, BLACK, WINDOW_SIZE // 2, WINDOW_SIZE // 2 - 50)
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()


# Главный цикл
def main():
    while True:
        action = handle_start_screen_events()

        if action == "start_game":
            while True:
                result = play_game()
                if result == "win":
                    next_action = win_screen()
                else:
                    next_action = lose_screen()

                if next_action == "menu":
                    break
                elif next_action == "restart":
                    continue

if __name__ == "__main__":
    main()