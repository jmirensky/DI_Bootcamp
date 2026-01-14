#Exercise 4: Family and Person Classes

#Step 1: Create the Person Class
class Person:
    '''Represents a person with a first name, age and last name'''
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ''
        
    def is_18(self):
        '''Return True if the person is 18 or older, False otherwise'''
        if self.age >= 18:
            return True
        else:
            return False


#Step 2: Create the Family Class
class Family:
    '''Represents a family with a last name and a list of members'''
    def __init__(self, last_name):
        '''Initialize a Family with a last name and empty list of members'''
        self.last_name = last_name
        self.members = []
        
    def born(self, first_name, age):
        '''Add a new member (born) to the family
        Args:
            first_name (str): First name of the new member.
            age (int): Age of the new member'''
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)

    def check_majority(self, first_name):
        '''Check if a member is 18 or older.
        Args:  --> first_name (str): first name of the member to check'''
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f'{first_name} is over 18, you can go out with your friends.')
                else:
                    print(f'{first_name} is under 18, you cannot go out with your friends.')
                return
        print(f'No member named {first_name} found in the family.')

    def family_presentation(self):
        '''Print the family's last name and each member's first name and age'''
        print('Members:')
        for member in self.members:
            print(f"{member.first_name}, {member.age} years old")


# ----- Testing  ------

my_family = Family('Levi')

# Add members
my_family.born('Gal', 20)
my_family.born('Noah', 15)
my_family.born('Aviv', 45)
my_family.born('Sara', 43)

# Check majority
my_family.check_majority("Noah")   # not allowed
my_family.check_majority("Gal")  # allowed
my_family.check_majority("Ruti")  # No member named Ruti found in the family.

# Show family info
my_family.family_presentation()