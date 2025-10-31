def sort_quick(collection, start_pos, end_pos):
    """
    Функция для сортировки коллекции методом быстрой сортировки
    """
    if start_pos < end_pos:
        # split_index - индекс разбиения, collection[split_index] на своем месте
        split_index = partition_collection(collection, start_pos, end_pos)
        
        # Рекурсивно сортируем элементы до и после разбиения
        sort_quick(collection, start_pos, split_index - 1)
        sort_quick(collection, split_index + 1, end_pos)

def partition_collection(collection, start_pos, end_pos):
    """
    Функция для разделения коллекции относительно опорного элемента
    """
    # Выбираем последний элемент в качестве опорного
    pivot_value = collection[end_pos]
    smaller_index = start_pos - 1  # Индекс меньшего элемента
    
    for current_index in range(start_pos, end_pos):
        # Если текущий элемент меньше или равен опорному
        if collection[current_index] <= pivot_value:
            smaller_index += 1
            # Меняем местами collection[smaller_index] и collection[current_index]
            collection[smaller_index], collection[current_index] = collection[current_index], collection[smaller_index]
    
    # Меняем местами collection[smaller_index+1] и collection[end_pos]
    collection[smaller_index + 1], collection[end_pos] = collection[end_pos], collection[smaller_index + 1]
    
    return smaller_index + 1

def display_collection(collection):
    """
    Вспомогательная функция для вывода коллекции
    """
    for element in collection:
        print(element, end=" ")
    print()

# Основная функция для демонстрации
if __name__ == "__main__":
    numbers = [10, 7, 8, 9, 1, 5]
    
    print("Исходная коллекция:")
    display_collection(numbers)
    
    sort_quick(numbers, 0, len(numbers) - 1)
    
    print("Отсортированная коллекция:")
    display_collection(numbers)
