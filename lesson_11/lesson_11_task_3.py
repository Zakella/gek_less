class NotNumeric(Exception):
    pass

new_list = []

while True:
    value = input("Введите значение: ")
    if value == "stop":
        break
    else:
        try:
            if value.isnumeric():
                new_list.append(value)
            else:
                raise NotNumeric
        except NotNumeric:
            print("Введите только числовое значение")
            continue

print(new_list)
