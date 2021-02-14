"""
8. Вводится список слов разделенных пробелом. Найти все слова, длина которых больше 5.
Использовать списки для хранения слов.
"""


string = input().split(' ')
words = filter(lambda word: len(word) > 5, string)
print(*words)