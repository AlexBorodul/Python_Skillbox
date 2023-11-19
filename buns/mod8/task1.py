class Transport():
    def __init__(self, coordinates=(0, 0), speed=100, brand='', year=0, number=0):
        self.__coordinates = coordinates
        self.__speed = speed
        self.__brand = brand
        self.__year = year
        self.__number = number

    def __str__(self) -> str:
        '''
           Представление всей информации для вывода в методе print()
        '''
        return f'{self.coordinates}, {self.speed}, {self.brand}, {self.year}, {self.number}'

    @property
    def transport_coordinates(self) -> tuple:
        return self.__coordinates

    @transport_coordinates.setter
    def transport_coordinates(self, coordinates):
        if type(coordinates) is not tuple:
            raise Exception("Введено значение неверного типа")
        self.__coordinates = coordinates

    @property
    def transport_speed(self) -> int:
        return self.__speed

    @transport_speed.setter
    def transport_speed(self, speed):
        if type(speed) is not int:
            raise Exception("Введено значение неверного типа")
        if speed < 0: raise Exception("Введено значение меньше нуля")
        self.__coordinates = coordinates

    @property
    def transport_coordinates(self) -> tuple:
        return self.__coordinates

    @transport_coordinates.setter
    def transport_coordinates(self, coordinates):
        if type(coordinates) is not tuple:
            raise Exception("Введено значение неверного типа")
        self.__coordinates = coordinates

    @property
    def transport_speed(self) -> int:
        return self.__speed

    @transport_speed.setter
    def transport_speed(self, speed):
        if type(speed) is not int:
            raise Exception("Введено значение неверного типа")
        if speed < 0: raise Exception("Введено значение меньше нуля")
        self.__speed = speed

    @property
    def transport_year(self) -> int:
        return self.__year

    @transport_year.setter
    def transport_year(self, year):
        if type(year) is not int:
            raise Exception('Введенно неверное значение')
        if year < 0: raise Exception("Введено значение меньше нуля")
        self.__year = year

    @property
    def transport_brand(self) -> str:
        return self.__brand

    @transport_brand.setter
    def transport_brand(self, brand):
        if type(brand) is not str:
            raise Exception('Введено неверное значение')
        self.__brand = brand

    @property
    def transport_number(self) -> int:
        return self.__number

    @transport_number.setter
    def transport_number(self, number):
        if type(number) is not int:
            raise Exception('Введено неверное значение')
        if number < 0:
            raise Exception('Введено значение меньше нуля')
        self.__number = number

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданной области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        return (pos_x <= self.coordinates[0] <= pos_x + length) and (pos_y <= self.coordinates[1] <= pos_y + width)


class Passenger():
    def __init__(self, capacity, passengers):
        self.__passengers_capacity = capacity
        self.__number_of_passengers = passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity) -> None:
        if type(passengers_capacity) is not int:
            raise Exception("Введено значение неверного типа")
        if passengers_capacity < 0: raise Exception("Введено значение меньше нуля")
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers) -> None:
        if type(number_of_passengers) is not int:
            raise Exception("Введено значение неверного типа")
        if number_of_passengers < 0: raise Exception("Введено значение меньше нуля")
        self.__number_of_passengers = number_of_passengers


class Cargo():

    def __init__(self, carrying):
        self.__carrying = carrying

    @property
    def carrying(self) -> float:
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying) -> None:
        if type(carrying) is not float:
            raise Exception("Введено значение неверного типа")
        if carrying < 0: raise Exception("Введено значение меньше нуля")
        self.__carrying = number_of_passengers


class Plane(Transport):
    def __init__(self, height=0):
        super().__init__(coordinates, speed, brand, year, number)
        self.__height = height

    @property
    def plane_height(self) -> float:
        return self.__height

    @plane_height.setter
    def plane_height(self, height):
        if type(height) is not float:
            raise Exception("Введено значение неверного типа")
        if height < 0: raise Exception("Введено значение меньше нуля")
        self.__height = number_of_passengers


class Auto(Transport):
    def __init__(self):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, name, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.__name = name
        self.__port = port

    @property
    def ship_name(self) -> str:
        return self.__name

    @ship_name.setter
    def ship_name(self, name):
        if type(name) is not str:
            raise Exception("Введено значение неверного типа")
        self.__name = name

    @property
    def ship_port(self) -> str:
        return self.__port

    @ship_port.setter
    def ship_port(self, port):
        if type(port) is not str:
            raise Exception("Введено значение неверного типа")
        self.__port = port


class Car(Auto):
    def __init__(self):
        super().__init__()


class Bus(Auto, Passenger):
    def __init__(self):
        super().__init__()


class CargoAuto(Auto, Cargo):
    def __init__(self):
        super().__init__()


class Boat(Ship):
    def __init__(self):
        super().__init__(name, port)


class PassengerShip(Ship, Passenger):
    def __init__(self):
        Ship.__init__(self, name, port)
        Passenger.__init__(self, capacity, passengers)


class CargoShip(Ship, Cargo):
    def __init__(self):
        Ship.__init__(self, name, port)
        Cargo.__init__(self, carrying)

