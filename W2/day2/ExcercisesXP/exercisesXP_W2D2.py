
#Exercise 1: What Are You Learning?
#Goal: Create a function that displays a message about what you’re learning.

#Step 1: Define a Function
def display_message():

#Step 2: Print a Message
    print(f'I am learning about functions in Python.')

#Step 3: Call the Function
display_message()

#output  --> I am learning about functions in Python.


#Exercise 2: What’s Your Favorite Book?
#Goal: Create a function that displays a message about a favorite book.

#Step 1: Define a Function with a Parameter
def favorite_book(title):

#Step 2: Print a Message with the Title
    print(f'One of my favorite books is {title}')

#Step 3: Call the Function with an Argument
favorite_book('The Little Prince')

#output --> One of my favorite books is The Little Prince

#Exercise 3: Some Geography
#Goal: Create a function that describes a city and its country.

#Step 1: Define a Function with Parameters 
def describe_city(city, country='Unknown'):

#Step 2: Print a Message
    print(f'{city} is in {country}')

#Step 3: Call the Function
describe_city('Reykjavik', 'Iceland')
describe_city('Paris')

#output --> 
    #Reykjavik is in Iceland
    #Paris is in Unknown


#Exercise 4: Random
#Goal: Create a function that generates random numbers and compares them.

#Step 1: Import the random Module
import random

#Step 2: Define a Function with a Parameter
def random_game(user_number):
   
#Step 3: Generate a Random Number
    random_number = random.randint(1, 100)

#Step 4: Compare the Numbers
    if user_number == random_number:
        print('Success!')
    else:
        print(f'Fail! Your number: {user_number}, Random number: {random_number}')

#Step 5: Call the function with a number between 1 and 100.
random_game(45)


#Exercise 5: Let’s Create Some Personalized Shirts!
#Goal: Create a function to describe a shirt’s size and message, with default values.

#Step 1: Define a Function with Parameters
#Step 4: Modify the Function with Default Values
def make_shirt(size='Large', text='I love Python'):

#Step 2: Print a Summary Message
    print(f'The size of the shirt is {size} and the text is {text}.')

#Step 3: Call the Function
#Step 5: Call the Function with Default and Custom Values
make_shirt()
make_shirt('medium')
make_shirt('small', 'I love TLV')

#output --> 
    #The size of the shirt is Large and the text is I love Python.
    #The size of the shirt is medium and the text is I love Python.
    #The size of the shirt is small and the text is I love TLV.


#Exercise 6: Magicians…     [With ChatGTP]
#Goal: Modify a list of magician names and display them in different ways.

#Step 1: Create a List of Magician Names
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']   #original list

#magician_names2 --> internal name that the function uses to refer to magician_names. --> magician_names2 = magician_names
#Do not exist out of the function

#Step 2: Create a Function to Display Magicians
def show_magicians(magician_names2):
    for magician in magician_names2:
        print(magician)

#Step 3: Create a Function to Modify the List         
def make_great(magician_names2):
    for i in range(len(magician_names2)):
        magician_names2[i] = magician_names2[i] + " the Great "    #Does not create a new list: it changes the existing one, by accesing the indexes
 
#Step 4: Call the Functions
#First modify, then show.
make_great(magician_names)    
show_magicians(magician_names)

#output --> 
    #Harry Houdini the Great
    #David Blaine the Great
    #Criss Angel the Great


#Exercise 7: Temperature Advice
#Goal: Generate a random temperature and provide advice based on the temperature range.
import random

#Step 1: Create the get_random_temp() Function
#Step 4: Floating-Point Temperatures (Bonus)
def get_random_temp():
    return random.uniform(-10, 40)

#Step 2: Create the main() Function
#Step 3: Provide Temperature-Based Advice
def main():
    temp = get_random_temp()
    print(f'The temperature right now is {temp:.1f} degrees Celsius.')     #:.1f 1 decimal point
    
    if temp < 0:
        print('Brrr, that’s freezing! Wear some extra layers today.')
    elif temp < 16:
        print('Quite chilly! Don\'t forget your coat.')
    elif temp < 23:
        print('Nice weather.')
    elif temp <= 32:
        print('A bit warm, stay hydrated.')
    else:
        print('It’s really hot! Stay cool.')
main()

#Step 5: Month-Based Seasons (Bonus)
import random

def get_random_temp(season):
    if season == 'winter':
        return random.uniform(-10, 16)
    elif season == 'spring':
        return random.uniform(15, 26)
    elif season == 'summer':
        return random.uniform(23, 40)
    elif season == 'autumn':
        return random.uniform(14, 21)
    
def main():
    while True:
        month = int(input("Enter a month (1-12): "))
    
        if month in (12, 1, 2):
            season = 'winter'
            break
        elif month in (3, 4, 5):
            season = 'spring'
            break
        elif month in (6, 7, 8):
            season = 'summer'
            break
        elif month in (9, 10, 11):
            season = 'autumn'
            break
        else:
            print("Invalid month. Try again")
        
        
    temp = get_random_temp(season)
    
    print(f'We are in {season.capitalize()}')
    print(f'The temperature right now is {temp:.1f} degrees Celsius.')     #:.1f 1 decimal point
              
    if temp < 0:
        print('Brrr, that’s freezing! Wear some extra layers today.')
    elif temp < 16:
        print('Quite chilly! Don\'t forget your coat.')
    elif temp < 23:
        print('Nice weather.')
    elif temp < 32:
        print('A bit warm, stay hydrated.')
    else:
        print('It’s really hot! Stay cool.')
main()