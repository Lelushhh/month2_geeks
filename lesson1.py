class Car:
    # Конструктор, инициализатор объектов
    def __init__(self, color, model):
        self.color = "red"
        self.model = "Subaru"
    def drive(self, location):
        print(f"Car {self.model} is driving in {location}")
    def test(self):
        self.drive("Karakol")

color = "red"
car_honda = Car(color="red", model="honda" )
car_subaru = Car(color="silver", model="subaru")

car_honda.drive("Bishkek")
car_subaru.test()
print(car_honda)
print(car_subaru)
print(car_honda.color)

"""dunder methods""" # double underscore 