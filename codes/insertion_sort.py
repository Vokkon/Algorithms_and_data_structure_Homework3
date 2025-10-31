def sort_by_insertion(collection):
    # Обрабатываем элементы начиная со второго
    for current_index in range(1, len(collection)):
        current_element = collection[current_index]  # Элемент вставки
        previous_index = current_index - 1           # Индекс предыдущего элемента
        
        # Сдвигаем элементы, которые больше текущего элемента
        while previous_index >= 0 and collection[previous_index] > current_element:
            collection[previous_index + 1] = collection[previous_index]
            previous_index = previous_index - 1
        
        # Помещаем текущий элемент на нужную позицию
        collection[previous_index + 1] = current_element

def display_elements(items):
    # Отображаем элементы коллекции
    for element in items:
        print(element, end=" ")
    print()

if __name__ == "__main__":
    numbers = [15, 8, 22, 3, 11, 6]
    
    print("Массив до сортировки:")
    display_elements(numbers)
    
    sort_by_insertion(numbers)
    
    print("Массив после сортировки:")
    display_elements(numbers)
    
    # Дополнительный пример
    print("\nДополнительный пример:")
    another_list = [42, 17, 9, 31, 25, 5]
    print("До:", end=" ")
    display_elements(another_list)
    sort_by_insertion(another_list)
    print("После:", end=" ")
    display_elements(another_list)
