# Задание 1. Футбольная команда
print("Введите название футбольной команды:")
team_name = input()
print(f'Футбольная команда {team_name} имеет длину {len(team_name)} символов')

# Задание 2. Три города
print("Введите названия трех городов:")
city1 = input()
city2 = input()
city3 = input()
cities = [city1, city2, city3]
print("Самый короткий город:", min(cities, key=len))
print("Самый длинный город:", max(cities, key=len))

# Задание 3. Корректный e-mail
print("Введите e-mail для проверки:")
email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')

# Задание 4. В столбик 1
print("Введите строку для вывода через один символ:")
string = input()
for i in range(0, len(string), 2):
    print(string[i])

# Задание 5. В столбик 2
print("Введите строку для вывода в обратном порядке:")
string = input()
for char in reversed(string):
    print(char)

# Задание 6. Сколько раз?
print("Введите строку для подсчета символов + и *:")
string = input()
print(f'Символ + встречается {string.count("+")} раз')
print(f'Символ * встречается {string.count("*")} раз')

# Задание 7. Гласные и согласные
print("Введите строку на русском языке для подсчета гласных и согласных:")
vowels = "ауоыиэяюёе"
consonants = "бвгджзйклмнпрстфхцчшщ"
text = input().lower()
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char in consonants)
print(f'Количество гласных букв равно {vowel_count}')
print(f'Количество согласных букв равно {consonant_count}')
