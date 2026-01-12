#Mini-Project #2 - Hangman

''' Instructions
The computer choose a random word and mark stars for each letter of each word.
Then the player will guess a letter.
If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
The player can’t guess the same letter twice.'''


#Function 1 – Hide the word
'''Converts the chosen word into a string of *.
     Spaces are preserved so phrases stay readable'''

def hide_word(word):
    hidden = ""
    # We go through each character of the word
    for char in word:
        if char == " ":
            hidden += " "   # keep spaces as they are
        else:
            hidden += "*"   # hide letters with an asterisk
    return hidden


# Function 2 – Update the hidden word
'''Receives:
 - the original word
 - the current state (with * and letters)
 - the guessed letter
 Returns the updated hidden word'''

def update_hidden_word(word, hidden_word, letter):
    new_hidden = ""
    
    # We loop through the indexes of the word
    for i in range(len(word)):
        # If the guessed letter is at this position, we reveal it
        if word[i] == letter:
            new_hidden += letter
        else:
            # Otherwise, keep what was already there
            new_hidden += hidden_word[i]

    return new_hidden


# Main program, consider:
''' hidden_word
    errors
    guessed_letters (list)
    max_errors = 6 --> 6 body parts'''

# The computer chooses a random word from the list
import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
              'credit card', 'rush', 'south']
word = random.choice(wordslist) 

# Initial game state
hidden_word = hide_word(word)      # hidden version of the word, resulto of function 1
errors = 0                         # number of wrong guesses
guessed_letters = []               # letters already guessed


# Main game loop --> the logic is:
'''while not winning and not losing: ask for a letter
    if It was already used → notice 
    if it is in the word → update 
    if not → add error'''

# The game continues while the player has less than 6 errors and there are still hidden letters
while errors < 6 and "*" in hidden_word:
    print(hidden_word)
    letter = input("Guess a letter: ").lower()  #ask for a letter

    # Check if the letter was already guessed
    if letter in guessed_letters:                   #if It was already used → notice 
        print("You already guessed that letter.")    
        continue

    # Store the guessed letter
    guessed_letters.append(letter)

    # Check if the letter is in the word  → update 
    if letter in word:
        hidden_word = update_hidden_word(word, hidden_word, letter)    # hidden version of the word, resulto of function 2
    else:              #if not → add error
        errors += 1
        print(f"Wrong guess. Errors: {errors}/6")


# Final condition (win or lose): If there are no '*' left, the player won
if "*" not in hidden_word:
    print("You win!")
    print("The word was:", word)
else:
    print("You lose!")
    print("The word was:", word)