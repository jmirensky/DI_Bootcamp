#Exercise 6: Birthday and minutes
#Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.

from datetime import datetime

def minutes_lived  (birth_date_str):
    # Convert birthdate string to format date
    birthdate = datetime.strptime(birth_date_str, "%d-%m-%Y")
   
    # Current date and time
    now = datetime.now()

    # Calculate time difference
    time_lived = now - birthdate

    # Convert seconds to minutes
    minutes_lived =  time_lived.total_seconds()/60

    # Display result
    print(f'You have lived {int(minutes_lived):,} minutes.')


#To invoke the function --> in format "%d-%m-%Y"
minutes_lived ('24-10-1984')