
#6 You have a friend named Alice, and you want to send her a message
name = "Alice"
age = 30
city = "New York"
print (f"Hello, {name}! You are {age} years old and live in {city}.")  #f-strings
print ("Hello, {}! You are {} years old and live in {}.".format(name, age, city))  #str.format()

#7 Ask the user for their age using the function and store it in a variable age.input()
# Convert the inputted age into an integer and calculate the number of years until 
# they turn 100.
# Display a message: "You will turn 100 in X years", where X is the number of years calculated. 
age = input("What is your age? ")
age = int(age)
years_future = 100 - age
print(f"You will turn 100 in {years_future} years")