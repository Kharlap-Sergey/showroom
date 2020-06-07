from Vehicle import Vehicle
from Undefined import Undefined

class Car(Vehicle):
    def __init__(self, massa = Undefined(), fuel_consumption = Undefined(),\
       max_speed = Undefined(), number = Undefined(), charge = Undefined(), comfort_class = Undefined(),\
       ABS_sistem = Undefined(), required_license_category = Undefined()):
        Vehicle.__init__(self, massa, fuel_consumption, max_speed, number)
        self.charge = charge;
        self.ABS_sistem = ABS_sistem;
        self.comfort_class = comfort_class;
        self._required_license_category = required_license_category;

    def __del__(self):
        return self.__str__();

    def __str__(self):
        return "car\n" + super().__str__() + \
            "charge: {0}, comfort_class: {1}, ABS sistem: {2}".\
            format(self.charge, self.comfort_class, self.ABS_sistem); 