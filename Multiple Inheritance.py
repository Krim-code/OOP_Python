class Car:
    def drive(self):
        print("I can drive")

    def fly(self):
        print("I can`t fly")


class Bird:
    def drive(self):
        print("I can`t drive")

    def fly(self):
        print("I can fly")


class Test:
    def test(self):
        print("ttttteeeeeest")


class Jet(Car, Bird, Test):
    def fly(self):
        super(Car,self).fly()


Jet().drive()
Jet().fly()
Jet().test()