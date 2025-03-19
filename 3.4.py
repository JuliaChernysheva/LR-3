# Задание 1: Две старушки
print("Задание 1: Две старушки")
S = float(input("Введите расстояние между старушками (км): "))
V1 = float(input("Введите скорость первой старушки (км/ч): "))
V2 = float(input("Введите скорость второй старушки (км/ч): "))
time = S / (V1 + V2)  # Время до встречи
print(time)

# Задание 2: Обратное число
print("\nЗадание 2: Обратное число")
num = float(input("Введите число: "))
if num == 0:
    print("Обратного числа не существует")
else:
    print(1 / num)

# Задание 3: Dog age
print("\nЗадание 3: Dog age")
dog_years = int(input("Введите количество собачьих лет: "))
if dog_years == 1:
    human_years = 10.5
elif dog_years == 2:
    human_years = 21
else:
    human_years = 21 + (dog_years - 2) * 4  # После двух лет каждый год = 4 человеческих года
print(human_years)

# Задание 4: Первая цифра после точки
print("\nЗадание 4: Первая цифра после точки")
num = float(input("Введите положительное число: "))
first_digit = int(num * 10) % 10  # Получаем первую цифру после точки
print(first_digit)

# Задание 5: Дробная часть
print("\nЗадание 5: Дробная часть")
num = float(input("Введите положительное число: "))
frac_part = num - int(num)  # Вычисляем дробную часть
print(frac_part)

# Задание 6: Сортировка трёх
print("\nЗадание 6: Сортировка трёх")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
sorted_nums = sorted([a, b, c], reverse=True)  # Сортировка по убыванию
for num in sorted_nums:
    print(num)

# Задание 7: Манхэттенское расстояние
print("\nЗадание 7: Манхэттенское расстояние")
p1 = int(input("Введите координату p1: "))
p2 = int(input("Введите координату p2: "))
q1 = int(input("Введите координату q1: "))
q2 = int(input("Введите координату q2: "))
manhattan_distance = abs(p1 - q1) + abs(p2 - q2)  # Вычисление Манхэттенского расстояния
print(manhattan_distance)