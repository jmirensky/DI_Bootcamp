
#Exercise
#find the value 20 in the list
list1 = [5, 10, 15, 20, 25, 50, 20]
busco_al20= (list1.index(20))  #.index para buscar x descriptiva
print(busco_al20)

#if is present, replace it with 200. Only update the first occurrence of a value
list1[3]= 200  #primero lo reemplazo
print(list1)    #[5, 10, 15, 200, 25, 50, 20]


#Exercise
#Unpack the following tuple into 4 variables
a_tuple = (10, 20, 30, 40)
a,b,c,d = a_tuple
print(a) #  10
print(b) #  20
print(c) #  30
print(d) #  40

#Exercise
#Accept a number from the user and print its multiplication table
user_number = int (input("give a number: "))

for number in range(11):
    print(f"{user_number} x {number} = {user_number * number}")


#EXCERCISE 
#Print the numbers from 1 to 10 using while loop
current_number = 1 
while current_number <= 10:    
    print(current_number)   
    current_number += 1
