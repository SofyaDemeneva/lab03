# Функция для сортировки пузырьком
def bubble_sort(arr, ascending=True):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ввод чисел
numbers = [float(input(f"Введите число {i + 1}: ")) for i in range(int(input("Введите количество чисел: ")))]

# Ввод направления сортировки
direction = input("Введите направление сортировки (+ для возрастания, - для убывания): ").strip().lower()

# Сортировка и вывод
bubble_sort(numbers, ascending=(direction == "+"))
print("Отсортированные числа:", *numbers)
