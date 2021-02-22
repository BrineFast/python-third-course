"""
3. Дана строка, состоящая из слов, разделенных пробелами. Найти самое короткое слово. Если таких слов несколько,
то вывести все. В программе можно использовать только один цикл
"""

string = input()
words = string.split(' ')
lengths = {}
min_len = -1
for word in words:
    if lengths.__contains__(len(word)):
        lengths[len(word)].append(word)
    else:
        lengths[len(word)] = [word]
    if len(word) < min_len or min_len == -1:
        min_len = len(word)
print(lengths.get(min_len))
