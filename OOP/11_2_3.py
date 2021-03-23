"""
Реализовать класс в соответствии со своим вариантом и продемонстрировать его работу. Использовать инструкцию try ...
except ... для того, чтобы "отлавливать" ошибки.
№3 Класс обыкновенной дроби с атрибутами целая часть, числитель, знаменатель. Обратите внимание, что дроби могут быть
как положительными так и отрицательными. Для этого класса:

1) определить метод __init__
2) переопределить операции сравнения (==, !=, <, <=, >, >=),
3) переопределить операции сложения(+), вычитания(-), умножения(*), деления(/), возведение в степень(**)
4) переопределить методы trunc, round, ceil, floor
5) написать метод приведения к правильной дроби,
6) написать метод перевода в десятичную дробь,
7) переопределить функцию __str__  для того, чтобы можно было использовать вывод дроби в виде:  print(<экземпляр класса>)
8) написать методы сравнения с 0
"""

class Fraction:

    def __init__(self, whole, numerator, denominator):
        if denominator == 0:
            raise Exception("Знаменатель не может быть равен 0")
        self.whole = whole
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if (self.numerator * self.whole) / self.denominator == other:
                return True
            return False
        try:
            if (self.numerator * self.whole) / self.denominator == (other.numerator * other.whole) / other.denominator:
                return True
            return False
        except Exception:
            "Деление на 0"

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if (self.numerator * self.whole) / self.denominator < other:
                return True
            return False
        try:
            if (self.numerator * self.whole) / self.denominator < (other.numerator * other.whole) / other.denominator:
                return True
            return False
        except Exception:
            "Деление на 0"

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if (self.numerator * self.whole) / self.denominator > other:
                return True
            return False
        try:
            if (self.numerator * self.whole) / self.denominator > (other.numerator * other.whole) / other.denominator:
                return True
            return False
        except Exception:
            "Деление на 0"

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if (self.numerator * self.whole) / self.denominator <= other:
                return True
            return False
        try:
            if (self.numerator * self.whole) / self.denominator <= (other.numerator * other.whole) / other.denominator:
                return True
            return False
        except Exception:
            "Деление на 0"

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if (self.numerator * self.whole) / self.denominator >= other:
                return True
            return False
        try:
            if (self.numerator * self.whole) / self.denominator >= (other.numerator * other.whole) / other.denominator:
                return True
            return False
        except Exception:
            "Деление на 0"

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if (self.numerator * self.whole) / self.denominator != other:
                return True
            return False
        try:
            if (self.numerator * self.whole) / self.denominator != (other.numerator * other.whole) / other.denominator:
                return True
            return False
        except Exception:
            "Деление на 0"

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Fraction(self.whole + other, self.numerator, self.denominator)
        return Fraction(self.whole + other.whole, self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) and self.whole >= other:
            return Fraction(self.whole - other, self.numerator, self.denominator)
        elif isinstance(other, int) or isinstance(other, float):
            return Fraction(self.whole - other, self.numerator - (other * self.denominator), self.denominator)
        return Fraction(self.whole - other.whole, self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Fraction(self.whole, self.numerator * other, self.denominator)
        return Fraction(self.whole * other.whole, self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Fraction(self.whole, self.numerator, self.denominator * other)
        return Fraction(self.whole / other.whole, self.numerator * other.denominator, self.denominator * other.numerator)

    def __pow__(self, power, modulo=None):
        return Fraction(self.whole, self.numerator ** power, self.denominator ** power)

    def __trunc__(self):
        if self.numerator < 0:
            return -(-self.numerator // self.denominator)
        return self.numerator // self.denominator

    def __round__(self, n=None):
        if n > 0:
            return Fraction(self.whole, round(self.numerator / self.denominator * 10 ** n), 10 ** n)
        return Fraction(self.whole, round(self.numerator / self.denominator / 10 ** n) * 10 ** n)

    def __ceil__(self):
        return -(-self.numerator // self.denominator)

    def __floor__(self):
        return self.numerator // self.denominator

    def to_decimal(self):
        return self.numerator / self.denominator + self.whole

    def __str__(self):
        return f"({self.whole}({self.numerator} / {self.denominator}))"

    def to_correct(self):
        whole_part = self.numerator // self.denominator + self.whole
        return Fraction(whole_part, self.numerator - self.denominator, self.denominator)


if __name__ == "__main__":
    first_fraction = Fraction(1, 1, 2)
    second_fraction = Fraction(2, 3, 2)
    third_fraction = Fraction(3, 6, 4)
    fourth_fraction = Fraction(4, 7, 4)
    fifth_fraction = Fraction(0, 13, 4)

    print(f"{first_fraction} > {second_fraction}: {first_fraction > second_fraction}")
    print(f"{first_fraction} < {second_fraction}: {first_fraction < second_fraction}")
    print(f"{first_fraction} <= {second_fraction}: {first_fraction <= second_fraction}")
    print(f"{first_fraction} >= {second_fraction}: {first_fraction >= second_fraction}")
    print(f"{third_fraction} == {second_fraction}: {third_fraction == second_fraction}")
    print(f"{third_fraction} == {third_fraction}: {third_fraction == third_fraction}")
    print(f"{third_fraction} >= {second_fraction}: {third_fraction >= second_fraction}")
    print(f"{third_fraction} <= {second_fraction}: {third_fraction <= second_fraction}")
    print(f"{third_fraction} != {third_fraction}: {third_fraction != third_fraction}")
    print(f"{first_fraction} != {second_fraction}: {first_fraction != second_fraction}")
    print(f"{first_fraction} > 0: {first_fraction > 0}")
    print(f"{first_fraction} > 2: {first_fraction > 2}")
    print(f"{first_fraction} < 2: {first_fraction < 2}")
    print(f"{first_fraction} == 2: {first_fraction == 2}")
    print(f"{third_fraction} == 1.5: {third_fraction == 1.5}")
    print(f"{first_fraction} to decimal: {first_fraction.to_decimal()}")
    print(f"{third_fraction} to correct: {third_fraction.to_correct()}")
    print(f"{fourth_fraction} round 2: {fourth_fraction.__round__(2)}")
    print(f"{third_fraction} ceil: {third_fraction.__ceil__()}")
    print(f"{first_fraction} floor: {third_fraction.__floor__()}")
    print(f"{fifth_fraction} trunc: {fifth_fraction.__trunc__()}")
    print(f"{first_fraction} ** 2: {first_fraction ** 2}")
    print(f"{first_fraction} + 2: {first_fraction + 2}")
    print(f"{fifth_fraction} - 10: {fifth_fraction - 10}")
    print(f"{fifth_fraction} - 120: {fifth_fraction - 120}")
    print(f"{fifth_fraction} * 2: {fifth_fraction * 2}")
    print(f"{first_fraction} / 2: {fifth_fraction / 2}")
    print(f"{second_fraction} - {first_fraction}: {second_fraction - first_fraction}")
    print(f"{second_fraction} + {first_fraction}: {second_fraction + first_fraction}")
    print(f"{second_fraction} * {first_fraction}: {second_fraction * first_fraction}")
    print(f"{second_fraction} / {first_fraction}: {second_fraction / first_fraction}")
