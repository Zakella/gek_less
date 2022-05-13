import time
from termcolor import colored


class TrafficLight:

    def __init__(self):
        self.__color = None

    def running(self, color):
        self.color = color
        if color == "red":
            print(colored('Stop!', 'white', 'on_red'))
        elif color == "yellow":
            print(colored('Ready!', 'white', 'on_yellow'))
        elif color == "green":
            print(colored('Go!', 'white', 'on_green'))

        return color


while True:
    new_trafic = TrafficLight().running("red")
    time.sleep(7)
    new_trafic = TrafficLight().running("yellow")
    time.sleep(2)
    new_trafic = TrafficLight().running("green")
    time.sleep(7)
