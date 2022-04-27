class Stationery:
    def __init__(self):
        self.title = "Stationery"

    def draw(self):
        print("«Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Это ручка")


class Pencil(Stationery):
    def draw(self):
        print("Это карандаш")


class Handle(Stationery):
    def draw(self):
        print("Это маркер")


pen = Pen().draw()
pencil = Pencil().draw()
Handle = Handle().draw()
