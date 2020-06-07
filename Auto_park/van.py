from Vehicle import Vehicle
from Undefined import Undefined

class Van(Vehicle):
    def __init__(self, massa = Undefined(), fuel_consumption = Undefined(),\
       max_speed = Undefined(), number = Undefined(), charge = Undefined(), carrying  = Undefined(),\
       required_license_category = Undefined()):
        Vehicle.__init__(self, massa, fuel_consumption, max_speed, number)
        self.charge = charge;
        self.carrying  = carrying ;
        self._required_license_category = required_license_category;

    def __del__(self):
        return self.__str__();

    def __str__(self):
        return "van\n" + super().__str__() + \
            "charge: {0}, carrying : {1}".\
            format(self.charge, self.carrying); 