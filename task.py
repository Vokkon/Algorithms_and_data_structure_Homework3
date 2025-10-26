def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

test_array = [64, 25, 12, 22, 11]
print("Исходный массив:", test_array)
selection_sort(test_array)
print("Отсортированный массив:", test_array)
