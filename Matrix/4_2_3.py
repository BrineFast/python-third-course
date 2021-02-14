"""
3) Поменять местами строки по следующему правилу: первую со второй, третью с четвертой и т. д.
"""

n_arr_size = int(input('Введите четное количество строк массива: '))
m_arr_size = int(input('Введите количество столбцов: '))
if n_arr_size % 2 == 0:
    arr = []
    for row in range(n_arr_size):
        arr.append([])
        for col in range(m_arr_size):
            arr[row] += input(f'Введите элемент {row + 1} строки, {col + 1} столбца: ')

    for row_num in range(0, n_arr_size, 2):
        arr[row_num], arr[row_num + 1] = arr[row_num + 1], arr[row_num]
    for row in arr:
        print(row)
else:
    print('Размер массива должен быть четным, т.к. по условию я меняю местами четную и нечетную строки')