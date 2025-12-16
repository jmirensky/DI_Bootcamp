#Write code that asks the user for a number and determines whether this number is odd or even.

number = int(input ('Please, give an integer number: '))

if number % 2 == 0:
    print (f"Your number is {number}, and is even")
else:
    print (f"Your number is {number}, and is odd")
