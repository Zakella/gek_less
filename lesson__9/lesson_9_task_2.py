class Road:
    __length = 0
    __width = 0

    def get_mass(self, length, width, mass, thickness):
        self.__length = length
        self.__width = width
        return self.__length * self.__width * mass * thickness/1000


mass_of_asphalt = Road().get_mass(20, 5000, 25, 5)
print(mass_of_asphalt)
