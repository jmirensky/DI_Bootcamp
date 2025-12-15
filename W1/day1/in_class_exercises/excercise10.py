#Ask the user for a number between 1 and 100
#If the number is a divisible by three, print Fizz
#If the number is a divisible by five, print Buzz.
#If the number is a divisible by both three and five, print FizzBuzz instead.

number = int(input ("Give me a number between 0 and 100: "))
if number % 3 == 0 and number % 5 == 0:    #o poner en if number % 15 == 0:
     print ("FizzBuzz")     
elif number % 3 == 0:
    print ("Fizz")
elif number % 5 == 0:
    print ("Buzz")
print ("finished")