
#Exercise 3: Dogs Domesticated

from ExcerciseXP2_W3D2 import Dog
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