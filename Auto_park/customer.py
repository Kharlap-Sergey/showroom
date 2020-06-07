from Undefined import Undefined
class Customer(object):
    """description of class"""
    def __init__(self, first = Undefined(), second = Undefined()\
        , available_money = Undefined(), licenses = Undefined()):
        self.first = first;
        self.second = second;
        self.available_money = available_money;
        self.licenses = licenses;
        self._vehicles = []

    def add_vehicle(self, vehicle):
        self._vehicles.append(vehicle)

    def __str__(self):
        ans = "";
        ans += "first name: {0}, second name: {1}, available money: {2}\n".\
            format( self.first, self.second, self.available_money)
        ans += "cars:"
        for vehicle in self._vehicles:
            ans += "\n" + str(vehicle) 
        return ans




