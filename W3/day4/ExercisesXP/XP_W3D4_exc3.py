#Exercise 3: String module
# Generate a random string of length 5 using the string module.

#Step 1
import string
import random

# Step 2: Create a string of all uppercase and lowercase letters
letters = string.ascii_letters


#print(letters)  --> contains all uppercase and lowercase letters
#  abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

# Step 3: Generate a random string of length 5
random_string = ""

for _ in range(5):
    random_char = random.choice(letters)    #selects a random letter
    random_string += random_char

print(random_string)