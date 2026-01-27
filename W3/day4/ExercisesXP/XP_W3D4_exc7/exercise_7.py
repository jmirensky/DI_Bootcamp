#Exercise 7: Faker Module
#Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.

# Previous steps in the terminal:

# Create a virtual environment pointed to the folder's proyect     python -m venv venv
# Activate the virtual environment        venv\Scripts\activate
# Install faker module        pip install faker

# Create the Python file  (exercise_7.py)

# Step 1 & 2: Import the Faker module
from faker import Faker

# Create a Faker instance
fake = Faker()

#Step 3: Create an empty list of users
users = []

#Step 4: Create a function to add users
def add_users(number_of_users):
    """
    Generates fake users and stores them in a list of dictionaries.
    """
    for _ in range(number_of_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)


#Step 5: Call the function and print the users list
add_users(3)
print(users)

#[{'name': 'Tanya Coleman', 'address': '1075 Berger Radial\nWest Terrance, AZ 55937', 'language_code': 'hu'},
# {'name': 'Lisa Daniels', 'address': '96586 Gabriel Falls\nGomezland, NV 82453', 'language_code': 'iu'}, 
# {'name': 'Jessica Estrada', 'address': '36958 Kelly Hills\nHarperville, MA 40851', 'language_code': 'tg'}]