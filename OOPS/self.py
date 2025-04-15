class Animals:
    def __init__(self, name, animal_type, weight, size):
        self.name = name
        self.animal_type = animal_type
        self.weight = weight
        self.size = size

class Types(Animals):
    def __init__(self, name, animal_type, weight, size):
        super().__init__(name, animal_type, weight, size)

    def describe(self):
        return f'{self.name} is a {self.animal_type} cow, weighing {self.weight}. Its dimensions are {self.size}.'

raj_cow = Types("Jhony", "Desi", "200Kg", "45-56-37")
print(raj_cow.describe())
