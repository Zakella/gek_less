import datetime


class Storage:
    __open = False

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


class Tech:

    def __init__(self, brand, warranty):
        self.brand = brand
        self.warranty = warranty


class Printer(Tech):

    def __init__(self, color, model, quant):
        self.color = color
        self.model = model
        self.quant = quant


class Scanner(Tech):
    pass


class Xerox(Tech):
    pass


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
        exit()

    canonA50 = Printer()
    canonA50.brand = "Canon"
    canonA50.warranty = 2
    canonA50.color = "green"
    canonA50.model = "A50X42"
    canonA50.quant = 10


if __name__ == "__main__":
    open_storage()
