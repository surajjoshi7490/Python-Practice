# Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

my_car=Car("BMW","M5")
print(my_car.brand)
print(my_car.model)
