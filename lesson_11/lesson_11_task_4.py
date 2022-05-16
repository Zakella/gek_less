import datetime

"""Программа октрывает склад в 9.00 и закрывает в 18.00. В него добаляется оргтехника, в конце дня мы считаем общее 
количество добавленной техники на склад. Каждую технику нужно проверить на работоспособность прежде чем добавить на склад.
"""


class Storage:
    __open = False
    __total_tech = []
    __total_amount = 0

    def __init__(self, name, location, max):
        self.__name = name
        self.__location = location
        self.__max = max

    def __str__(self):
        return self.__name

    @property
    def info(self):
        return {"name": self.__name,
                "location": self.__location,
                "max": self.__max,
                "itsOpen": self.__open}

    @info.setter
    def info(self, open=False):
        self.__open = open

    def add_tech(self, tech):
        for i in self.__total_tech:
            self.__total_amount += i.amount

        if self.__total_amount > self.__max:
            raise f'Превышено максимальное количество ({self.__max}) в складе {self.__name}, пожалуйста воспользуйтесь другим складом!'

        self.__total_tech.append(tech)

    def show_leftovers(self, storage):
        for item in self.__total_tech:
            print(f'Добавлен на склад {self.__name} {item}')


class Equipment:
    amount = 0

    def __init__(self, brand):
        self.brand = brand
        Equipment.amount += 1

    @staticmethod
    def check_workability(tech_type):
        if isinstance(tech_type, Printer):
            result = input(f"Включите принтер {tech_type.model}. Он печатает? ")
            if result == "yes":
                return True
            else:
                raise "Нельзя добавлять на склад неработающую технику!"
        elif isinstance(tech_type, Scanner):
            result = input(f"Введите скорость сканирования модели {tech_type.model}:")
            if not result.isnumeric():
                raise "Не верный ввод данных, должно быть число!"
        elif isinstance(tech_type, Xerox):
            paper_standards = ["A4", "A5", "A0", "A1"]
            result = input(f"Укажите формат бумаги по умолчанию {tech_type.model}:")
            if not result.upper() in paper_standards:
                raise "Не верный формат бумаги!"


class Printer(Equipment):
    amount = 0

    def __init__(self, color, model, amount, brand):
        self.color = color
        self.model = model
        self.amount = amount
        self.brand = brand
        Printer.amount += amount

    def __str__(self):
        return f'Производитель {self.brand} , Модель:{self.model},цвет: {self.color},в количестве {self.amount} '


class Scanner(Equipment):
    amount = 0

    def __init__(self, color, model, amount, brand):
        self.color = color
        self.model = model
        self.amount = amount
        self.brand = brand
        Scanner.amount += amount

    def __str__(self):
        return f'Производитель {self.brand} , Модель:{self.model},цвет: {self.color},в количестве {self.amount} '


class Xerox(Equipment):
    def __init__(self, color, model, amount, brand):
        self.color = color
        self.model = model
        self.amount = amount
        self.brand = brand

    def __str__(self):
        return f'Производитель {self.brand} , Модель:{self.model},цвет: {self.color},в количестве {self.amount} '


def open_storage():
    main_storage = Storage("Main", "NY, Park Lain 5", 15)
    now = datetime.datetime.now()
    currentdate = datetime.datetime.today()
    open_time = currentdate.combine(currentdate.date(), currentdate.min.time()) + datetime.timedelta(hours=9)
    close_time = currentdate.combine(currentdate.date(), currentdate.min.time()) + datetime.timedelta(hours=20)

    if now > open_time:
        main_storage.info = True

    if now > close_time:
        main_storage.info = False

    if not main_storage.info.get("itsOpen"):
        print(f"Склад закрыт! Открытие в {open_time}")
        exit(1)

    tech = Equipment("Canon")
    canon_a50 = Printer("красный", "A50X42", 1, tech.brand)
    result = tech.check_workability(canon_a50)

    if result:
        main_storage.add_tech(canon_a50)

    canon_b60 = Printer("зеленый", "B77", 3, tech.brand)
    result = tech.check_workability(canon_b60)
    if result:
        main_storage.add_tech(canon_b60)

    tech_1 = Equipment("Panasonic")
    scan_six1600 = Scanner("черный", "ScanSnap iX1600", 1, tech_1.brand)
    tech.check_workability(scan_six1600)
    if result:
        main_storage.add_tech(scan_six1600)

    tech_3 = Equipment("Xerox")
    xerox_3025 = Xerox("белый", " Workcentre 3025", 2, tech_3.brand)
    tech_3.check_workability(xerox_3025)
    if result:
        main_storage.add_tech(xerox_3025)

    main_storage.show_leftovers(main_storage)
    print(f"Всего на складе {main_storage}  оргтехники:{Equipment.amount} вида, из них:\n"
          f"Принтеров в количестве {Printer.amount} шт\n"
          f"Сканеров в количестве {Printer.amount} шт\n"
          f"Ксероксов в количестве {Xerox.amount} шт")


if __name__ == "__main__":
    open_storage()
