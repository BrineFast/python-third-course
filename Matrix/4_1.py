"""
1. Крестики-нолики
Напишите программу, которая определяет, кто выиграл в крестики-нолики на увеличенном квадратном поле, выстроив подряд
по горизонтали или по вертикали (диагональ не считается) три своих символа: крестики (вывести латинскую букву “x”),
нолики (вывести “o”) или пока никто (вывести “-”). Гарантируется, что на поле нет победы одновременно обоих игроков.
На первой строке вводится натуральное число, не меньшее 3 — размер поля.
Затем идут строки — ряды клеток поля; поставленный крестик обозначается символом “x” (латинская буква x), нолик — “o”
(латинская буква o), пустая клетка — точкой.
Вывести символ победителя: “x”, “o” или если пока никто не выиграл “-”.
Пример:
.o.x
xx.o
ooo.
xxo.

.o.x
xx.o
oxo.
xxo.
"""

#WARNING!! Я мог бы это сделать гораздо проще (добавляя в список строку, а не список чаров), но тема требует именно
#двумерный массив
field_size = int(input('Введите размер поля: '))
field = []
win = False
for row in range(field_size):
    field.append(list(input(f'Введите {row + 1} строку: ')))
for row in field:
    str_row = ''
    for col_num in range(field_size):
        str_row += row[col_num]
    if str_row.__contains__('xxx'):
        print('x')
        win = True
        break
    elif str_row.__contains__('ooo'):
        print('o')
        win = True
        break
if win == False:
    for col_num in range(field_size):
        col = ''
        for row in field:
            col += row[col_num]
        if col.__contains__('xxx'):
            print('x')
            win = True
            break
        elif col.__contains__('ooo'):
            print('o')
            win = True
            break
if win == False:
    print('-')