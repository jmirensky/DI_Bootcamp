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