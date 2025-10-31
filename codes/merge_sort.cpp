#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Функция для слияния двух отсортированных векторов
vector<int> mergeVectors(const vector<int>& left, const vector<int>& right) {
    vector<int> result;
    size_t i = 0, j = 0;
    
    // Пока есть элементы в обоих векторах
    while (i < left.size() && j < right.size()) {
        if (left[i] < right[j]) {
            result.push_back(left[i]);
            i++;
        } else {
            result.push_back(right[j]);
            j++;
        }
    }
    
    // Добавляем оставшиеся элементы из левого вектора
    while (i < left.size()) {
        result.push_back(left[i]);
        i++;
    }
    
    // Добавляем оставшиеся элементы из правого вектора
    while (j < right.size()) {
        result.push_back(right[j]);
        j++;
    }
    
    return result;
}

// Функция сортировки слиянием
vector<int> mergeSort(const vector<int>& arr) {
    // Базовый случай: вектор длиной 0 или 1 уже отсортирован
    if (arr.size() <= 1) {
        return arr;
    }
    
    // Находим середину вектора
    size_t mid = arr.size() / 2;
    
    // Делим вектор на две части
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());
    
    // Рекурсивно сортируем каждую часть
    left = mergeSort(left);
    right = mergeSort(right);
    
    // Сливаем отсортированные части
    return mergeVectors(left, right);
}

// Функция для вывода вектора
void printVector(const vector<int>& vec) {
    for (size_t i = 0; i < vec.size(); i++) {
        cout << vec[i];
        if (i < vec.size() - 1) {
            cout << " ";
        }
    }
    cout << endl;
}

// Основная функция для тестирования
int main() {
    vector<int> array = {38, 27, 43, 3, 9, 82, 10};
    
    cout << "Исходный вектор: ";
    printVector(array);
    
    vector<int> sortedArray = mergeSort(array);
    
    cout << "Отсортированный вектор: ";
    printVector(sortedArray);
    
    return 0;
}
