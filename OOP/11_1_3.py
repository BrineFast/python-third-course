"""
Определить иерархию классов (в соответствии с вариантом – выделить базовый и производные). Реализовать классы
(самостоятельно задать атрибуты и методы класса). Написать демонстрационную программу, в которой создаются объекты
различных классов.
№3  Классы: автомобиль (марка, номер), поезд (номер, количество вагонов, количество пассажиров в вагоне), транспортное
средство (средняя скорость, вид топлива, год выпуска)
"""


class TransportVehicle:

    def __init__(self, average_speed, fuel_type, release_year):
        self.average_speed = average_speed
        self.fuel_type = fuel_type
        self.release_year = release_year
        self.started = False

    def start(self):
        if self.started:
            self.started = True
            print("Транспорт заведен успешно")
        else:
            print("Траспорт уже заведн")

    def stop(self):
        if self.started:
            print("Траспорт заглушен успешно")
        else:
            print("Траспорт не заведен")

    def move(self, direction_from, direction_to):
        if not self.started:
            self.start()
        print(f"Траспорт движется из {direction_from} в {direction_to} со скоростью {self.average_speed}")
        print(f"Траспорт прибыл в {direction_to}")


class Train(TransportVehicle):

    def __init__(self, average_speed, fuel_type, release_year, number, passengers_amount, carriage_amount):
        super().__init__(average_speed, fuel_type, release_year)
        self.number = number
        self.passengers_amount = passengers_amount
        self.carriage_amount = carriage_amount

    def move(self, direction_from, direction_to):
        if not self.started:
            self.start()
        print(f"Поезд номер {self.number} выехал со станции {direction_from} с {self.passengers_amount} пассажирами")
        print(f"Поезд номер {self.number} движется с {self.carriage_amount} вагонами")
        print(f"Поезд прибыл на станцию {direction_to} с {self.passengers_amount} пассажирами")

class Car(TransportVehicle):
    def __init__(self, average_speed, fuel_type, release_year, number, brand):
        super().__init__(average_speed, fuel_type, release_year)
        self.number = number
        self.brand = brand

    def move(self, direction_from, direction_to):
        if not self.started:
            self.start()
        print(f"Автомобиль {self.brand} {self.fuel_type} года выпуска с номером {self.number} выехал из {direction_from}")
        print(f"Атомобиль {self.brand} с номером {self.brand} прибыл в {direction_to} со средней скоростью {self.average_speed}")

    def refill(self, amount):
        print(f"Атомобиль {self.brand} с номером {self.brand} заправился {amount} литрами {self.fuel_type}")

if __name__ == "__main__":
    car1 = Car(54, "Бензин", 2010, "A394XO", "Mercedes-Benz")
    car2 = Car(34, "Газ", 2003, "P337XB", "Lada")
    car1.start()
    car1.move("Саратов", "Энгельс")
    car2.move("Вольск", "Волгоград")
    car1.refill(39)
    car2.stop()
    print()
    print()
    print()
    train1 = Train(143, "Дизель", 1989, "385473", 320, 11)
    train2 = Train(90, "Электричество", 2010, "476543", 30, 3)
    train1.move("Санкт-Петербург", "Краснодар")
    train2.start()
    train2.stop()