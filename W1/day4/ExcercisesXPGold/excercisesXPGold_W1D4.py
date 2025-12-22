#Exercise 1: Concatenate lists
#Write code that concatenates two lists together without using the + sign.
list1 = ['rishon', 'sheni', 'shlishi', 'revi\'i']
list2 = ['jamishi', 'shishi', 'shabat']
list1.extend(list2)
print(f"shavua: {list1}")


#Exercise 2: Range of numbers
#Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range (1500, 2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)  

#Exercise 3: Check the index
#Using names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
#Example: if input is 'Cortana', we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input ('what\'s you name? ').capitalize()
if user_name in names:
    print (f"1° ocurrence of {user_name} is at index: {names.index(user_name)}")
else:
    print (f"{user_name} not found in the list")

#Exercise 4: Greatest Number
#Ask the user for 3 numbers and print the greatest number.

#version1: con limitacion de intentos, forma sofisticada
numbers = []
tries = 1
max_tries = 3                       

while tries <= max_tries:
    number = int(input('Input a number: '))
    numbers.append(number)
    tries += 1

print(numbers)
max_number = max(numbers)
print(f'The greatest number is: {max_number}')

#version2: simple pero efectiva
n1 = int(input("Input the 1st number: "))
n2 = int(input("Input the 2nd number: "))
n3 = int(input("Input the 3rd number: "))

maximo = max(n1, n2, n3)
print("The greatest number is:", maximo)

#Exercise 5: The Alphabet
#Create a string of all the letters in the alphabet
#Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

for letter in alphabet:
    if letter in vowels:
        print(f'{letter} is a vowel')
    else:
         print(f'{letter} is a consonant')

#Exercise 6: Words and letters
#Ask a user for 7 words, store them in a list named words.
#Ask the user for a single character, store it in a variable called letter.
#Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
#If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.
words = []
tries = 1
max_tries = 7                       

# Ask for 7 words
while tries <= max_tries:
    word = input('Input a word: ')
    words.append(word)
    tries += 1

letter = input('Input just a single character: ')   # Ask for a single character

# Loop through the words
for word in words:
    index = word.find(letter)   #busca el index de acuerdo a una descriptiva

    if index != -1:      #-1 es que NO lo encontró
        print(f'The letter {letter} appears in word {word} at position {index} (for first time)')
    else:
        print(f'The letter {letter} does not appear in word {word}')


#Exercise 8 : List and Tuple
#Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.

numbers = input('Enter some comma-separated numbers: ')   #sequence of comma-separated numbers
numbers_list = numbers.split(',')   #Generate a list using split as separator and returning list
numbers_tupple = tuple(numbers_list)

print(numbers_list)
print(numbers_tupple)


#Exercise 9 : Random number
#Ask the user to input a number from 1 to 9 (including).
#Get a random number between 1 and 9. Hint: random module.
#If the user guesses the correct number print a message that says Winner.
#If the user guesses the wrong number print a message that says better luck next time.

import random

guess = int(input("Guess a number from 1 to 9: "))
random_number = random.randint(1,9)

print(f'the number to guess was {random_number}')

if guess == random_number:
    print('Winner!')
else:
   print('better luck next time')   


#Bonus: use a loop that allows the user to keep guessing until they want to quit.

import random

while True:
    guess = input("Guess a number from 1 to 9 (or 'q' to stop playing) ")

    if guess.lower() == 'q':
        print ('Thanks for playing')
        break

    guess = int(guess)
    random_number = random.randint(1,9)
    
    print(f'the number to guess was {random_number}')
    if guess == random_number:
        print('Winner!')
    else:
        print('better luck next time')  

 
#Bonus 2: on exiting the loop tally up and display total games won and lost.

import random
wins = 0
losses = 0
total = wins + losses

while True:
    guess = input("Guess a number from 1 to 9 (or 'q' to stop playing) ")

    if guess.lower() == 'q':
        print ('Thanks for playing')
        break

    guess = int(guess)
    random_number = random.randint(1,9)
    
    print(f'the number to guess was {random_number}')
    if guess == random_number:
        print('Winner!')
        wins +=1
    else:
        print('better luck next time') 
        losses += 1

print(f"Games won: {wins}")
print(f"Games lost: {losses}")