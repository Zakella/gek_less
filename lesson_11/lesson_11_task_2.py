class MyDivZero(ZeroDivisionError):
    pass


firt_int = input("Введите первое число:")
sec_int = input("Введите второе  число:")

try:
    print(int(firt_int) / int(sec_int))
except ValueError:
    print("Не верный тип данных!")
except MyDivZero:
    print("Нельзя делить на ноль!")

