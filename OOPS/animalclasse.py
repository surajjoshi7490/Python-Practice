class Animals:
    def __init__(self,name , animal_type , weight,size):
        self.name=name
        self.type=type
        self.weight=weight
        self.size=size

class Types(Animals):
    def __init__(self,name,animal_type,weight,size):
        super().__init__(name,animal_type,weight,size)
    def cows(self):
        return f'{self.name} is a {self.animal_type} and weight of this Cow is {self.weight} . Its dimentions are {self.size}'

raj_cow=Types("jhony","Desi","200Kg",'45-56-37')
print(raj_cow.name)