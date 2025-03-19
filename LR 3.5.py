import math

# Задание 1: Евклидово расстояние
print("Задание 1: Евклидово расстояние")
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(distance)

# Задание 2: Площадь и длина
print("\nЗадание 2: Площадь и длина")
R = float(input("Введите радиус: "))
area = math.pi * R ** 2
circumference = 2 * math.pi * R
print(area)
print(circumference)

# Задание 3: Средние значения
print("\nЗадание 3: Средние значения")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
arithmetic_mean = (a + b) / 2
geometric_mean = math.sqrt(a * b)
harmonic_mean = 2 * a * b / (a + b)
quadratic_mean = math.sqrt((a ** 2 + b ** 2) / 2)
print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(quadratic_mean)

# Задание 4: Тригонометрическое выражение
print("\nЗадание 4: Тригонометрическое выражение")
x = float(input("Введите угол в градусах: "))
x_rad = math.radians(x)
result = math.sin(x_rad) + math.cos(x_rad) + math.tan(x_rad) ** 2
print(result)

# Задание 5: Пол и потолок
print("\nЗадание 5: Пол и потолок")
x = float(input("Введите число: "))
result = math.ceil(x) + math.floor(x)
print(result)

# Задание 6: Квадратное уравнение
print("\nЗадание 6: Квадратное уравнение")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    root1 = (-b - math.sqrt(discriminant)) / (2 * a)
    root2 = (-b + math.sqrt(discriminant)) / (2 * a)
    print(root1)
    print(root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print(root)
else:
    print("Нет корней")

# Задание 7: Правильный многоугольник
print("\nЗадание 7: Правильный многоугольник")
n = int(input("Введите количество сторон: "))
a = float(input("Введите длину стороны: "))
polygon_area = (n * a ** 2) / (4 * math.tan(math.pi / n))
print(polygon_area)
