# Задание 1. Начало столетия
print("Задание 1. Начало столетия")
year = int(input("Введите год: "))
print("YES" if year % 100 == 0 else "NO")
print()

# Задание 2. Шахматная доска
print("Задание 2. Шахматная доска")
x1, y1, x2, y2 = (int(input()) for _ in range(4))
print("YES" if (x1 + y1) % 2 == (x2 + y2) % 2 else "NO")
print()

# Задание 3. Girls only
print("Задание 3. Girls only")
age = int(input("Введите возраст: "))
gender = input("Введите пол (m/f): ")
print("YES" if 10 <= age <= 15 and gender == 'f' else "NO")
print()

# Задание 4. Римские цифры
print("Задание 4. Римские цифры")
num = int(input("Введите число: "))
roman_numerals = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
                  6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
print(roman_numerals.get(num, "ошибка"))
print()

# Задание 5. YES or NO
print("Задание 5. YES or NO")
n = int(input("Введите число: "))
if n % 2 != 0 or (6 <= n <= 20):
    print("YES")
else:
    print("NO")
print()

# Задание 6. Ход слона
print("Задание 6. Ход слона")
x1, y1, x2, y2 = (int(input()) for _ in range(4))
print("YES" if abs(x1 - x2) == abs(y1 - y2) else "NO")
print()

# Задание 7. Ход коня
print("Задание 7. Ход коня")
x1, y1, x2, y2 = (int(input()) for _ in range(4))
if (abs(x1 - x2), abs(y1 - y2)) in [(1, 2), (2, 1)]:
    print("YES")
else:
    print("NO")
print()

# Задание 8. Ход ферзя
print("Задание 8. Ход ферзя")
x1, y1, x2, y2 = (int(input()) for _ in range(4))
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")
print()
