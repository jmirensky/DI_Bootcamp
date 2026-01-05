#Crash Course
#Python Iterables
#Exercise 1 : Dictionary

#1. Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks
# like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).
list = [("name", "Elie"), ("job", "Instructor")]
dictionary = dict(list)
print(dictionary)


#2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"],
# return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
dict_states = dict(zip(list1, list2))
# zip Takes two or more iterables (lists, tuples) and matches them element by element, like a matchmaker
print(dict_states)


#3. Create a dictionary where the keys are vowels in the alphabet and the values are 0.
# Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
vowels = ['a', 'e', 'i', 'o', 'u']
dict_vowels = {v: 0 for v in vowels}  
print(dict_vowels)


#4. Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself.
numbers = [i for i in range(1, 27)]
print(numbers)
letters = [chr(num) for num in range(65,91)]
print(letters)
dict_alphabet = dict(zip(numbers, letters))
print (dict_alphabet)

#Super Bonus:  #Given the string "awesome sauce", return a dictionary where the keys are vowels,
# and the values are the count of each vowel in the string.
# Your dictionary should look like this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.
#------ >[with ChatGP]

string = "awesome sauce"
vowels = "aeiou"
d = {v: 0 for v in vowels}

for char in string:
    if char in vowels:
        d[char] += 1   

print(d)