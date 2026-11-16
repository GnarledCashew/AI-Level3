# 1. Parent Class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def drive(self):
        print(f"The {self.brand} is moving on {self.wheels} wheels.")

# 2. Child Class (inherits from Vehicle)
class ElectricCar(Vehicle):
    def charge(self):
        print(f"The {self.brand} is charging its battery.")

# Create an object from the Child Class
my_ev = ElectricCar("Tesla", 4)

# Uses a method inherited from Vehicle
my_ev.drive()   # Output: The Tesla is moving on 4 wheels.

# Uses its own method from ElectricCar
my_ev.charge()  # Output: The Tesla is charging its battery.
