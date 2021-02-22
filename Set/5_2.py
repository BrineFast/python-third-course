"""
2. Вводится список целых чисел. Найдите те цифры, которые встречаются только в двухзначных числах (в числах другой
значности они не встречаются) и  выведите их в порядке возрастания.
Входные данные
38 12 2 555 6 639 40000 60
Выходные данные
1  8
"""

k = input().split()
dvuznach, ne_dvuznach = list(filter(lambda x: len(x) == 2, k)), list(filter(lambda x: len(x) != 2, k)), set(), set()
dvuznach_set, ne_dvuznach_set = set(), set()
for i in dvuznach:
    dvuznach_set.update(list(map(lambda x: int(x), list(i.replace('-', '')))))
for i in ne_dvuznach:
    ne_dvuznach_set.update(list(map(lambda x: int(x), list(i.replace('-', '')))))
print(sorted(dvuznach_set.difference(ne_dvuznach_set)))