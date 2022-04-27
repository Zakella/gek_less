class Worker:
    def __init__(self):
        self.name = 'Andrew'
        self.surname = "Rayel"
        self.position = 'programmer'
        self.__income = {"wage": 10000,
                         "bonus": 2000}

    def get_wage(self):
        return self.__income["wage"]

    def get_bonus(self):
        return self.__income["bonus"]


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self.get_wage() + self.get_bonus()


hum_1 = Position().get_full_name()
print(hum_1)

hum_1 = Position().get_total_income()
print(hum_1)
