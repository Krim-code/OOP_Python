class Person:
    def __init__(self):
        self._name = "Unknown"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __str__(self):
        return f"class Person having the name {self._name}"


if __name__ == "__main__":
    Person = Person()
    print(Person)

    Person.name = "Tim"
    print(Person)
