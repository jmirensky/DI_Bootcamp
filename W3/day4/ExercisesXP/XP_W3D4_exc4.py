#Exercise 4: Current Date
#Goal: Create a function that displays the current date.

# Step 1: import the datetime module
import datetime  

def show_current_date():

    # Step 2: get the current date
    today = datetime.date.today()

    # Step 3: display the date
    print(today)

# call the function
show_current_date()