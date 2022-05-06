class Cell:
    def __init__(self, quant):
        self.quant = quant

    def __str__(self):
        return str(self.quant)

    def __add__(self, other):
        return Cell(self.quant + other.quant)

    def __sub__(self, other):
        result = self.quant - other.quant
        if result < 0:
            raise "Отрицательная разность"
        return result

    def __mul__(self, other):
        return self.quant * other.quant

    def __floordiv__(self, other):
        return self.quant // other.quant

    def make_order(self, row):
        result = ["*" * row] * (self.quant // row)
        if self.quant % row:
            result.append("*" * (self.quant % row))
        return "\n".join(result)


cell_1 = Cell(5)
cell_2 = Cell(13)
cell_3 = Cell(20)
cell_4 = cell_1 + cell_2 + cell_3
print(cell_4)

print(cell_3 - cell_1)
print(cell_3 * cell_1)

cell_5 = cell_3 // cell_2
print(cell_5)

result = cell_2.make_order(5)
print(result)
