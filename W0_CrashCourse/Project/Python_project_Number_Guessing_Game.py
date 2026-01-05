#Crash Course
#Python Project
#Exam 1 : Number Guessing Game 
'''Build a fun Number Guessing Game in Python! 🐍 The program picks a random number between 1-100, 
and you have 7 attempts to guess it. 
Get hints if you’re too high 📈 or too low 📉! Perfect for practicing loops 🔄, conditionals ❓, and user input ⌨️.'''


import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    # number of attempts allowed
    attempts = 7   

    print("\nWelcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100...")
    print(f"You have {attempts} attempts to guess it.\n")

    # Ask the player to enter a number, validating that it meets the requirements
    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"Try {attempt}, what is the number?: "))
                if 1 <= guess <= 100:
                    break
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Enter an integer number.")

        # Verificar la adivinanza
        if guess < number_to_guess:
            print("Too low.\n")
        elif guess > number_to_guess:
            print("Too high.\n")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempt} attempt(s).")
            return

    # If it doesn't guess correctly in the given attempts
    print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

# Run the game
number_guessing_game()







# --> #version sin limitar los intentos (de youtube)

#import random
#lowest = 1
#highest = 100
#answer = random.randint (lowest, highest)
#print(answer)

#guesses = 0
#is_running = True

#print('Welcome to the Number Guessing Game!')
#print(f"Select a number between {lowest} and {highest}")

#while is_running:
#    guess = input("Enter your guess: ")

#    if guess.isdigit():
#        guess = int(guess)
#        guesses += 1

#        if guess > highest or guess < lowest:
#            print(f"Your guess is out of range!")
#            print(f"Select a number between {lowest} and {highest}")
#        elif guess < answer:
#            print(f"Your guess is too low! Try again!")
#        elif guess > answer:
#            print(f"Your guess is too high! Try again!")
#        else:
#            print(f"Correct! The answer was {answer}!")
#            print(f"You guessed in {guesses} times!")
#           is_running = False

#    else:
#       print("invalid guess")
#        print(f"Select a number between {lowest} and {highest}")


