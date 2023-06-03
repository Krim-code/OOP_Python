class Car:
    def drive(self):
        print("I can drive")


class Bird:
    def fly(self):
        print("I can fly")


class Jet(Car, Bird):
    pass


Jet().drive()
Jet().fly()