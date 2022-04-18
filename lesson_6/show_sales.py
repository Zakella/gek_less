import sys


def show_sales(*args):
    param_list = list(*args)
    with open("bakery.csv", "r", encoding="utf8") as sales:
        begin = 0
        end = sum(1 for line in sales)
        sales.seek(0)
        if len(param_list) == 2:
            begin = int(param_list[1]) - 1
        if len(param_list) == 3:
            begin = int(param_list[1]) - 1
            end = int(param_list[2]) - 1

        for index, line in enumerate(sales):
            if index >= begin and index <= end:
                print(line, end="")



if __name__ == "__main__":
   show_sales(sys.argv)
