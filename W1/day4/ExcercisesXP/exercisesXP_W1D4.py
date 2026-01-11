#Exercise 1: Favorite Numbers
#Create a set called my_fav_numbers and populate it with your favorite numbers.
my_fav_numbers = {24, 31, 10, 1984, 2025}
print(my_fav_numbers)

#Add two new numbers to the set.
my_fav_numbers.add(15)
my_fav_numbers.add(3)

#Remove the last number you added to the set.
my_fav_numbers.remove(3)

#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
friend_fav_numbers = {3, 7, 12}

#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

#Note: Sets are unordered collections, so ensure no duplicate numbers are added.
print(f'my fav: {my_fav_numbers}')
print(f'friend\'s fav: {friend_fav_numbers}')
print(f'our favs: {our_fav_numbers}')


#Exercise 2: Tuple
#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
numbers =(1,2,3)
print(numbers)
#numbers.add(4)  #'tuple' object has no attribute 'append' or 'add'. INMUTABLE!
numbers = numbers + (4,5)
print(numbers)

#Exercise 3: List Manipulation
#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

#Remove "Banana" from the list.
basket.remove('Banana')

#Remove "Blueberries" from the list.
basket.remove('Blueberries')

#Add "Kiwi" to the end of the list.
basket.append('Kiwi')

#Add "Apples" to the beginning of the list.
basket.insert (0, 'Apples')  #uso insert pq ya tengo Apples en la posicion 0

#Count how many times "Apples" appear in the list.
count_Apples = basket.count('Apples')
print(f'Count apples: {count_Apples}')

#Empty the list.
basket.clear()

#Print the final state of the list.
print("final state: " , basket)   #[]


#Exercise 4: Floats
#What is a float? What’s the difference between a float and an integer?
#int (integer): whole numbers → 1, 2, 5
#float: numbers with a decimal part → 1.5, 2.0, 4.75

#Create a list containing the following sequence of mixed types: floats and integers:  1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
#Avoid hard-coding each number manually. Can you generate this sequence using a loop or another method?

numbers = [i / 2 for i in range(3, 11)]
print(numbers)

#otra forma (para mi, menos prolija)
result = []
for i in range(1,6):
    result.append(i)
    result.append(i+0.5)
print(result[1:-1])

#Exercise 5: For Loop
#Write a for loop to print all numbers from 1 to 20, inclusive.
for i in range (1, 21):
    print(i)

#Write another for loop that prints every number from 1 to 20 where the index is even.
my_list = (list(range(1,21)))
print(my_list)

for index, value in enumerate(my_list):     #enumerate: index and value at the same time
    if index % 2 == 0:
       print(index, value)


#Exercise 6: While Loop
#Use an input to ask the user to enter their name.
#Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
#hint: check for the method isdigit()
#if the input is incorrect, keep asking for the correct input until it is correct
#if the input is correct print “thank you” and break the loop

while True: 
    name = input('Enter your name: ').strip()  #strip quita espacios
    if name.isdigit() or len(name) <3:
        print("Invalid name. Try again.")
    else:
        print(f"Thank you, {name}")
        break


#Exercise 7: Favorite Fruits
#Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
fruits = input('Enter your favorite fruits, separated by spaces: ')

#Store these fruits in a list.
list_fruits = fruits.split()   #convert string in list, using spaces as separator
print (list_fruits)

#Ask the user to input the name of any fruit.
chosen_fruit = input("Enter the name of ANY fruit: ")

#If the fruit is in their list of favorite fruits, print:  "You chose one of your favorite fruits! Enjoy!"
#If not, print: "You chose a new fruit. I hope you enjoy it!"

if chosen_fruit in list_fruits:
     print("You chose one of your favorite fruits! Enjoy!")
else:
    print ("You chose a new fruit. I hope you enjoy it!")


#Exercise 8: Pizza Toppings  (Hard excercise for me)
#Write a loop that asks the user to enter pizza toppings one by one.
#Stop the loop when the user types . 'quit'
#For each topping entered, print:    "Adding [topping] to your pizza."
#After exiting the loop, print all the toppings and the total cost of the pizza.
#The base price is $10, and each topping adds $2.50.

toppings = []    # List to keep toppings

# Loop to ask toppings
while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")
    
    if topping.lower() == 'quit':
       break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")        

# Prices:
base_price = 10
topping_price = 2.5
total_price = base_price + topping_price * len(toppings)

# Show toppings y total price
print("Your pizza has the following toppings:")
for t in toppings:
    print(f"- {t}")

print(f"Total cost: ${total_price:.2f}") 
#:.2f en f-string formatea el total a 2 decimales
    # : → From here on, format
    # .2 → 2 decimal places
    # f → float ( decimal number)


# --- MANERA ALTERNATIVA
toppings = []    # List to keep toppings
price = 10

while True:
    topping = input("Enter a pizza topping (type 'q' to finish): ").lower()
    
    if topping == 'q':
        if toppings:  #implies that toppings is NOT empty
            print(f'Your toppings are {', '.join(toppings)} and the price is ${price:.2f}')
            break  #the person choose some toppings and decide to go out
        else:
            print(f'You didn\'t choose any topping, the price is ${price:.2f}')
            break    #the person decided NOT to choose any topping
    else:
        toppings.append(topping)
        price += 2.5
        print(f"Adding {topping} to your pizza.") #toppings are still being chosen



#Exercise 9: Cinemax Tickets  (Hard excercise for me)
#Ask for the age of each person in a family who wants to buy a movie ticket.
#Calculate the total cost based on the following rules:
    #Free for people under 3.
    #$10 for people aged 3 to 12.
    #$15 for anyone over 12.
#Print the total ticket cost.

total_cost = 0

while True:
    
    age_input = input('Enter the age of the family\'s member: (done to finish) ')
    
    if age_input.lower() == 'done':
        print ('Thank you, you can pay now')
        break
    
    age = int(age_input)
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost
    print(f"Total ticket cost: ${total_cost}")

#Bonus: 
#Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
#Write a program to:
#Ask for each person’s age.
#Remove anyone who isn’t allowed to watch.
#Print the final list of attendees.

#opcion 1 LO QUE PIDE EL EJERCICIO (exclusión de ages 16–21).
# estrictamente lo aplicaría para mayores de 21 años, los niños no deberian ir.

ages = []   # Lista vacía para guardar a todos los asistentes

while True:
    age = int(input("Enter your age (0 to finish): "))
    
    if age == 0:
        break
    
    ages.append(age)

allowed = []  # Lista vacía para guardar a todos los permitidos

for age in ages:
    if age < 16 or age >21:  #estrictamente lo aplicaría para mayores de 21 años, los niños no deberian ir.
        allowed.append(age)
    else:
        print(f"Age {age} is not allowed for this movie.")

not_allowed = [item for item in ages if item not in allowed]

print(f"Final list of attendees allowed: {allowed}")
print(f"Final list of attendees NOT allowed: {not_allowed}")  #not required by the excercise