#include <iostream>
#include <vector>

using namespace std;

int performSequentialSearch(const vector<int>& collection, int searchValue) {
    // Проходим по всем элементам коллекции
    for (size_t index = 0; index < collection.size(); index++) {
        // Если нашли искомый элемент
        if (collection[index] == searchValue) {
            return index;  // Возвращаем индекс найденного элемента
        }
    }
    
    return -1;  // Возвращаем -1, если элемент не найден
}

// Основная функция для тестирования
int main() {
    vector<int> numbers = {3, 5, 2, 7, 9, 1, 4};
    int valueToFind = 7;  // Искомое значение

    // Вызываем функцию поиска
    int foundIndex = performSequentialSearch(numbers, valueToFind);

    // Выводим результат
    if (foundIndex != -1) {
        cout << "Элемент найден на позиции: " << foundIndex << endl;
    } else {
        cout << "Элемент не найден" << endl;
    }
    
    // Дополнительные тесты
    cout << "\nДополнительные проверки:" << endl;
    vector<int> testValues = {3, 10, 4, 0};
    for (int testValue : testValues) {
        int result = performSequentialSearch(numbers, testValue);
        if (result != -1) {
            cout << "Значение " << testValue << " найдено на позиции: " << result << endl;
        } else {
            cout << "Значение " << testValue << " не найдено" << endl;
        }
    }

    return 0;
}
