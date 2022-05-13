import datetime


class Storage:
    __open = False
    __total_tech = []

    def __init__(self, name, location, max):
        self.__name = name
        self.__location = location
        self.__max = max

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
        self.__total_tech.append(tech)

    def show_leftovers(self, storage):
        for item in self.__total_tech:
            print(item)


class Equipment:

    def __init__(self, brand):
        self.brand = brand

    @staticmethod
    def check_workability(tech_type):
        if isinstance(tech_type, Printer):
            result = input("Включите принтер. Он печатает? ")
            if result == "yes":
                return True
            else:
                raise "Нельзя добавлять на склад не работающую технику!"


class Printer(Equipment):

    def __init__(self, color, model, quant):
        self.color = color
        self.model = model
        self.quant = quant

    def __str__(self):
        return f'{self.model} color {self.color} total pieces {self.quant} '


class Scanner(Equipment):
    def __init__(self, color, model, quant):
        self.color = color
        self.model = model
        self.quant = quant


class Xerox(Equipment):
    def __init__(self, color, model, quant):
        self.color = color
        self.model = model
        self.quant = quant


def open_storage():
    main_storage = Storage("Main", "NY, Park Lain 5", 500)
    now = datetime.datetime.now()
    currentdate = datetime.datetime.today()
    open_time = currentdate.combine(currentdate.date(), currentdate.min.time()) + datetime.timedelta(hours=9)
    close_time = currentdate.combine(currentdate.date(), currentdate.min.time()) + datetime.timedelta(hours=20)

    if now > open_time:
        main_storage.info = True

    if now > close_time:
        main_storage.info = False

    if not main_storage.info.get("itsOpen"):
        print(f"Storage is closed! Open time in {open_time}")
        exit(1)

    tech = Equipment("Canon")
    canon_a50 = Printer("green", "A50X42", 1)
    result = tech.check_workability(canon_a50)

    if result:
        main_storage.add_tech(canon_a50)

    # canon_b60 = Printer("green", "B77", 1)


    main_storage.show_leftovers(main_storage)
        # print(main_storage.total_tech)


if __name__ == "__main__":
    open_storage()
