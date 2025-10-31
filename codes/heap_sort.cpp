#include <iostream>
#include <vector>

using namespace std;

void heapifySubtree(vector<int>& data, int heapSize, int rootIndex) {
    int largestIndex = rootIndex; // Инициализируем наибольший элемент как корень
    int leftChildIndex = 2 * rootIndex + 1;
    int rightChildIndex = 2 * rootIndex + 2;
    // Проверяем существует ли левый дочерний элемент больший, чем корень
    if (leftChildIndex < heapSize && data[rootIndex] < data[leftChildIndex]) {
        largestIndex = leftChildIndex;
    }
    
    // Проверяем существует ли правый дочерний элемент больший, чем корень
    if (rightChildIndex < heapSize && data[largestIndex] < data[rightChildIndex]) {
        largestIndex = rightChildIndex;
    }
    
    // Меняем корень, если нужно
    if (largestIndex != rootIndex) {
        int swapValue = data[rootIndex];
        data[rootIndex] = data[largestIndex];
        data[largestIndex] = swapValue;
        
        // Рекурсивно применяем heapify к поддереву
        heapifySubtree(data, heapSize, largestIndex);
    }
}

// Основная функция для пирамидальной сортировки
void performHeapSort(vector<int>& data) {
    int dataSize = data.size();
    
    // Построение max-heap
    for (int currentIndex = dataSize / 2 - 1; currentIndex >= 0; currentIndex--) {
        heapifySubtree(data, dataSize, currentIndex);
    }
    
    // Один за другим извлекаем элементы
    for (int currentIndex = dataSize - 1; currentIndex > 0; currentIndex--) {
        // Меняем корень с последним элементом
        int swapValue = data[0];
        data[0] = data[currentIndex];
        data[currentIndex] = swapValue;
        
        // Вызываем heapify на уменьшенной куче
        heapifySubtree(data, currentIndex, 0);
    }
}

// Вспомогательная функция для вывода массива
void displayArray(const vector<int>& data) {
    for (size_t i = 0; i < data.size(); i++) {
        cout << data[i];
        if (i < data.size() - 1) {
            cout << " ";
        }
    }
    cout << endl;
}

// Пример использования
int main() {
    vector<int> numbers = {12, 11, 13, 5, 6, 7};
    
    cout << "Исходный вектор: ";
    displayArray(numbers);
    
    performHeapSort(numbers);
    
    cout << "Отсортированный вектор: ";
    displayArray(numbers);
    
    return 0;
}
