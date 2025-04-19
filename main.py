import pygame
from utils.save_utils import load_unlocked_levels, save_unlocked_levels
from settings import WINDOW_SIZE, MAX_DIFFICULTY
from screens.start_screen import show_start_screen
from screens.difficulty_screen import show_difficulty_screen
from screens.game_screen import play_game
from screens.final_screen import show_final_screen
from utils.piece_images import load_piece_images


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Шахматная память")

    # Загрузка изображений фигур
    piece_images = load_piece_images()
    if piece_images is None:
        print("Ошибка загрузки изображений фигур. Завершение программы.")
        pygame.quit()
        exit()

    # Загрузка доступных уровней
    unlocked_levels = load_unlocked_levels()

    while True:
        # Стартовый экран
        action = show_start_screen(screen)
        if action == 'quit':
            break  # Завершаем программу
        elif action == 'reset':
            unlocked_levels = [1]  # Сбрасываем прогресс до начального состояния
            continue  # Возвращаемся на стартовый экран

        # Выбор уровня
        difficulty = show_difficulty_screen(screen)

        # Проверяем, если пользователь вернулся на главный экран через Esc
        if difficulty == 'menu':
            continue

        # Преобразуем сложность в целое число
        difficulty = int(difficulty)

        while True:
            # Игра
            result = play_game(screen, difficulty, piece_images)

            # Если пользователь вышел через Esc
            if result == 'menu':
                break

            # Финальный экран
            action = show_final_screen(screen, result)

            # Обработка действия пользователя
            if action == 'retry':
                continue  # Повторить игру с той же сложностью
            elif action == 'next':
                # Открываем следующий уровень
                next_level = difficulty + 1
                if next_level not in unlocked_levels:
                    unlocked_levels.append(next_level)
                    save_unlocked_levels(unlocked_levels)  # Сохраняем прогресс
                difficulty = next_level
                continue  # Начать новую игру с новой сложностью
            elif action == 'menu':
                break  # Вернуться в главное меню

    pygame.quit()


if __name__ == "__main__":
    main()