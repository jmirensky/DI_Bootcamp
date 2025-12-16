#Write code that asks the user for their name and determines whether or not you have the same name.
# Print out a funny message based on the outcome.

my_name = 'Julieta'
user_name = input ('What is your name? ').capitalize()

if user_name == my_name:
    print (f"What a coincidence! Your name is {user_name}, my name is {my_name} too!")
else:
    print (f"Your name is {user_name}, my name is {my_name}. We don't have the same name")