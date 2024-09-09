# Функция для сортировки пузырьком
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ввод чисел
numbers = [float(input(f"Введите число {i + 1}: ")) for i in range(int(input("Введите количество чисел: ")))]

# Сортировка и вывод
bubble_sort(numbers)
print("Отсортированные числа:", *numbers)
