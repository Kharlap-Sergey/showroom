from customer import Customer
from car import Car
from van import Van
from Car_showroom import Car_showroom

class Console_mainp():
    def __init__(self):
        self.car_showroom = Car_showroom()
        self.customer =  Customer()
    def call_menu(self):
        console_m = "enter 0 to add vehicle in showroom\n\
        enter 1 to show next car in showtoom\n\
        enter 2 to rewrite customer information\n\
        enter 3 to get customer imformation\n\
        enter 4 to buy last showd car\n\
        enter 5 to exit program"
        self.show(console_m)
        choice = self.read_int();
        if(isinstance(choice, int) and 0 <= choice <= 5):
            if choice == 0:
                vehicle = None
                while(vehicle == None):
                    vehicle = self.read_vehicle()
                self.car_showroom.add_vehicle(vehicle)
            elif choice == 1:
                self.show(self.car_showroom.get_next_vehicle())
            elif choice == 2:
                cust = None
                while cust == None:
                    cust = self.read_customer()
                self.customer = cust
            elif choice == 3:
                self.show(self.customer)
            elif choice == 4:
                self.show(self.car_showroom.sell(self.customer))
            elif choice == 5:
                return
        else:
            self.show("error, try again")
        self.call_menu()

    def show(self, mess):
        print(mess)

    def _read(self):
        return input()

    def read_int(self):
        try:
            a = int(self._read())
            return a
        except:
            return None

    def read_string(self):
        return self._read()

    def read_vehicle(self):
        try:
            self.show("enter vehicle type car/van: ")
            tipe = self.read_string()
            if tipe != "car" and tipe != "van":
                return None
            self.show("enter name: ")
            name = self.read_string()
            mass = None
            while mass == None:
                self.show("enter massa: ")
                mass = self.read_int()
            max_speed = None
            while max_speed == None:
                self.show("enter max speed: ")
                max_speed = self.read_int()
            fuel_consumption = None
            while fuel_consumption == None:
                self.show("enter fuel consumption: ")
                fuel_consumption = self.read_int()
            self.show("enter required categoty: ")
            categ = self.read_string()
            charge = None
            while charge == None:
                self.show("enter charge: ")
                charge = self.read_int()

            if tipe == "car":
                class_ = None
                while class_ == None:
                    self.show("enter class: ")
                    class_ = self.read_int()
                self.show("enter abs y/n")
                ans = self.read_string();
                abs = ans == 'y'

                return Car(mass, fuel_consumption, max_speed, name,\
                    charge, class_, abs, categ)
            else:
                carring = None
                while carring == None:
                    self.show("enter carring: ")
                    carring = self.read_int()
                return Van(mass, fuel_consumption, max_speed,\
                    name,  charge, carring, categ)

        except:
            return None

    def read_customer(self):
        try:
            self.show("enter first name: ")
            fname = self.read_string()
            self.show("enter second name: ")
            sname = self.read_string()
            self.show("enter available money that you have: ")
            money = self.read_int()
            self.show("enter you driv categories: ")
            catigories = self.read_string().split()

            return Customer(sname, fname, money, catigories)
        except:
            return None
        
