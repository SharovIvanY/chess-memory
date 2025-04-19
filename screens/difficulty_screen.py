import pygame
import json
from sys import exit
from utils.button import Button
from utils.draw_utils import draw_text
from settings import WINDOW_SIZE, BLACK, WHITE, BUTTON_COLOR, BUTTON_HOVER_COLOR, TEXT_COLOR


def load_unlocked_levels():
    """Загрузка доступных уровней из save.json."""
    try:
        with open("save.json", "r") as file:
            data = json.load(file)
            return data.get("unlocked_levels", [1])
    except FileNotFoundError:
        # Если файл не найден, создаем новый с начальными данными
        initial_data = {"unlocked_levels": [1]}
        with open("save.json", "w") as file:
            json.dump(initial_data, file)
        return [1]

def show_difficulty_screen(screen):
    pygame.display.set_caption("Выбор уровня")

    # Загрузка доступных уровней
    unlocked_levels = load_unlocked_levels()

    # Создание кнопок для всех уровней
    buttons = []
    for level in range(1, 6):  # Уровни от 1 до 5
        button_color = BUTTON_COLOR if level in unlocked_levels else (128, 128, 128)  # Серый цвет для заблокированных уровней
        hover_color = BUTTON_HOVER_COLOR if level in unlocked_levels else (128, 128, 128)
        button = Button(
            x=WINDOW_SIZE // 2 - 100,
            y=100 + (level - 1) * 70,  # Вертикальное расположение кнопок
            width=200,
            height=50,
            text=f"Уровень {level}",
            color=button_color,
            hover_color=hover_color,
            text_color=TEXT_COLOR,
            font_size=36
        )
        buttons.append(button)

    while True:
        screen.fill(WHITE)

        # Отрисовка текста
        draw_text(screen, "Выберите уровень", 48, BLACK, WINDOW_SIZE // 2, 50)

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
                for i, button in enumerate(buttons):
                    level = i + 1
                    if button.is_clicked(mouse_pos) and level in unlocked_levels:
                        return level  # Возвращаем выбранный уровень

        # Обновление состояния кнопок
        for button in buttons:
            button.update_hover(mouse_pos)

        # Отрисовка кнопок
        for button in buttons:
            button.draw(screen)

        pygame.display.flip()