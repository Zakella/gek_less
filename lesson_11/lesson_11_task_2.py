class MyDivZero(ZeroDivisionError):
    pass


first_int = input("Введите первое число:")
sec_int = input("Введите второе  число:")

try:
    if int(sec_int) == 0:
        raise MyDivZero

    print(int(first_int) / int(sec_int))
except ValueError:
    print("Не верный тип данных!")
except MyDivZero:
    print("Нельзя делить на ноль!")
