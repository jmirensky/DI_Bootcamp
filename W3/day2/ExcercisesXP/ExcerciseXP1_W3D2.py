#Exercise 1: Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals    #[]

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True   #class atribute

    def __init__(self, name, age):  #instances
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'  #method
    
    def sing(self, sounds):
        return f'{sounds}'
    

#Step 1: Create the Siamese Class (and 2 more races), the three of them inherit from the class Cat
class Siamese(Cat):          
    def intro(self):
        return f'{self.name} is a {self.age} years old Siames Cat'
    
class Bengal(Cat):
    def intro(self):
        return f'{self.name} is a {self.age} years old Bengal Cat'

class Persian(Cat):
    def intro(self):
        return f'{self.name} is a {self.age} years old Persian Cat'

#Step 2: Create a List of Cat Instances
siamese_cat = Siamese("Nina", 2) 
bengal_cat = Bengal("Luna", 3)
persian_cat = Persian("Milo", 5)

list_cats = [siamese_cat, bengal_cat, persian_cat]

#Step 3: Create a Pets instance of the list of cat instances
sara_pets = Pets(list_cats)

#Step 4: Take Cats for a Walk
sara_pets.walk()


# Pets (not a parent class) => contains cats, manages them, makes them walk --> composition, not inheritance.

# Cat (base class) = > all cats have in common: attributes [name, age] - behaviors [walk()  sing()] - class attribute [is_lazy]
# │
# ├── Siamese   (child class)
# ├── Bengal    (child class)
# └── Persian   (child class)