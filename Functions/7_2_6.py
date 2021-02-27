"""
Создать рекурсивную функцию, определяющую 𝑁-ый член геометрической прогрессии,
если известен первый член и знаменатель прогрессии.
"""

def geom_progr(n, denom, current_elem):
    if (n == 1):
        return current_elem
    return geom_progr(n - 1, denom, current_elem) * denom

n = int(input("Номер нужного члена прогрессии: "))
denom = int(input("Знаменатель прогрессии: "))
first_elem = int(input("Первый член прогрессии: "))

print(f"{n} член прогрессии: {geom_progr(n, denom, first_elem)}")