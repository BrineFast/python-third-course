"""
6. Дан текст, состоящий из предложений. Найдите предложения - палиндромы (без учета пробелов и знаков препинания
предложения читаются одинаково справа налево и слева направо)
Например, для строки "Леша не клопа на полке нашел. На столе лежала книга. У лип Леша нашел пилу."
Должно быть выведено:
Леша не клопа на полке нашел
У лип Леша нашел пилу
"""

string = input()
sentences = string.strip('!?,;:').split('.')
for sentence in sentences:
    if sentence.lower().replace(' ', '') == sentence.lower().replace(' ', '')[::-1]:
        print(sentence)