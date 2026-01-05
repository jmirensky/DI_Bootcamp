#Crash Course
#Python Iterables
#Exercise 1 : Lists

#1 - Given a list [1, 2, 3, 4], print out all the values in the list one by one.
list = [1, 2, 3, 4]
for num in list:
    print(num)

#2 - Given a list [1, 2, 3, 4], print out all the values in the list multiplied by 20.
list = [1, 2, 3, 4]
for num in list:
    print(num*20)

#3 - Given a list ["Elie", "Tim", "Matt"], return a new list with only the first letter of each name: ["E", "T", "M"].
names = ["Elie", "Tim", "Matt"]
initials = [ nam[0] for nam in names]  
print (initials)   #['E', 'T', 'M']

#4 - Given a list [1, 2, 3, 4, 5, 6], return a new list with all the even values: [2, 4, 6].
list = [1, 2, 3, 4, 5, 6]
new_list = [num for num in list if num % 2 == 0 ]   #list comprehension
print (new_list)   #[2, 4, 6]

#5 - Given two lists [1, 2, 3, 4] and [3, 4, 5, 6], return a new list that contains only the values present in both lists:
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
new_list = [num for num in list_a if num in list_b]   #list comprehension
print(new_list)   #[3, 4]

#6 - Given a list of words ["Elie", "Tim", "Matt"], return a new list with each word reversed and in lowercase: 
# ["eile", "mit", "ttam"].
names = ["Elie", "Tim", "Matt"]
result = [nam.lower()[::-1] for nam in names]
print(result)

#7 - Given two strings "first" and "third", return a new list of the letters that are present in both strings: ["i", "r", "t"].
f = 'first'
t = 'third'
list_letters = [ch for ch in f if ch in t]    #list comprehension
print(list_letters)  #['i', 'r', 't']

#8 - For all numbers between 1 and 100, return a list of the numbers that are divisible by 12: [12, 24, 36, 48, 60, 72, 84, 96].
result = [num for num in range (1, 101) if num % 12 == 0 ]   #list comprehension
print (result)   #[12, 24, 36, 48, 60, 72, 84, 96]

#9 - Given the string "amazing", return a list with all the vowels removed: ["m", "z", "n", "g"].
string = "amazing"
vowels = "aeiou"
result = [char for char in string if char not in vowels ] #list comprehension
print(result)  #['m', 'z', 'n', 'g']

#10 - Generate a list with the following value: [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
result = [[0, 1, 2]] * 3  
print(result)

#[with chatGPT]
#11 - Generate a list with the following structure:
result = [[i for i in range(10)] for _ in range(10)]
print(result)

#  _ → convención para indicar que no usamos la variable del bucle.  
#list comprehension anidada. Forma compacta de crear una lista de listas.

# [i for i in range(10)]     Crea [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for _ in range(10)         Repite esa lista 10 veces.
# El _ se usa porque no nos importa el valor, solo queremos repetir. 3

# Resultado final --> “grilla” de 10 filas por 10 columnas:
# ✔ Es una lista 2D (lista de listas)
# ✔ Muy usada para tableros, matrices, juegos, datos

