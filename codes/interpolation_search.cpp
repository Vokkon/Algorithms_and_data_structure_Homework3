#include <iostream>
#include <vector>

using namespace std;

// Функция линейного поиска
int linearSearch(const vector<int>& arr, int target) {
    // Проходим по всем элементам вектора
    for(int i = 0; i < arr.size(); i++) {
        // Если нашли искомый элемент
        if(arr[i] == target) {
            return i; // Возвращаем индекс найденного элемента
        }
    }
    return -1; // Возвращаем -1, если элемент не найден
}

int main() {
    // Создаем вектор
    vector<int> array = {3, 5, 2, 7, 9, 1, 4};
    
    int target = 7; // Искомое значение
    
    // Вызываем функцию поиска
    int result = linearSearch(array, target);
    
    // Выводим результат
    if(result != -1) {
        cout << "Элемент найден на позиции: " << result << endl;
    } else {
        cout << "Элемент не найден" << endl;
    }
    
    return 0;
}
