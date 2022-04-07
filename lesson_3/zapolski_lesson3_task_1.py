# вариант 1
def num_translate_adv(val):
    dict = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    capitalized = val.istitle()
    if capitalized:
        result = dict.get(val.lower())
    else:
        result = dict.get(val)
    if result is None:
        print("Невозможно перевести введенное значение!")
    else:
        rusult_final = lambda capitalized: result.title() if capitalized else result
        print(rusult_final(capitalized))


num_translate_adv(input('Введите число: '))
