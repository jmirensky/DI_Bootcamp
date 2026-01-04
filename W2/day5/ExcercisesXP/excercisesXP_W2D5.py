#Introduction to OOP

#Exercise 1: Cats
#Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

#Step 1: Create Cat Objects
#Use the Cat class to create three cat objects with different names and ages.

class Cats:
     # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name    #self.attribute = value
        self.age = age
   
cat1 = Cats('Michi', 3)
cat2 = Cats('Milo', 2)
cat3 = Cats('Luna', 9)

#Step 2: Create a Function to Find the Oldest Cat
#Create a function that takes the three cat objects as input.
#Inside the function, compare the ages of the cats to find the oldest one.
#Return the oldest cat object.

cats = (cat1, cat2, cat3)

def find_oldest_cat(cats):
    oldest = cats[0]          

    for cat in cats[1:]:      
        if cat.age > oldest.age:
            oldest = cat

    return oldest             


#Step 3: Print the Oldest Cat’s Details
#Call the function to get the oldest cat.
#Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
#Replace <cat_name> and <cat_age> with the oldest cat’s name and age.

oldest_cat = find_oldest_cat(cats)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


#Exercise 2 : Dogs
#Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.

#Step 1: Create the Dog Class
#Create a class called Dog.
#In the __init__ method, take name and height as parameters and create corresponding attributes.
#Create a bark() method that prints “<dog_name> goes woof!”.
#Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.
class Dogs:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        print(f'{self.name} jumps {self.height*2} cm high!')

#Step 2: Create Dog Objects
#Create davids_dog and sarahs_dog objects with their respective names and heights.
davids_dog = Dogs('Max', 70)
sarahs_dog = Dogs('Inti', 40)

#Step 3: Print Dog Details and Call Methods
#Print the name and height of each dog.
#Call the bark() and jump() methods for each dog.

print(f'Name: {davids_dog.name}, Height: {davids_dog.height} cm')
davids_dog.bark()
davids_dog.jump()

print(f'Name: {sarahs_dog.name}, Height: {sarahs_dog.height} cm')
sarahs_dog.bark()
sarahs_dog.jump()

#Step 4: Compare Dog Sizes
if davids_dog.height > sarahs_dog.height:
    print(f'{davids_dog.name} is taller than {sarahs_dog.name}.')
elif davids_dog.height < sarahs_dog:
    print(f'{davids_dog.name} is smaller than {sarahs_dog.name}.')
else:
     print(f'Both dogs, {davids_dog.name} and {sarahs_dog.name}, have the same height.')



#Exercise 3 : Who’s the song producer? 
#Create a Song class with a method to print song lyrics line by line.
#Step 1: Create the Song Class
#Create a class called Song.
#In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
#Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
#Example:
#stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
#stairway.sing_me_a_song()
#Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

bohemian_rhapsody = Song( ['Is this the real life?',
                'Is this just fantasy?',
                'Caught in a landslide, no escape from reality...'
                ])

bohemian_rhapsody.sing_me_a_song()

#Exercise 4 : Afternoon at the Zoo

#Step 1: Define the Zoo Class
#1. Create a class called Zoo.
#2. Implement the __init__() method:

class Zoo:
    def __init__(self,zoo_name):        #It takes a string parameter zoo_name, representing the name of the zoo.
        self.zoo_name = zoo_name
        self.animals = []               #Initialize an empty list called animals to keep track of animal names.

#3. Add a method add_animal(new_animal):
#    This method adds a new animal to the animals list.
#    Do not add the animal if it is already in the list.

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
                
#4. Add a method get_animals():
#    This method prints all animals currently in the zoo.  

    def get_animals(self):
       print(self.animals)    #print the list of the current animals
     
#5. Add a method sell_animal(animal_sold):
#    This method checks if a specified animal exists on the animals list and if so, remove from it.

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:  #remove only if it exists in the list
            self.animals.remove(animal_sold)

#6. Add a method sort_animals():
#This method sorts the animals alphabetically.
#It also groups them by the first letter of their name.
#The result should be a dictionary where:
    #Each key is a letter.
    #Each value is a list of animals that start with that letter.
     
    def sort_animals(self):
        self.animals.sort()   #sorts the animals list alphabetically.
        
        grouped = {}  #empty dict, to continue grouping by the first letter

        for animal in self.animals:
            first_letter = animal[0].upper()     #Initial capital letter
            if first_letter not in grouped:      #if the letter is not in the dictionary...
                grouped[first_letter] = []       #define it as key and assign an empty list as value
            grouped[first_letter].append(animal)  #to group animals according to their initial letter
            
        self.grouped_animals = grouped  # Saving the dictionary as an attribute, in case we need to use it later.
        print(grouped)    #This is not a good practice.
        #return grouped   #This is a good practice, use return instead of print. 
                          # Return the dictionary so you can manipulate it later.

        
#7. Add a method get_groups():
#This method prints the grouped animals as created by sort_animals().

    def get_groups(self):
        for letter, animals in self.grouped_animals.items():
            print(f'{letter}: {animals}')


#Step 2: Create a Zoo Object
#Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.

zoo_sandiego = Zoo('Zoo San Diego')

zoo_sandiego.add_animal('Lion')
zoo_sandiego.add_animal('Elephant')
zoo_sandiego.add_animal('Giraffe')
zoo_sandiego.add_animal('Zebra')
zoo_sandiego.add_animal('Hippo')
zoo_sandiego.add_animal('Bear')
zoo_sandiego.add_animal('Lemur')
zoo_sandiego.add_animal('Hyena')

zoo_sandiego.get_animals()    
#output --> ['Lion', 'Elephant', 'Giraffe', 'Zebra', 'Hippo', 'Bear', 'Lemur', 'Hyena']

zoo_sandiego.sell_animal('Elephant')
zoo_sandiego.get_animals()
#output --> ['Lion', 'Giraffe', 'Zebra', 'Hippo', 'Bear', 'Lemur', 'Hyena']

zoo_sandiego.sort_animals()
#output --> {'B': ['Bear'], 'G': ['Giraffe'], 'H': ['Hippo', 'Hyena'], 'L': ['Lemur', 'Lion'], 'Z': ['Zebra']}

zoo_sandiego.get_groups()
#output -->
#    B: ['Bear']
#    G: ['Giraffe']
#    H: ['Hippo', 'Hyena']
#    L: ['Lemur', 'Lion']
#    Z: ['Zebra']



#Bonus: Modify the add_animal() method to get *args so you dont need to repeat the method each time for a new animal,
# you can pass multiple animals names separated by a comma.
print('------ B - O - N - U - S ------')

class Zoo:
    def __init__(self,zoo_name):        
        self.zoo_name = zoo_name
        self.animals = []               

#  # Bonus: *args para múltiples animales
    def add_animal(self, *new_animals):   #*new_animals = lista separada por coma
        for animal in new_animals:
            if animal not in self.animals:
                self.animals.append(animal)
                
    def get_animals(self):
       print(self.animals)  

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:  
            self.animals.remove(animal_sold)
     

    def sort_animals(self):
        self.animals.sort()   
        
        grouped = {} 

        for animal in self.animals:
            first_letter = animal[0].upper()   
            if first_letter not in grouped:  
                grouped[first_letter] = []   
            grouped[first_letter].append(animal)
            
        self.grouped_animals = grouped  
        print(grouped)    #This is not a good practice.
        #return grouped   #this is a good practice, instead of print.     
    
    def get_groups(self):
        for letter, animals in self.grouped_animals.items():
            print(f'{letter}: {animals}')


#testing methods

zoo_chicago = Zoo('Zoo Chicago')

zoo_chicago.add_animal('Lion', 'Leopard', 'Elephant', 'Giraffe', 'Zebra', 'Hippo', 'Bear', 'Lemur','Hyena', 'Eagle', 'Goat', 'Buffalo')

zoo_chicago.get_animals()    
#output --> ['Lion', 'Leopard', 'Elephant', 'Giraffe', 'Zebra', 'Hippo', 'Bear', 'Lemur', 'Hyena', 'Eagle', 'Goat', 'Buffalo']

zoo_chicago.sell_animal('Giraffe')
zoo_chicago.get_animals()
#output --> ['Lion', 'Leopard', 'Elephant', 'Zebra', 'Hippo', 'Bear', 'Lemur', 'Hyena', 'Eagle', 'Goat', 'Buffalo']

zoo_chicago.sort_animals()
#output --> {'B': ['Bear', 'Buffalo'], 'E': ['Eagle', 'Elephant'], 'G': ['Goat'],
#             'H': ['Hippo', 'Hyena'], 'L': ['Lemur', 'Leopard', 'Lion'], 'Z': ['Zebra']}

zoo_chicago.get_groups()
#output -->
#    B: ['Bear', 'Buffalo']
#    E: ['Eagle', 'Elephant']
#    G: ['Goat']
#    H: ['Hippo', 'Hyena']
#    L: ['Lemur', 'Leopard', 'Lion']
#    Z: ['Zebra']