def find_element_sorted(sequence, value):
    """
    Осуществляет поиск элемента в отсортированной последовательности
    
    Args:
        sequence: упорядоченный список элементов
        value: значение для поиска
    
    Returns:
        позиция элемента или -1 при отсутствии
    """
    low_index = 0
    high_index = len(sequence) - 1
    
    while low_index <= high_index:
        # Способ вычисления середины
        center_index = (low_index + high_index) >> 1  # Побитовый сдвиг
        
        current_element = sequence[center_index]
        
        # Логика сравнений
        if current_element < value:
            low_index = center_index + 1
        elif current_element > value:
            high_index = center_index - 1
        else:
            return center_index
    
    return -1

# Дополнительная функция для проверки результата
def check_search_result(position, value):
    if position >= 0:
        print(f"Значение {value} обнаружено в позиции {position}")
    else:
        print(f"Значение {value} отсутствует в массиве")

# Основной блок выполнения
if __name__ == "__main__":
    test_data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    search_target = 10
    
    found_position = find_element_sorted(test_data, search_target)
    check_search_result(found_position, search_target)
    
    # Дополнительный тест
    another_target = 15
    result = find_element_sorted(test_data, another_target)
    check_search_result(result, another_target)
