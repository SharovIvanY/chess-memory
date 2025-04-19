import pygame
from settings import WINDOW_SIZE, MAX_DIFFICULTY
from screens.start_screen import show_start_screen
from screens.difficulty_screen import show_difficulty_screen
from screens.game_screen import play_game
from screens.final_screen import show_final_screen

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Шахматная память")

    difficulty = 1  # Начальная сложность

    while True:
        # Стартовый экран
        action = show_start_screen(screen)
        if action == 'quit':
            break  # Завершаем программу

        # Выбор сложности
        difficulty = show_difficulty_screen(screen)

        while True:
            # Игра
            result = play_game(screen, difficulty)

            # Финальный экран
            action = show_final_screen(screen, result)

            # Обработка действия пользователя
            if action == 'retry':
                continue  # Повторить игру с той же сложностью
            elif action == 'next':
                difficulty += 1  # Увеличить сложность
                if difficulty > MAX_DIFFICULTY:  # Если достигнут максимальный уровень
                    difficulty = 1
                continue  # Начать новую игру с новой сложностью
            elif action == 'menu':
                break  # Вернуться в главное меню

    pygame.quit()

if __name__ == "__main__":
    main()