"""
Задан список чисел. Используя стандартную функцию map и анонимную функцию преобразуйте его в список квадратов этих чисел.
Список: [4, 6, 8, 12, 67, 98, 3, 56, 108]
Выходные данные: [16, 36, 64, 144,  4489,  9604, 9, 3136,  11664]
"""

print(*map(lambda x: int(x)*int(x), input().split(', ')))
