"""
В первой строчке записано целое число N (1 ≤ N ≤ 1000) — количество Васиных одноклассников.
В следующих N строчках записана информация об их днях рождения. Каждая строчка состоит из трёх частей,
разделённых пробелом — имени одноклассника, дня и месяца его рождения. Имя — это строка из русских букв, день —
исло от 1 до 31, а месяц — строка из набора «янв», «фев», «мар», «апр», «май», «июн», «июл», «авг», «сен», «окт»,
«ноя», «дек».

Пример входных данных
5
Ваня 20 янв
Петя 15 июн
Вася 10 янв
Денис 15 июн
Коля 20 июл
3
июн
дек
янв

Выходные данные
Денис 15 Петя 15
Вася 10 Ваня 20
"""
n_classmates = int(input("Введите количество одноклассиков: "))
classmates = [input(f"{i + 1} одноклассник: ") for i in range(n_classmates)]

n_months = int(input("Введите количество месяцев: "))
months = [input(f"{i + 1} месяц: ") for i in range(n_months)]

result = {month: [] for month in months}
for classmate in classmates:
    classmate = classmate.split()
    if result.keys().__contains__(classmate[2]):
        result[classmate[2]].append([classmate[0], classmate[1]])
for row in result:
    result[row].sort(key=lambda x: (int(x[1]), x[0]))
    s = ''
    for elem in result[row]:
        s += ' '.join(elem) + ' '
    print(s)