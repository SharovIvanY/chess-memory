import pygame
from board import Board
from settings import WINDOW_SIZE, SQUARE_SIZE

# Инициализация PyGame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Шахматы")

# Создание объекта доски
board = Board()

# Основной цикл игры
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Отрисовка доски
        screen.fill((0, 0, 0))  # Очистка экрана
        board.draw(screen, SQUARE_SIZE)

        # Обновление экрана
        pygame.display.flip()

    # Завершение работы PyGame
    pygame.quit()

if __name__ == "__main__":
    main()