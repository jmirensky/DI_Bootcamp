#Tall enough to ride a roller coaster
#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.

height_cm = int(input ('Can you tell your height in centimeters? '))

if height_cm > 145:
    print (f"You are tall enough to ride the roller coaster")
else:
    print (f"You need to grow some more to ride the roller coaster")