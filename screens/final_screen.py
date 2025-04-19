import pygame
from settings import WINDOW_SIZE, BLACK, WHITE, BUTTON_COLOR, BUTTON_HOVER_COLOR, TEXT_COLOR
from utils.button import Button
from utils.draw_utils import draw_text


def show_final_screen(screen, result):
    """
    Отображение финального экрана.
    :param screen: Объект pygame.Surface (экран).
    :param result: Результат игры ('win' или 'lose').
    :return: Действие, выбранное пользователем ('retry', 'next', 'menu').
    """
    pygame.display.set_caption("Финальный экран")

    # Создание кнопок
    retry_button = Button(
        x=WINDOW_SIZE // 2 - 100,
        y=WINDOW_SIZE // 2 - 50,
        width=200,
        height=50,
        text="Еще раз",
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    if result == 'win':
        next_button_text = "Следующая сложность"
    else:
        next_button_text = "В главное меню"

    next_button = Button(
        x=WINDOW_SIZE // 2 - 100,
        y=WINDOW_SIZE // 2 + 20,
        width=200,
        height=50,
        text=next_button_text,
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    while True:
        screen.fill(WHITE)

        # Отрисовка текста
        if result == 'win':
            draw_text(screen, "Вы выиграли!", 48, BLACK, WINDOW_SIZE // 2, 100)
        else:
            draw_text(screen, "Вы проиграли!", 48, BLACK, WINDOW_SIZE // 2, 100)

        # Обработка событий
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.is_clicked(mouse_pos):
                    return 'retry'
                elif next_button.is_clicked(mouse_pos):
                    return 'next' if result == 'win' else 'menu'

        # Обновление состояния кнопок
        retry_button.update_hover(mouse_pos)
        next_button.update_hover(mouse_pos)

        # Отрисовка кнопок
        retry_button.draw(screen)
        next_button.draw(screen)

        pygame.display.flip()