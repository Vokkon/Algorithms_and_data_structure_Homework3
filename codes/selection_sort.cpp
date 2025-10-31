#include <iostream>
#include <vector>

using namespace std;

// Функция для сортировки выбором
void performSelectionSort(vector<int>& data) {
    int elementCount = data.size();
    
    // Проходим по всем элементам вектора
    for (int currentPosition = 0; currentPosition < elementCount; currentPosition++) {
        // Предполагаем, что текущий элемент - минимальный
        int minValueIndex = currentPosition;

        // Ищем минимальный элемент в оставшейся части вектора
        for (int searchIndex = currentPosition + 1; searchIndex < elementCount; searchIndex++) {
            // Сравниваем текущий элемент с предполагаемым минимумом
            if (data[searchIndex] < data[minValueIndex]) {
                minValueIndex = searchIndex;  // Обновляем индекс минимального элемента
            }
        }

        // Меняем найденный минимальный элемент с текущим элементом
        int temporaryValue = data[currentPosition];
        data[currentPosition] = data[minValueIndex];
        data[minValueIndex] = temporaryValue;
    }
}

// Функция для вывода вектора
void displayVector(const vector<int>& elements) {
    for (size_t i = 0; i < elements.size(); i++) {
        cout << elements[i];
        if (i < elements.size() - 1) {
            cout << " ";
        }
    }
    cout << endl;
}

// Основная функция
int main() {
    // Создаем тестовый вектор
    vector<int> sampleData = {64, 25, 12, 22, 11};
    
    cout << "Исходный вектор: ";
    displayVector(sampleData);
    
    // Сортируем вектор
    performSelectionSort(sampleData);
    
    cout << "Отсортированный вектор: ";
    displayVector(sampleData);
    
    return 0;
}
