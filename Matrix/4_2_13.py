"""
13) Поменять местами первую строку и строку, сумма элементов которой максимальна.
"""

n_arr_size = int(input('Введите количество строк массива: '))
m_arr_size = int(input('Введите количество столбцов: '))
arr = []
max_row_sum_index = 0
for row in range(n_arr_size):
    arr.append([])
    for col in range(m_arr_size):
        arr[row].append(int(input(f'Введите элемент {row + 1} строки, {col + 1} столбца: ')))
    if sum(arr[max_row_sum_index]) < sum(arr[row]):
        max_row_sum_index = row
arr[0], arr[max_row_sum_index] = arr[max_row_sum_index], arr[0]
for row in arr:
    print(row)