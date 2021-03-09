"""
Вводится дата и количество дней N. Воспользуйтесь средствами модуля datetime.
Выведите:
-  дату и день недели за N дней до введенной
- дату и день недели через N дней после введенной
Входные данные:
Дата: 12.04.2020
N = 3

Выходные данные:
9.04.2020 — четверг
15.04.2020 — среда
"""

from datetime import datetime, timedelta

date = datetime.strptime(input("Дата: "), "%d.%m.%Y")
days = int(input("Количество дней: "))
week_days = {1: "понедельник", 2: "вторник", 3: "среда", 4: "четверг", 5: "пятница", 6: "суббота", 7: "воскресенье"}
previous_date = date - timedelta(days)
next_date = date + timedelta(days)
print(f"{datetime.strftime(previous_date, '%d.%m.%Y')} - {week_days.get(previous_date.isoweekday())}")
print(f"{datetime.strftime(next_date, '%d.%m.%Y')} - {week_days.get(next_date.isoweekday())}")
