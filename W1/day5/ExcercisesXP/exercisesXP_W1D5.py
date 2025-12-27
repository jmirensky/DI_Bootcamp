#Exercise 1: Converting Lists into Dictionaries
#Given two lists.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
#Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

my_dict = dict(zip(keys, values))   # → zip => creates pairs & dict => turn them into a dictionary.
print(my_dict)

#Exercise 2: Cinemax #2
#Write a program that calculates the total cost of movie tickets for a family based on their ages.
#Under 3 years old: Free
#3 to 12 years old: $10
#Over 12 years old: $15

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

cost_movie = 0

for i, f in family.items():
    if f < 3:
        price = 0
    elif 3 <= f <=12:
        price = 10
    else:
      price = 15  
   
    cost_movie += price
    print(f'For {i.capitalize()} the cost is ${price}')

print(f'Total cost for the family is ${cost_movie}')

#Bonus:  Allow the user to input family members’ names and ages, then calculate the total ticket cost.  [HARD]

dict_family = {}

while True:
    input_name = input('Enter family\'s member name ("done" to finish the purchase): ').lower()
   
    if input_name == 'done':
        break

    input_age = int(input(f'Enter {input_name}\'s age: '))
    dict_family[input_name] = input_age

cost_movie = 0
    
for name, age in dict_family.items():
    if age < 3:
        price = 0
    elif 3 <= age <=12:
        price = 10
    else:
      price = 15  
   
    cost_movie += price
    print(f'For {name.capitalize()} the cost is ${price}')

print(f'Total cost for the family is ${cost_movie}')


#Exercise 3: Zara
#Create and manipulate a dictionary that contains information about the Zara brand.

#Create a dictionary called brand with the provided data.
Zara = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color':   {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green']    
     }
}

print (type(Zara))
print(Zara)

#Change the value of number_stores to 2.
Zara['number_stores'] = 2
print(Zara)

#Print a sentence describing Zara’s clients using the type_of_clothes key.
sentence  =  'Zara\'s sectors are '
for sector in Zara['type_of_clothes']:
    sentence += sector + ", "
sentence = sentence[0:-2]  saco la coma y el espacio
sentence += '.'    agrego un punto
print(sentence)

#Add a new key country_creation with the value Spain.
Zara['country_creation'] = 'Spain'
print(Zara)

#Check if international_competitors exists and, if so, add “Desigual” to the list.
if 'international_competitors' in Zara.keys():
    Zara['international_competitors'].append('Desigual')
print(Zara['international_competitors'])

#Delete the creation_date key.
del Zara['creation_date']
print(Zara)

#Print the last item in international_competitors.
print(Zara['international_competitors'][-1])

#Print the major colors in the US.
print(Zara['major_color']['US'])

#Print the number of keys in the dictionary.
print(len(Zara))

#Print all keys of the dictionary.
print(Zara.keys())


#Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#1. Create a dictionary that maps characters to their indices:
dict_index_characters = {name: i for i, name in enumerate(users)}
print(dict_index_characters)

#2. Create a dictionary that maps indices to characters:
dict_characters_index = {i: name for i, name in enumerate(users)}
print(dict_characters_index)

#3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
dict_index_characters_sorted = {name: i for i, name in enumerate(sorted(users))}
print(dict_index_characters_sorted)