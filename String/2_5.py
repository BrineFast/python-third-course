"""
5. Дана строка, содержащая слова и числа, разделенные запятой и пробелом (", "). Посчитать сумму чисел в этой строке.
Для строки: mam, 23, dead, 25, 5, son
ответ:  53
"""

string = input()
integers = string.split(', ')
print(sum([int(integer) for integer in integers if integer.isdigit()]))