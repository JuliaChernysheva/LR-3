# Задание 1. Python is awesome
print("Задание 1: Вывод 10 раз 'Python is awesome!'")
for _ in range(10):
    print("Python is awesome!")

# Задание 2. Повторяй за мной 1
print("\nЗадание 2: Введите предложение и количество повторений")
sentence = input("Введите предложение: ")
repeat_count = int(input("Введите количество повторений: "))
for _ in range(repeat_count):
    print(sentence)

# Задание 3. Последовательность символов
print("\nЗадание 3: Вывод последовательности символов")
for _ in range(6):
    print("AAA")
for _ in range(5):
    print("BBBB")
print("E")
for _ in range(9):
    print("TTTTT")
print("G")

# Задание 4. Звездный прямоугольник
print("\nЗадание 4: Введите высоту звездного прямоугольника")
n = int(input("Введите число (от 1 до 20): "))
for _ in range(n):
    print("*" * 19)

# Задание 5. Повторяй за мной 2
print("\nЗадание 5: Введите строку для вывода с нумерацией")
text = input("Введите строку: ")
for i in range(10):
    print(f"{i} {text}")

# Задание 6. Квадрат числа
print("\nЗадание 6: Введите число для вычисления квадратов")
n = int(input("Введите натуральное число: "))
for i in range(n + 1):
    print(f"Квадрат числа {i} равен {i ** 2}")

# Задание 7. Звездный треугольник
print("\nЗадание 7: Введите катет звездного треугольника")
n = int(input("Введите число (n ≥ 2): "))
for i in range(n, 0, -1):
    print("*" * i)

# Задание 8. Популяция
print("\nЗадание 8: Прогноз популяции")
m = int(input("Введите стартовое количество организмов: "))
p = int(input("Введите среднесуточное увеличение в %: "))
n = int(input("Введите количество дней для размножения: "))

population = m
for day in range(1, n + 1):
    print(f"{day} {population:.6g}")  # Округление до 6 значащих цифр
    population += population * (p / 100)
