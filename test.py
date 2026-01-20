# test.py - тестирование функции count_common_elements из lib.py

def test_count_common_elements():

    print("Тестирование функции count_common_elements")
    print("=" * 40)

    # Импортируем функцию из lib.py
    from lib import count_common_elements

    # Тест 1: Обычный случай
    result = count_common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5])
    print(f"Тест 1: {[1, 2, 3]}, {[2, 3, 4]}, {[3, 4, 5]}")
    print(f"  Результат: {result} (ожидается: 1)")
    print(f"  Статус: {'ПРОЙДЕН' if result == 1 else 'НЕ ПРОЙДЕН'}")
    print()

    # Тест 2: Все элементы одинаковые
    result = count_common_elements([1, 2], [1, 2], [1, 2])
    print(f"Тест 2: {[1, 2]}, {[1, 2]}, {[1, 2]}")
    print(f"  Результат: {result} (ожидается: 2)")
    print(f"  Статус: {'ПРОЙДЕН' if result == 2 else 'НЕ ПРОЙДЕН'}")
    print()

    # Тест 3: Нет общих элементов
    result = count_common_elements([1, 2, 3], [4, 5, 6])
    print(f"Тест 3: {[1, 2, 3]}, {[4, 5, 6]}")
    print(f"  Результат: {result} (ожидается: 0)")
    print(f"  Статус: {'ПРОЙДЕН' if result == 0 else 'НЕ ПРОЙДЕН'}")
    print()

    # Тест 4: Один список
    result = count_common_elements([1, 2, 3, 4])
    print(f"Тест 4: {[1, 2, 3, 4]}")
    print(f"  Результат: {result} (ожидается: 4)")
    print(f"  Статус: {'ПРОЙДЕН' if result == 4 else 'НЕ ПРОЙДЕН'}")
    print()

    # Тест 5: Пустые списки
    result = count_common_elements([], [], [])
    print(f"Тест 5: [], [], []")
    print(f"  Результат: {result} (ожидается: 0)")
    print(f"  Статус: {'ПРОЙДЕН' if result == 0 else 'НЕ ПРОЙДЕН'}")
    print()

    # Тест 6: Строки
    result = count_common_elements(["a", "b", "c"], ["b", "c", "d"], ["c", "d", "e"])
    print(f'Тест 6: {["a", "b", "c"]}, {["b", "c", "d"]}, {["c", "d", "e"]}')
    print(f"  Результат: {result} (ожидается: 1)")
    print(f"  Статус: {'ПРОЙДЕН' if result == 1 else 'НЕ ПРОЙДЕН'}")
    print()

    print("=" * 40)
    print("Тестирование завершено")


if __name__ == "__main__":
    test_count_common_elements()