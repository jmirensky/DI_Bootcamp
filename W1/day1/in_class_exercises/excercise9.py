#1. ask the user to enter his/her name
#2. use the len() function to check the lenght of the name. 
# if it is less than 5 letter print('You have a short name :)')

name = input ("What is your name?: ")
print(name)
if len(name) < 5:
    print ("you have a short name")