import numpy as np


"""
Задание 1
В файле присутствуют комментарии, описывающие датасет. Комментарии начинаются  с символа '%'. При загрузке датасета
очистите его от всех комментариев. 
"""
print("Задание 1")
df = np.loadtxt(fname='wind-data-1971.csv', comments='%', delimiter=',')
print(df)
print()

"""
Задание 2
При заполнении не был указан год, тогда значение в первой колонке будет  равно 0. Заполните отсутствующие значения
года самостоятельно.
"""
print("Задание 2:")

df[:, 0] = 71
print(df)
print()
print()


"""
Были дни, когда не удавалось снять значение со всех реперных точек.  В этом случае в местах отсутствия измерений
стоит NaN.  Заполните недостающие значения средним значением в этой точке. 
"""
print(df[1])
nan_indexes = np.where(np.isnan(df))
means = np.nanmean(df[:, 3:15], axis=1)
df[nan_indexes] = np.take_along_axis(means, nan_indexes[1], axis=0)
print(df[1])
print()
print()


"""
Задание 3
Посчитайте минимальное, максимальное и среднее значение скорости ветра, а также среднее квадратическое отклонение
скорости ветра, по всем реперным точкам за все дни (каждое значение считается относительно всего сета).
"""
min_speed = np.min(df[:, 3:15])
max_speed = np.max(df[:, 3:15])
average_speed = np.average(df[:, 3:15])
mean_square_deviation = np.std(df[:, 3:15])

print("Задание 3:")
print(f"Минимальная скорость: {min_speed}")
print(f"Максимальная скорость: {max_speed}")
print(f"Среднияя скорость: {average_speed}")
print(f"Среднее квадратичное отклонение скорости: {mean_square_deviation}")
print()
print()

"""
Задание 4
Посчитайте минимальное, максимальное и среднее значение скорости ветра, а также среднее квадратическое отклонение
скорости ветра, каждой реперной точки по всем дням. Для каждой точки должен получиться свой набор значений.
Выведите полученные значения.
"""
min_speed = np.min(df[:, 3:15], axis=0)
max_speed = np.max(df[:, 3:15], axis=0)
average_speed = np.average(df[:, 3:15], axis=0)
mean_square_deviation = np.std(df[:, 3:15], axis=0)
print("Задание 4:")
print(f"Минимальная скорость: {min_speed}")
print(f"Максимальная скорость: {max_speed}")
print(f"Среднияя скорость: {average_speed}")
print(f"Среднее квадратичное отклонение скорости: {mean_square_deviation}")
print()
print()

"""
Задание 5
Посчитайте минимальное, максимальное и среднее значение скорости ветра, а также среднее квадратическое отклонение
скорости ветра, всех реперных точек для каждого дня. Должен получиться свой набор значений для каждого дня.  
Добавьте в датасет новую колонку с максимальными значениями по дням.    
"""
min_speed = np.min(df[:, 3:15], axis=1)
max_speed = np.max(df[:, 3:15], axis=1)
average_speed = np.average(df[:, 3:15], axis=1)
mean_square_deviation = np.nanstd(df[:, 3:15], axis=1)

max_speed_column = np.reshape(max_speed, (max_speed.shape[0], 1))
df_with_max_speed_column = np.hstack((df, max_speed_column))
print("Задание 5:")
print(f"Минимальная скорость: {min_speed}")
print(f"Максимальная скорость: {max_speed}")
print(f"Среднияя скорость: {average_speed}")
print(f"Среднее квадратичное отклонение скорости: {mean_square_deviation}")
print(f"Первая строка датафрейма с дополнительной колонкой: {df_with_max_speed_column[0]}")
print()
print()

"""
Задание 6
Найдите точку с наибольшем значением скорости ветра по всем дням. Выведите целое число, соответствующее номеру этой точки.
"""
print("Задание 6:")
max_speed = np.max(df[:, 3:15], axis=0)
row = np.nanargmax(max_speed)
print(row)
print()
print()

"""
Задание 7
Найдите год, месяц и день, который была зафиксирована самая большая скорость ветра. Выведите найденную дату.
"""
print("Задание 7:")
max_speed = np.max(df[:, 3:15], axis=1)
row = np.nanargmax(max_speed)
print(df[row, 0:3])
print()
print()

"""
Задание 8
Найдите среднюю скорость в январе для каждой реперной точки. Выведите полученные значения.
"""
print("Задание 8:")
january = df[df[:, 1] == 1]
average_speed = np.average(january[:, 3:15], axis=0)
print(average_speed)
print()
print()

"""
Задание 9
Сохраните получившийся датасет в csv файл. Проследите, чтобы целые числа  были сохранены в целочисленном формате, без
нулей в дробной части.  Каждое число с плавающей точкой сохраните с точностью ровно в 4 знака после точки.
"""
print("Задание 9:")
np.savetxt("12_1971_result.csv", df_with_max_speed_column, fmt=', '.join(['%.d']*3 + ['%1.4f']*13))
print("Сохранено в файл: 12_1971_result.csv")
print()
print()

"""
Задание 10
Посчитайте среднюю скорость ветра для каждого месяца в датасете. Выведите полученные значения.
"""
print("Задание 10:")
for i in range(1, 13):
    month = df[df[:, 1] == i]
    average_speed = np.average(np.average(month[:, 3:15], axis=0))
    print(f"Средняя скорость в {i} месяце: {average_speed}")
print()