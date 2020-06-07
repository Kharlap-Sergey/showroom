from Undefined import Undefined

class Vehicle(object):
    """description of class"""
    def __init__(self, massa = Undefined(), fuel_consumption = Undefined(),\
       max_speed = Undefined(), number = Undefined()):
        self.massa = massa
        self.number = number
        self.fuel_consumption = fuel_consumption
        self.max_speed = max_speed

    def __del__(self):
        return self.number;

    def __str__(self):
        return "name: {0}, massa: {1}, fuel_consumption: {2}, max speed: {3}".format(\
            self.number, self.massa, self.fuel_consumption, self.max_speed)

        

