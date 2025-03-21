# Задача 1. Геометрическая прогрессия
print("Задача 1. Геометрическая прогрессия")
b1 = int(input("Введите первый член прогрессии: "))
q = int(input("Введите знаменатель прогрессии: "))
n = int(input("Введите номер члена прогрессии: "))
print(f"Результат: {b1 * q ** (n - 1)}\n")

# Задача 2. Расстояние в метрах
print("Задача 2. Расстояние в метрах")
cm = int(input("Введите количество сантиметров: "))
print(f"Полное число метров: {cm // 100}\n")

# Задача 3. Мандарины
print("Задача 3. Мандарины")
N = int(input("Введите количество школьников: "))
K = int(input("Введите количество мандаринов: "))
print(f"Каждому школьнику достанется: {K // N}")
print(f"Останется в корзине: {K % N}\n")

# Задача 4. Сама неотвратимость
print("Задача 4. Сама неотвратимость")
n = int(input("Введите население Вселенной: "))
print(f"Количество выживших: {(n + 1) // 2}\n")

# Задача 5. Номер купе
print("Задача 5. Номер купе")
seat = int(input("Введите номер места в вагоне: "))
print(f"Номер купе: {(seat - 1) // 4 + 1}\n")

# Задача 6. Пересчет временного интервала
print("Задача 6. Пересчет временного интервала")
minutes = int(input("Введите количество минут: "))
hours = minutes // 60
mins = minutes % 60
print(f"{minutes} мин - это {hours} час {mins} мин\n")

# Задача 7. Трехзначное число
print("Задача 7. Трехзначное число")
num = int(input("Введите трехзначное число: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
print(f"Сумма цифр = {a + b + c}")
print(f"Произведение цифр = {a * b * c}\n")

# Задача 8. Перестановка цифр
print("Задача 8. Перестановка цифр")
num = input("Введите трехзначное число с разными цифрами: ").strip()
a, b, c = num[0], num[1], num[2]
print(f"Все перестановки цифр: {a+b+c}, {a+c+b}, {b+a+c}, {b+c+a}, {c+a+b}, {c+b+a}\n")

# Задача 9. Четырёхзначное число
print("Задача 9. Четырёхзначное число")
num = int(input("Введите четырехзначное число: "))
print(f"Цифра в позиции тысяч равна {num // 1000}")
print(f"Цифра в позиции сотен равна {(num // 100) % 10}")
print(f"Цифра в позиции десятков равна {(num // 10) % 10}")
print(f"Цифра в позиции единиц равна {num % 10}\n")
