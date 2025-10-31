def perform_shell_sort(sequence):
    """
    Реализация алгоритма сортировки Шелла
    """
    total_elements = len(sequence)
    
    # Начинаем с большого интервала и постепенно уменьшаем его
    interval = total_elements // 2
    while interval > 0:
        # Выполняем сортировку вставками для элементов на расстоянии interval
        for current_index in range(interval, total_elements):
            # Сохраняем текущий элемент для вставки
            current_value = sequence[current_index]
            position = current_index
            
            # Сдвигаем элементы, которые больше current_value, вправо
            while position >= interval and sequence[position - interval] > current_value:
                sequence[position] = sequence[position - interval]
                position -= interval
            
            sequence[position] = current_value
        
        # Уменьшаем интервал
        interval //= 2

def display_sequence(elements):
    """
    Функция для отображения элементов последовательности
    """
    for element in elements:
        print(element, end=" ")
    print()

# Демонстрационная программа
if __name__ == "__main__":
    # Пример использования
    numbers = [35, 12, 29, 15, 42, 8, 23]
    
    print("Исходная последовательность: ", end="")
    display_sequence(numbers)
    
    perform_shell_sort(numbers)
    
    print("Отсортированная последовательность: ", end="")
    display_sequence(numbers)
    
    # Дополнительный пример
    print("\nДополнительный пример:")
    another_list = [64, 34, 25, 12, 22, 11, 90, 5]
    print("До сортировки: ", end="")
    display_sequence(another_list)
    perform_shell_sort(another_list)
    print("После сортировки: ", end="")
    display_sequence(another_list)
