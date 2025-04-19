import pygame
from settings import WINDOW_SIZE, BLACK, WHITE, BUTTON_COLOR, BUTTON_HOVER_COLOR, TEXT_COLOR
from utils.button import Button
from utils.draw_utils import draw_text

def show_start_screen(screen):
    """
    Отображение стартового экрана.
    :param screen: Объект pygame.Surface (экран).
    :return: Действие, выбранное пользователем ('start' или 'quit').
    """
    pygame.display.set_caption("Шахматная память")

    # Создание кнопок
    start_button = Button(
        x=WINDOW_SIZE // 2 - 100,
        y=WINDOW_SIZE // 2 - 50,
        width=200,
        height=50,
        text="Начать игру",
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    quit_button = Button(
        x=WINDOW_SIZE // 2 - 100,
        y=WINDOW_SIZE // 2 + 20,
        width=200,
        height=50,
        text="Выйти",
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    while True:
        screen.fill(WHITE)

        # Отрисовка текста
        draw_text(screen, "Шахматная память", 48, BLACK, WINDOW_SIZE // 2, 100)

        # Обработка событий
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(mouse_pos):
                    return 'start'
                elif quit_button.is_clicked(mouse_pos):
                    return 'quit'

        # Обновление состояния кнопок
        start_button.update_hover(mouse_pos)
        quit_button.update_hover(mouse_pos)

        # Отрисовка кнопок
        start_button.draw(screen)
        quit_button.draw(screen)

        pygame.display.flip()