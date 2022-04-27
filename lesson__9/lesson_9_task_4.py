class Car:
    def __init__(self):
        self.speed = 180
        self.color = "black"
        self.name = 'Ford'
        self.is_police = False

    def go(self):
        print("Go!")

    def stop(self):
        print("Stop!")

    def turn(self, direction):
        print("Turn " + direction)

    def show_speed(self, speed):
        print(f"Speed is {speed}")


class TownCar(Car):
    def __init__(self):
        self.speed = 60

    def show_speed(self, speed):
        if speed > self.speed:
            return print(f"Внимание! Превышение скорости")
        else:
            return super().show_speed(speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self):
        self.speed = 40

    def show_speed(self, speed):
        if speed > self.speed:
            return print(f"Внимание! Превышение скорости")
        else:
            return super().show_speed(speed)


class PoliceCar(Car):
    def __init__(self):
        self.is_police = True


town_car = TownCar().go()
town_car = TownCar().turn("left")
town_car = TownCar().show_speed(55)
town_car = TownCar().stop()

work_car = WorkCar().show_speed(41)
