def fibonacci_search(sequence, target_value):
    """
    Реализация алгоритма поиска с использованием чисел Фибоначчи
    """
    length = len(sequence)
    
    # Инициализация чисел Фибоначчи
    fib_prev = 0
    fib_curr = 1
    fib_next = fib_prev + fib_curr
    
    # Находим наименьшее число Фибоначчи, большее или равное длине массива
    while fib_next < length:
        fib_prev = fib_curr
        fib_curr = fib_next
        fib_next = fib_prev + fib_curr
    
    # Начальная позиция для поиска
    search_start = -1
    
    # Основной цикл поиска
    while fib_next > 1:
        # Вычисляем позицию для проверки
        check_index = min(search_start + fib_prev, length - 1)
        
        # Сравниваем элемент с искомым значением
        if sequence[check_index] < target_value:
            # Перемещаемся к правой части
            fib_next = fib_curr
            fib_curr = fib_prev
            fib_prev = fib_next - fib_curr
            search_start = check_index
        
        elif sequence[check_index] > target_value:
            # Перемещаемся к левой части
            fib_next = fib_prev
            fib_curr = fib_curr - fib_prev
            fib_prev = fib_next - fib_curr
        
        else:
            # Возвращение элемента
            return check_index
    
    # Проверка последнего элемента
    if fib_curr == 1 and search_start + 1 < length and sequence[search_start + 1] == target_value:
        return search_start + 1
    
    return -1  # Если элемент не найден

def run_demo():
    """
    Демонстрация работы алгоритма поиска Фибоначчи
    """
    data = [2, 5, 8, 12, 16, 23, 38, 45, 67, 73, 91]
    search_target = 45
    
    print("Исходная последовательность:", data)
    print("Цель поиска:", search_target)
    
    position = fibonacci_search(data, search_target)
    
    if position != -1:
        print(f"Найдено на позиции: {position}")
    else:
        print("Цель не найдена в последовательности")
    
    # Дополнительные проверки
    print("\nПроверка других значений:")
    test_values = [2, 73, 91, 25, 100]
    for value in test_values:
        idx = fibonacci_search(data, value)
        status = f"на позиции {idx}" if idx != -1 else "не найдено"
        print(f"Значение {value}: {status}")

if __name__ == "__main__":
    run_demo()
