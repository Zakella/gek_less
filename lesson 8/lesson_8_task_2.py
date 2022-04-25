def type_logger(callback):
    def wrapper(*args):
        for arg in args:
            print(arg, type(arg))
            result = callback(arg)
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
