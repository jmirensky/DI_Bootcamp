#Daily Challenge : Lists & Strings

#Challenge 1: Multiples of a Number
#1. Ask the user for two inputs:
    #A number (integer).
    #A length (integer).

number = int(input('Choose a number: '))   
lenght = int(input('Choose the lenght: ')) 


#2. Create a program that generates a list of multiples of the given number.
#3. The list should stop when it reaches the length specified by the user.

list_multiples = []
for l in range(1, lenght+1):
    list_multiples.append(number * l)
print (list_multiples)


#Challenge 2: Remove Consecutive Duplicate Letters

#1. Ask the user for a string.
#2. Write a program that processes the string to remove consecutive duplicate letters.
    #The new string should only contain unique consecutive letters.
    #For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
#3. The program should print the modified string.

#LO HICE CON CHATGTP, Hard excercise

word = input("Enter a word: ")

result = ""  #se actualiza a medida que avanzan las letras

for char in word:
    if result == "" or char != result[-1]:
        result += char

print(result)

#profe no lo supo resolver en clase, pero un compañero lo hizo asi y funciona.
word_user = input("Enter a word2: ") 
limpio = ""    #se actualiza a medida que avanzan las letras
check = ""

for letter in word_user:
    if letter != check:
        limpio += letter
        check = letter
print (limpio)