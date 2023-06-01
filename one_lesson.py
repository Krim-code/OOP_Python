class Animal:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Cat(Animal):
    def __init__(self, name, age, type_cat):
        super().__init__(name, age)
        self.type_cat = type_cat

    def __str__(self):
        return f"{'Cat':*^50}\n{f'Cat name:':<15}{self.name}" \
               f"\n{f'Cat age:':<15}{self.age}" \
               f"\n{f'Cat type:':<15}{self.type_cat} "


if __name__ == '__main__':
    Mur = Cat("Mur", 4, "British")
    print(Mur)