"""
Входные данные:
В первой строчке записано целое число N (1 ≤ N ≤ 1000) — количество записей о событиях в ежедневнике. В следующих N
строчках записана информация о запланированных делах. В каждой строке сначала записана дата (через точку указывается
число, месяц и год), потом время (через точку указывается час и минуты) и запланированное дело.
В следующей строчке записано целое число M (1 ≤ M ≤ 100) — количество вопросов, на которое надо ответить. В следующих
M строках содержатся сами вопросы. Вопрос — это дата в том же виде: число, месяц и год через точку

Выходные данные:
Для каждого вопроса выведите: дату на отдельной строке, а потом список дел упорядоченных по времени,
каждое дело в отдельной строке.
Если на некоторый день дел было не запланировано, то выведите  просто дату на отдельной строке.
Между делами на разные дни выводите пустую строку

Входные данные
7
9.03.2020 13.00 Стоматолог
10.03.2020 18.30 Встреча с друзьями
9.03.2020 10.00 Стрижка
9.03.2020 19.00 Театр "Вишневый сад"
10.03.2020 8.00 Отвести Ивана в школу
10.03.2020 13.00 Забрать Ивана
8.03.2020 18.00 кафе "Березка"
4
8.03.2020
11.03.2020
09.03.2020
10.03.2020
"""
import datetime

n = int(input('Количество дел: '))
todo = [input(f'{i + 1} дело: ').split() for i in range(n)]
m = int(input('Количество дат: '))
dates = [input(f'{i + 1} дата: ') for i in range(m)]
result = {datetime.datetime.strptime(date, "%d.%m.%Y").date(): [] for date in dates}
for i in todo:
    date = datetime.datetime.strptime(i[0], "%d.%m.%Y").date()
    if date in result:
        result[date].append(i)
    else:
        result[date] = i
    result[date].sort(key=lambda x: int(x[1].replace('.', '')))
print()
for row in result:
    print(datetime.datetime.strftime(row, "%d.%m.%Y"))
    for task in result[row]:
        s = ' '.join(task) + ' '
        print(s)
    print()