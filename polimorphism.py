class Animal:
    def sound(self):
        print("Unexpected sound")

class Cat(Animal):
    def sound(self):
        print("Muyaw")

class Dog(Animal):
    def sound(self):
        print("Gav gav")


if __name__ == "__main__":
    Dog().sound()
    Cat().sound()