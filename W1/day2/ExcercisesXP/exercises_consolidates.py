#Exercise 1: Hello World
# Print the following output using one line of code:
#Hello world
#Hello world
#Hello world
#Hello world

print ("hello world\n" * 4)


#Exercise 2: Some Math
#Write code that calculates the result of:
# (99^3)*8 (meaning 99 to the power of 3, times 8).

result = (99**3)*8
print (result)


#Exercise 3: What is the output?
#Predictions
# 5 < 3 #False
# 3 == 3  #True
# 3 == "3"  #False
# "3" > 3 #Error   (not possible > or < for string)
# "Hello" == "hello"  #True --> is False, case sensitive

#Verification
print(5 < 3) #False
print(3 == 3)  #True
print(3 == "3")  #False
print("3" > 3) #Error  --> '>' not supported between instances of 'str' and 'int'
print("Hello" == "hello")  #True --> is False


#Exercise 4: Your computer brand
#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable, print a sentence that states the following:
#"I have a <computer_brand> computer."

#option1
computer_brand = 'Lenovo'
print(f"I have a {computer_brand} computer.")

#option2
computer_brand = input("Enter your computer brand: ")
print(f"I have a {computer_brand} computer.")


#Exercise 5: Your information
#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
#Have your code print the info message.
#Run your code.

name = 'Julieta'
age = 41
shoe_size = 36
info = f"My name is {name}, I am {age} years old, and I wear European size {shoe_size} shoes"
print (info)


#Exercise 6: A & B
#Create two variables, a and b. Each variable’s value should be a number.
#If a is bigger than b, have your code print "Hello World".
a = 20
b = 10
if a > b:
    print("Hello World")

print ('finished')


#Exercise 7: Odd or Even
#Write code that asks the user for a number and determines whether this number is odd or even.

number = int(input ('Please, give an integer number: '))

if number % 2 == 0:
    print (f"Your number is {number}, and is even")
else:
    print (f"Your number is {number}, and is odd")


#Exercise 8: What’s your name?
#Write code that asks the user for their name and determines whether or not you have the same name.
# Print out a funny message based on the outcome.

my_name = 'Julieta'
user_name = input ('What is your name? ').capitalize()

if user_name == my_name:
    print (f"What a coincidence! Your name is {user_name}, my name is {my_name} too!")
else:
    print (f"Your name is {user_name}, my name is {my_name}. We don't have the same name")


#Exercise 9: Tall enough to ride a roller coaster
#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.

height_cm = int(input ('Can you tell your height in centimeters? '))

if height_cm > 145:
    print (f"You are tall enough to ride the roller coaster")
else:
    print (f"You need to grow some more to ride the roller coaster")