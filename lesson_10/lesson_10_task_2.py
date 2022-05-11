from abc import ABC, abstractmethod


class Clothes:

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def calculate(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def calculate(self):
        return 2 * self.growth + 0.3


print(Coat(5).calculate + Suit(15).calculate)
