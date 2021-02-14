"""
3. Обратная польская нотация
Напишите программу, которая производит вычисление выражения, записанного в обратной польской нотации (ОПН).
Работайте со списком как со стеком.
Возможные операции: бинарные + (сложение), - (вычитание), * (умножение), /(деление нацело;
для отрицательных чисел работает по тем же правилам, что и в Питоне); унарные ~ (унарный минус — меняет знак),
! (факториал), # (клонирование — вернуть в стек значение два раза); тернарная @ (возвращает в стек те же три значения,
но в ином порядке: второе, третье, первое). Примеры работы

Ввод	 Вывод
7 2 3 * -       	1
10 15 - 7 *	         -35
7 1 10 100 # * @ - + + ~         	-10016
"""
from math import factorial as fac

string = input('Введите элементы через пробел: ').split(' ')
stack = []
for num in string:
    if num.isdigit():
        stack.append(int(num))
    elif num == '*':
        first, second = stack.pop(), stack.pop()
        stack.append(first * second)
    elif num == '-':
        second, first = stack.pop(), stack.pop()
        stack.append(first - second)
    elif num == '+':
        first, second = stack.pop(), stack.pop()
        stack.append(first + second)
    elif num == '/':
        second, first = stack.pop(), stack.pop()
        stack.append(first // second)
    elif num == '!':
        first = stack.pop()
        stack.append(fac(first))
    elif num == '~':
        stack.append(-stack.pop())
    elif num == '#':
        first = stack.pop()
        stack.append(first)
        stack.append(first)
    elif num == '@':
        third, second, first = stack.pop(), stack.pop(), stack.pop()
        stack.append(second)
        stack.append(third)
        stack.append(first)
print(stack)
