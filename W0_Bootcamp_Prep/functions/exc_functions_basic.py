#Exercises Functions - Basics

#Exercise 1 : Add Two Numbers
#Write a function add_two_numbers that takes two numbers as parameters and returns their sum
def add_two_number(a, b):
    return a+b
print(add_two_number(3,5))   #3 + 5 = 8
print(add_two_number(10,20))   #10 + 20 = 30


#Exercise 2 : Print a Greeting
#Write a function greet that takes one parameter, a person’s name, and prints a greeting message like “Hello, [name]!”.
def greet(name):
    print (f'Hello {name}!')
greet('Alice')
greet('Bob')

#Exercise 3 : Check if Number is Even or Odd
#Write a function check_even_odd that takes one number and prints “Even” if the number is even, and “Odd” if the number is odd.
def check_even_odd(number):
    if number %2 == 0:
        return f'{number} is even'
    else:
        return f'{number} is odd'
print(check_even_odd(124))

#Exercise 4 : Sum of Numbers in a List
#Write a function sum_list that takes a list of numbers as a parameter and returns the sum of all numbers in the list.
def sum_list(list_num):
    result = 0
    for num in list_num:
        result += num
    return result
print(sum_list([1, 2, 3, 4]))  # Output: 10
print(sum_list([5, 5, 5]))     # Output: 15


#Exercise 5 : Print Days of the Week
#Write a function print_days that prints the days of the week (Sunday, Monday, Tuesday, etc.) using a loop.
def print_days():   
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for day in week:
        print(day)
print_days() 


#Exercise 6 : Check if Number is Positive, Negative, or Zero
#Write a function check_sign that takes a number and prints whether the number is positive, negative, or zero.
def check_sign(number):     
    if number > 0:
        return f'{number} is positive'
    elif number == 0:
        return f'{number} is zero'
    else:
        return f'{number} is negative'
print(check_sign(1589))
print(check_sign(-0.57))
print(check_sign(0))

#Exercise 7 : Repeat a Word
#Write a function repeat_word that takes a word and a number as parameters and prints the word that many times.
def repeat_word(word, times):
    print((word + "\n") * times)
repeat_word("hello", 3)  
repeat_word("goodbye", 2)  