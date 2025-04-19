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
    pygame.display.set_caption("Результат игры")

    # Создание кнопок
    retry_button = Button(
        x=WINDOW_SIZE // 2 - 100,
        y=WINDOW_SIZE // 2 - 50,
        width=200,
        height=50,
        text="Повторить",
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    menu_button = Button(
        x=WINDOW_SIZE // 2 - 100,
        y=WINDOW_SIZE // 2 + 90,
        width=200,
        height=50,
        text="Главное меню",
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    # Кнопка "Следующий уровень" создается только при победе
    next_button = None
    if result == 'win':
        next_button = Button(
            x=WINDOW_SIZE // 2 - 100,
            y=WINDOW_SIZE // 2 + 20,
            width=200,
            height=50,
            text="Дальше",
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'menu'  # Возвращаемся в главное меню

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.is_clicked(mouse_pos):
                    return 'retry'
                elif next_button and next_button.is_clicked(mouse_pos):
                    return 'next'
                elif menu_button.is_clicked(mouse_pos):
                    return 'menu'

        # Обновление состояния кнопок
        retry_button.update_hover(mouse_pos)
        if next_button:
            next_button.update_hover(mouse_pos)
        menu_button.update_hover(mouse_pos)

        # Отрисовка кнопок
        retry_button.draw(screen)
        if next_button:
            next_button.draw(screen)
        menu_button.draw(screen)

        pygame.display.flip()