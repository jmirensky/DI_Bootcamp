#Daily challenge: Old MacDonald’s Farm

#Step 1: Create the Farm Class
    #Create a class called Farm.
    #This class will represent a farm and its animals.

#Step 2: Implement the __init__ Method
    # The Farm class should have an __init__ method.
    # It should take one parameter: farm_name.
    # Inside __init__, create two attributes: name to store the farm’s name and animals 
        #    to store the animals (initialize as an empty dictionary).

# Step 3: Implement the add_animal Method
    #Create a method called add_animal.
    #It should take two parameters: animal_type and count (with a default value of 1). 
    # Count is the quantity of the animal that will be added to the animal dictionary.       
    #If the animal_type already exists in the animals dictionary, increment its count by count.
    #If it doesn’t exist, add it to the dictionary as the key and with the given count as value.

#Step 4: Implement the get_info Method
    #Create a method called get_info.
    #It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
    #Format the output to match the provided example.
    #Use string formatting to align the animal names and counts into columns.

# Step 5: Test Your Code
    # Create a Farm object and call the add_animal and get_info methods.
    # Verify that the output matches the provided example.

#Bonus: Expand The Farm

#Step 6: Implement the get_animal_types Method
    #Add a method called get_animal_types to the Farm class.
    #This method should return a sorted list of all animal types (keys from the animals dictionary).
    #Use the sorted() function to sort the list.

#Step 7: Implement the get_short_info Method
    #Add a method called get_short_info to the Farm class.
    #This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
    #Call the get_animal_types method to get the list of animals.
    #Construct the string, adding an “s” to the animal name if its count is greater than 1.
    #Use string formatting to create the output.

#Step 8: upgrade the add_animal Method
    #use **kwargs for passing multiple animals. The keys will be the animal name and the value will be the quantity.
    #Then you can call the method this way: macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)

class Farm:
    '''This class will represent a farm and its animals'''
        
        # Initializer / Instance Attributes
    def __init__(self, farm_name):   
        self.name = farm_name
        self.animals = {}      # {animal_type : count}
        

    # def add_animal(self, animal_type, count=1):
    #     '''code to add a new animal to the farm or increases its count if it already exists'''
    #     if animal_type in self.animals:
    #         self.animals[animal_type] += count
    #     else:
    #         self.animals[animal_type] = count
           
    def add_animal(self, **kwargs):   # IMPROVED VERSION --> to upgrade the first add_animal Method
        '''code to add multiple animals to the farm and update their quantities'''
        for animal, count in kwargs.items():
            if count is None or count ==0:     # Prevents invalid quantities (None or 0) by defaulting to 1
                count = 1

            self.animals[animal] = self.animals.get(animal, 0) + count


    def get_info(self):
        '''code to display the farm’s name, the animals with their counts, and the “E-I-E-I-0!” phrase'''
        result = f'{self.name}\'s farm\n\n'
        
        for animal_type, count in self.animals.items():
            result += f'{animal_type:<6} : {count}\n'
        
        result += "\n   E-I-E-I-0!"
        
        return result

    
    def get_animal_types(self):
        '''code to return a sorted list of all animal types''' 
        return sorted(self.animals.keys())
    
    
    def get_short_info(self):
        '''code to return a string like “McDonald’s farm has cows, goats and sheeps”'''
        animals_list = []

        for animal in self.get_animal_types():
            if self.animals[animal] >= 2:            #if for that animal_type there are at least 2...
                animals_list.append(animal + 's')   #pass it plural
            else:
                animals_list.append(animal)
        
        if len(animals_list) == 1:
            animal_str = animals_list[0]
        else:
            animal_str = ", ".join(animals_list[:-1]) + " and " + animals_list[-1]

        return f'{self.name}\'s farm has {animal_str}.'
      


# Test the code - Invoke methods
macdonald = Farm("McDonald")   #instance creation

#macdonald.add_animal('cow', 5)
#macdonald.add_animal('sheep')
#macdonald.add_animal('sheep')
#macdonald.add_animal('goat', 12)

#Bonus: Expand The Farm
macdonald.add_animal(cow=5, sheep=2, goat=12)   

print(macdonald.get_info())  
# McDonald's farm

# cow    : 5
# sheep  : 2
# goat   : 12

#    E-I-E-I-0!

print(macdonald.get_animal_types()) 
# ['cow', 'goat', 'sheep']

print(macdonald.get_short_info())
#McDonald's farm has cows, goats and sheeps.