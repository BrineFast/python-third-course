"""
Напишите программу, которая генерирует пароль длиной в 12 символов. Пароль должен содержать ровно 4 буквы
(не важно какого регистра), не менее одной цифры, не менее одного специального символа. Воспользуйтесь средствами
модуля random и константами модуля string. Будем считать, что последовательность специальных символов включает в себя
!«» #$%&()* +:;=?@ ~
Для разных запусков программы произвольными(случайными) должны быть:
- последовательность символов, для разных запусков, например, на первом месте может стоять буква, или цифра, или
специальный символ
- количество символов разного вида (Например, 1 запуск: 2 больших буквы, 2 маленьких, 5 цифр, 3 спец символа; 2-ой
запуск: 1 большая буква, 3 маленьких буквы, 7 цифр, 1 специальный символ и т.д.)
- количество заглавных и строчных букв
"""

import random
import string

password = []
punctuation = list("!«»#$%&()*+:;=?@~")
letters = set(string.ascii_letters)
digits = string.digits

while len(password) < 12:
    if len(letters.intersection(password)) < 4:
        password.append(list(letters)[random.randint(0, len(letters) - 1)])
    case = random.randint(0, 1)
    if case == 0:
        password.append(digits[random.randint(0, len(digits) - 1)])
    else:
        password.append(punctuation[random.randint(0, len(punctuation) - 1)])
random.shuffle(password)

print(f"Пароль: {''.join(password)}")
print(f"Длина пароля: {len(password)}")
print(f"Количество букв: {len(letters.intersection(password))}")