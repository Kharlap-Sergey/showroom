from Undefined import Undefined
from car import *
from van import *
from customer import *

class Car_showroom():
    def __init__(self):
        self._cars = list()
        self._position = 0

    def add_vehicle(self, vehicle):
        self._cars.append(vehicle) 
        n = len(self._cars)
        p = n

    def get_next_vehicle(self):
        if(len(self._cars) == 0):
            return None
        self._position += 1
        if(len(self._cars) <= self._position):
            self._position = 0

        return self._cars[self._position]

    def _get_current_vehicle(self):
        if(len(self._cars) == 0):
            return None
        if(len(self._cars) <= self._position):
            self._position = 0
        return self._cars[self._position]

    def sell(self, customer):
        vehicle = self._get_current_vehicle()
        if vehicle == None:
            return "There aren't available vehicles in showrooms"

        if(not vehicle._required_license_category in customer.licenses):
            return "error, you don't have enough authority to drive this carr"

        if(customer.available_money < vehicle.charge):
            return "you have not enough money"

        customer.available_money -= vehicle.charge
        customer.add_vehicle(vehicle);
        return "succsess"
        

