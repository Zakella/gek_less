class Road:
    __length = 0
    __width = 0

    def get_mass(self, length, width, mass, thickness):
        self.__length = length
        self.__width = width
        return self.__length * self.__width * mass * thickness


mass_of_asphalt = Road().get_mass(2, 5, 500, 600)
print(mass_of_asphalt)
