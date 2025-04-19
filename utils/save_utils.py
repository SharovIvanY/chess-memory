import json
import os
from utils.draw_utils import resource_path  # Импортируем функцию

def load_unlocked_levels():
    """
    Загрузка доступных уровней из save.json.
    :return: Список доступных уровней.
    """
    try:
        # Путь к файлу через resource_path
        save_path = resource_path("save.json")
        with open(save_path, "r") as file:
            data = json.load(file)
            return data.get("unlocked_levels", [1])
    except FileNotFoundError:
        # Если файл не найден, создаем новый с начальными данными
        initial_data = {"unlocked_levels": [1]}
        with open("save.json", "w") as file:
            json.dump(initial_data, file)
        return [1]


def save_unlocked_levels(unlocked_levels):
    """
    Сохранение доступных уровней в save.json.
    :param unlocked_levels: Список доступных уровней.
    """
    save_path = resource_path("save.json")
    with open(save_path, "w") as file:
        json.dump({"unlocked_levels": unlocked_levels}, file)