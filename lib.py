def count_common_elements(*lists):
    """
    Возвращает количество элементов, которые есть во всех переданных списках.
    """
    if not lists:  # если не передали ни одного списка
        return 0

    # Преобразуем первый список в множество
    common = set(lists[0])

    # Находим пересечение со всеми остальными списками
    for lst in lists[1:]:
        common = common.intersection(set(lst))

    # Возвращаем количество общих элементов
    return len(common)