#Exercises Functions - Intermediate

#Exercise 1 : Return the Largest Number
#Write a function find_largest that takes a list of numbers and returns the largest number in the list.
def find_largest(numbers_list):
   number = numbers_list[0]
   for n in numbers_list:
        if number < n:
            number = n
   return number 
print(find_largest([1, 2, 3, 4]))  #4
print(find_largest([10, 20, 5]))   #20

#Exercise 2 : Check for Letter in Word
#Write a function check_letter that takes a word and a letter as parameters and checks if the letter is in the word.
#  It should return True if the letter is found and False if not.
def check_letter(word, letter):
    if letter in word:
        return True
    else:
        return False
print(check_letter("apple", "a"))  #True
print(check_letter("banana", "z")) #False

#Exercise 3 : Count to a Number
#Write a function count_to_number that takes a number as a parameter and prints all numbers from 1 to that number.
def count_to_number(number):
    for i in range(1, number+1):
        print(i)
count_to_number(9)  