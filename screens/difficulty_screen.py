import pygame
from settings import WINDOW_SIZE, BLACK, WHITE, BUTTON_COLOR, BUTTON_HOVER_COLOR, TEXT_COLOR
from utils.button import Button
from utils.draw_utils import draw_text

def show_difficulty_screen(screen):
    pygame.display.set_caption("Выбор сложности")

    # Создание кнопки
    level_1_button = Button(
        x=WINDOW_SIZE // 2 - 100,
        y=WINDOW_SIZE // 2 - 25,
        width=200,
        height=50,
        text="Уровень 1",
        color=BUTTON_COLOR,
        hover_color=BUTTON_HOVER_COLOR,
        text_color=TEXT_COLOR,
        font_size=36
    )

    while True:
        screen.fill(WHITE)

        # Отрисовка текста
        draw_text(screen, "Выберите уровень сложности", 48, BLACK, WINDOW_SIZE // 2, 100)

        # Обработка событий
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_1_button.is_clicked(mouse_pos):
                    return 1  # Возвращаем уровень сложности

        # Обновление состояния кнопки
        level_1_button.update_hover(mouse_pos)

        # Отрисовка кнопки
        level_1_button.draw(screen)

        pygame.display.flip()