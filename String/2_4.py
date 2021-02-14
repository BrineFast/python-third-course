"""
4. Дана строка, состоящая из слов, разделенных пробелами и символ. Вывести все слова (в строку), которые содержат данный
символ в нижнем или верхнем регистре. Например
строка: Аня и Петя ходили в театр
символ: а
надо вывести: Аня театр
--------
строка: Аня и Петя ходили в театр
символ: А
надо вывести: Аня театр
"""

string = input()
character = input()
words = string.split(' ')
output_string = ''
for word in words:
    if word.lower().__contains__(character.lower()):
        output_string += f"{word} "
print(output_string)