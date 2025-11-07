class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        print("Какое-то животное издает звук")


class Dog(Animal):
    def make_sound(self):
        print("Собака лает: Гав-гав!")


class Cat(Animal):
    def make_sound(self):
        print("Кошка мяукает: Мяу!")


dog = Dog("Барбос", 3)
cat = Cat("Мурка", 2)


dog.make_sound()
cat.make_sound()


dog.set_name("Мухтар")
dog.set_age(4)

cat.set_name("Матроскин")
cat.set_age(3)


print(f"{dog.get_name()}, возраст: {dog.get_age()}")
print(f"{cat.get_name()}, возраст: {cat.get_age()}")