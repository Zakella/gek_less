import sys


def add_sale(summ):
    if its_float(summ.replace(",", '.')):
        with open("bakery.csv", "a+", encoding="utf8") as sales:
            sales.write(str(summ) + "\n")



def its_float(summ):
    try:
        float(summ)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    add_sale(sys.argv[1])
