def bubble_sort(collection):
    """
    Реализация алгоритма сортировки пузырьком
    
    Args:
        collection: список элементов для упорядочивания
    """
    total_elements = len(collection)
    
    # Количество проходов
    for pass_num in range(total_elements):
        swapped = False
        
        # Сравнение соседних элементов
        for position in range(total_elements - pass_num - 1):
            # Сравниваем текущий и следующий элемент
            if collection[position] > collection[position + 1]:
                # Обмен значений при необходимости
                collection[position], collection[position + 1] = collection[position + 1], collection[position]
                swapped = True
        
        # Если на этом проходе не было обменов, массив уже отсортирован
        if not swapped:
            break

def display_list(items):
    """
    Функция для отображения элементов списка
    
    Args:
        items: список для отображения
    """
    print("[", end="")
    for i, item in enumerate(items):
        if i > 0:
            print(", ", end="")
        print(item, end="")
    print("]")

# Демонстрация работы алгоритма
if __name__ == "__main__":
    # Исходные данные для сортировки
    numbers = [29, 10, 14, 37, 13, 25, 50]
    
    print("Массив до сортировки:")
    display_list(numbers)
    
    # Выполняем сортировку
    bubble_sort(numbers)
    
    print("Массив после сортировки:")
    display_list(numbers)
    
    # Дополнительный тест с другим массивом
    another_list = [5, 2, 8, 1, 9]
    print("\nДополнительный тест:")
    print("До:", another_list)
    bubble_sort(another_list)
    print("После:", another_list)
