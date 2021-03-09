"""
С клавиатуры вводится дата рождения в формате dd.mm.yyyy некоторого человека.  С помощью средств модуля datetime
определить сколько лет данному человеку. Определить на какой день недели выпадает его следующий день рождения (даже
если он будет в следующем календарном году).
Текущая дата определяется программным путем, а не вводится. Если предположить, что сегодня 01.03.2021, то получим
следующие тестовые данные

Входные данные:
Дата рождения: 20.04.2020

Выходные данные:
Возраст 0 лет
Следующий день рождения: 20.04.2021 - вторник
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

date = datetime.strptime(input("День рождения: "), "%d.%m.%Y")
week_days = {1: "понедельник", 2: "вторник", 3: "среда", 4: "четверг", 5: "пятница", 6: "суббота", 7: "воскресенье"}
today = datetime.today()
next_birthday_year = 0
if today.month > date.month or (today.month == date.month and today.day >= date.day):
    next_birthday_year = today.year + 1
else:
    next_birthday_year = today.year
years_delta = relativedelta(today, date).years
next_birthday = datetime.strptime(f"{date.day}.{date.month}.{next_birthday_year}", '%d.%m.%Y')
print(f"Возраст {years_delta} лет")
print(f"{next_birthday.date()} - {week_days.get(next_birthday.isoweekday())}")
