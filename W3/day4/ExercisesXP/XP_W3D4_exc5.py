#Exercise 5: Amount of time left until January 1st
#Goal: Create a function that displays the amount of time left until January 1st.

# Step 1: Import the datetime module
from datetime import datetime

def time_until_january_first():
    
    # Step 2: Get the current date and time 
    now = datetime.now()
  
    # Step 3: Create a datetime object for January 1st of the next year
    next_year = now.year + 1
    january_first = datetime(next_year, 1, 1)

    # Step 4: Calculate the time difference
    # Time difference
    time_left = january_first - now

    #  Step 5: Display the time difference
    print(f'Time left until January 1st: {time_left}')

# call the function
time_until_january_first()