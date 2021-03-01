"""
Дан текстовый файл. Найти в нем строку, в которой доля (в процентах) вхождения символа С наибольшая. Напишите функцию
для расчета доли вхождения некоторой буквы в строку. При подсчете общего количества символов в строке надо учитывать
только буквы, а пробельные символы, цифры? знаки препинания и специальные символы не учитываются.
В первой строке входного файла содержится единственный символ С, являющийся строчной латинской буквой. В следующих
строках содержится текст, состоящий из строчных латинских букв и пробелов.
В выходной файл выведите два целых числа через пробел - долю вхождения символа в процентах в искомую строку
(округленная до целого числа) и номер строки. Если в тексте несколько строк, удовлетворяющих условию задачи,
найдите такую строку с наименьшим номером.
"""
import string

try:
    with open('utils/file.txt', encoding='utf-8') as f:
        text = f.read()
        rows = text.split("\n")
    f.close()
except Exception:
    raise Exception("Файл не найден")

def letter_occurrence(letter, rows):
    result = []
    min_index = len(rows)
    for row in rows[1:]:
        delete_punctuation = row.maketrans(dict.fromkeys(string.punctuation))
        delete_digits = row.maketrans(dict.fromkeys(string.digits))
        delete_whitespaces = row.maketrans(dict.fromkeys(string.whitespace))
        row = row.translate(delete_punctuation).translate(delete_digits).translate(delete_whitespaces).lower()
        try:
            result.append(int(row.count(letter) / len(row) * 100))
        except Exception:
            pass
        max_index = result.index(max(result))
        if max_index < min_index:
            min_index = max_index

    return (min_index + 1, max(result))

result = letter_occurrence(text[0], rows)
print(f"Буква '{text[0]}' занимает {result[1]}% позиций в строке {result[0]}")