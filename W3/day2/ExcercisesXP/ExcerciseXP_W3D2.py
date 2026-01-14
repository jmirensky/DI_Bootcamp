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
    

#Step 1: Create the Siamese Class (and 2 mor races), the three of them inherit from the class Cat
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


#Exercise 2: Dogs

# Step 1: Create the Dog class
class Dog:
    def __init__(self, name, age, weight):
        '''Initializer / Instance Attributes Code'''
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        ''' Code to return bark message'''
        return f"{self.name} is barking"

    def run_speed(self):
        '''Code to estimate run speed based on weight and age'''
        return self.weight / self.age * 10

    def fight(self, other_dog):
        '''Code to determine and return a winner dog, according to fighting ability, 
        based on speed and weight'''
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if self_power > other_power:
            return f"{self.name} won the fight!"
        elif self_power < other_power:
            return f"{other_dog.name} won the fight!"
        else:
            return "It's a tie!"

# Step 2: Create Dog instances
dog1 = Dog("Rex", 4, 20)   # name, age, weight
dog2 = Dog("Firulais", 3, 15)
dog3 = Dog("Rocky", 5, 25)

# Step 3: Test Dog methods
print(dog1.bark())          # Rex is barking
print(dog2.run_speed())     # 50.0
print(dog1.fight(dog2))     # Rex won the fight!
print(dog3.fight(dog1))     # Rocky won the fight!


#Exercise 3: Dogs Domesticated

import random

#inherits from Dog.
class PetDog(Dog):  

    def __init__(self, name, age, weight):
        """
        Initialize a PetDog instance.        
        Calls the parent Dog class constructor to set name, age, and weight.
        Adds an extra attribute 'trained', which is False by default.
        """
        super().__init__(name, age, weight)
        self.trained = False         
    
    def train(self):
        """
        Train the dog.
        Prints the dog's bark and sets the 'trained' attribute to True,
        indicating the dog has learned tricks.
        """
        print(self.bark())
        self.trained = True

    def play(self, *args):
        """
        Play with other dogs.
        Accepts any number of other dog instances via *args.
        Prints a message showing that all the dogs, including self, are playing together.
        """
        dog_names = [self.name] + [dog.name for dog in args]  
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        """
        Make the dog perform a random trick.
        Only allowed if the dog is trained.
        Selects randomly from a predefined list of tricks and prints it.
        If the dog is not trained, prints a warning message.
        """
        if self.trained:
            tricks =["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f'{self.name} {random.choice(tricks)}')
        else:
            print(f'{self.name} is not trained yet!')
    
dog1 = PetDog("Rex", 4, 20)   # name, age, weight
dog2 = PetDog("Firulais", 3, 15)
dog3 = PetDog("Rocky", 5, 25)

dog1.train()  #Rex is barking
dog1.play(dog2, dog3)  # Rex, Firulais, Rocky all play together
dog1.do_a_trick()  #Rex plays dead

print(dog1.name, dog1.age, dog1.weight, "Trained:", dog1.trained)  #Rex 4 20 Trained: True
print(dog2.name, dog2.age, dog2.weight, "Trained:", dog2.trained)  #Firulais 3 15 Trained: False
print(dog3.name, dog3.age, dog3.weight, "Trained:", dog3.trained)  #Rocky 5 25 Trained: False



#Exercise 4: Family and Person Classes

#Step 1: Create the Person Class
class Person:
    '''Represents a person with a first name, age and last name'''
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ''
        
    def is_18(self):
        '''Return True if the person is 18 or older, False otherwise'''
        if self.age >= 18:
            return True
        else:
            return False


#Step 2: Create the Family Class
class Family:
    '''Represents a family with a last name and a list of members'''
    def __init__(self, last_name):
        '''Initialize a Family with a last name and empty list of members'''
        self.last_name = last_name
        self.members = []
        
    def born(self, first_name, age):
        '''Add a new member (born) to the family
        Args:
            first_name (str): First name of the new member.
            age (int): Age of the new member'''
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)

    def check_majority(self, first_name):
        '''Check if a member is 18 or older.
        Args:  --> first_name (str): first name of the member to check'''
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f'{first_name} is over 18, you can go out with your friends.')
                else:
                    print(f'{first_name} is under 18, you cannot go out with your friends.')
                return
        print(f'No member named {first_name} found in the family.')

    def family_presentation(self):
        '''Print the family's last name and each member's first name and age'''
        print('Members:')
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")


# ----- Testing  ------

my_family = Family('Levi')

# Add members
my_family.born('Gal', 20)
my_family.born('Noah', 15)
my_family.born('Aviv', 45)
my_family.born('Sara', 43)

# Check majority
my_family.check_majority("Noah")   # not allowed
my_family.check_majority("Gal")  # allowed
my_family.check_majority("Ruti")  # No member named Ruti found in the family.

# Show family info
my_family.family_presentation()