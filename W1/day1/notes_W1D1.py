
#W1 D1      14Dic

#str
# string --> text, in between '' or "", sequence of char.  #Inmutable
food = 'pizza'
print (f"I like {food}")
print(type(food))
print ('5' + '2')  #52    + une caracteres SIN ESPACIO

print('it\'s complicated')  #entre barras simples poner alt+92 {barra invertida} y el apostrofe del inglés
#it's complicated
      
#string methods = upper(), lower(), len(), replace()

#long_string = van entre triple comillas. Son para textos largos.
long_string = '''
WOW
O O
---
'''
print(long_string)


#numbers = int, float
 
#int
players = 3
print (f"there are {players} players online")
print(type(players))

#float
price=3.95
print (f"the price is usd {price}")
print(type(price))

#boolean
online = True
print (f"the page is online?: {online}")
print(type(online))

#NoneType: nothing, None

#EXERCISE
description = "strings are..."
print(description.upper()) #make it all uper case
print(description.replace("are", "is") )   #replace the word "are" to "is"
print(description.split()[0])   #print just the word "strings"   --> Convierte un string en iterable (lista)
print(description[:7])

#números = hay int y hay float. Aplican operaciones matemáticas + - * / resto
#resto --> x % y (resto of x/y)  
num = 12 
if num % 2 == 0:     #saber si un número es par o impar
    print("par")
else:
    print("impar")


#EXERCISE
my_age = 41
future_age = my_age + 123879
print(f"my future_age is {future_age} years")

#castear = type convertion = pasar de int a str y viceversa; de int a float y viceversa
print(int('12') * 2)
expresion = str(30)
print(type(expresion))
print(float(5))

#EXERCISE
bank_balance = '33000'
print(type(bank_balance))   #es string
bank_balance2 = int(bank_balance)   #cast a int
print(type(bank_balance2))

phone_number = 532287514
print(type(phone_number))  #es int
phone_number2 = str(phone_number)   #cast a str
print(type(phone_number2))

print("Hello "*3)    #Hello Hello Hello
print (("Hello" + "World" + " ")*3)  #HelloWorld HelloWorld HelloWorld
print("My favorite number is " + str(8))
#print("My favorite number is " + (8))  #error, no se puede concatenar str con int

#EXERCISE
first_name = 'Lionel'
last_name = 'Messi'
print(f"He is {first_name} {last_name}")


#Caracteres especiales
print("Hello world\nMy name is Juli")   # \n define linea nueva (punto aparte, un enter)
print('I love Pyhton\n' * 3) 
print("Hello world My name is\tJuli")   # \t define un espacio TAB
print("I love Pyhton\t" * 3)   

print ('hello' == 'hello')   # ==  compara si 2 valores u operandos son iguales (números o strings)
print ('hello' != 'hello')   # !=  compara si 2 valores u operandos son distintos

#swap, creo una variable temporal
x = 1
y = 2
print(x, y)   #1 2
temp = y
y = x
x = temp
print(x, y)  #2 1


#Some operators can be used in plain English form:  #is iqual to ==    #is not equal to !=   #and    #or
print ('me' is 'me')
print ('me' is not 'you')
print ('b' != 'a' and 'c' is 'c')

#Regla de oro en Python:   cero y vacío → False; lo demás → True.

#bajo bool son False: falso, 0, None, vacío (string, list, tuple, diccionario, set)
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool([]))  #Lista vacía
print(bool(())) #Tuple vacía
print(bool({})) #Diccionario vacío
print(bool(set()))  #Set vacío

#bajo bool son True: True, 1, número diferente a 0, no vacío (string, list, tuple, diccionario, set)
print(bool(True))
print(bool(1))
print(bool(-5))  # is not True en estricto rigor, es truthy
print(bool("hola"))
print(bool([1,2,3]))
print(bool((1,2,3)))
print(bool({'a':1,'b':2}))
print(bool({1,3,5}))

#EXERCISE
x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"
print ((x < y) and (y > z))   #1. Check if x is less than y and y is greater than z
print (word1 != word2)        #2. Verify if word1 is not equal to word2
print (word1 is not word2)
print(bool(z))          #3. Use bool() to check the boolean value of z and word1
print(bool(word1))

#incremento de variables
my_number = 5
#my_number = my_number + 1  # Increment it
#print (my_number)   #6

#operador de asignación compuesta o aumentada
#  +=   # suma
#  -=   # resta
#  *=   # multiplica
#  /=   # divide
#  %=   # resto
my_number += 5   #  es lo mismo que my_number = my_number + 5
print (my_number)   #10

name = "Frank"
age = 65
print("Hello, {}. You are {}.".format(name, age))   # str.format() Method (Legacy)
print(f"Hello, {name}. You are {age}.")    #f-strings

#EXERCISE
name = "Alice"
age = 30
city = "New York"
print (f"Hello, {name}! You are {age} years old and live in {city}.")
print ("Hello, {}! You are {} years old and live in {}.".format(name, age, city))  #str.format()

#EXERCISE
age = input("What is your age? ")
age = int(age)
years_future = 100 - age
print(f"You will turn 100 in {years_future} years, in {2025+years_future}.")

frase = "hola mundo "
print(frase*2)

my_name = input ("What is my name? ")
print (my_name)

#input x default is string, debo convertirlo a int p/ realizar operaciones matemáticas
my_numb = int(input('Give me a number: ')) 
numb_x2 = my_numb * 2
print (f"The number 2 times is {numb_x2}")

#Exercise - Password checker
user_name = input ('What\'s your username? ')
password= input ('What\'s your password? ')
password_lenght = len(password)
hidden_password = '*' * password_lenght
#print (f"{user_name}, your password, {password}, has {len(password)} letters long")
print (f"{user_name}, your password, {hidden_password}, has {password_lenght} letters long")  #sol definitiva


#EXPLICACION CONDICIONALES Y IF STATEMENTS

print('a' > 'A') #is True xq según código Unicode (antes ASCII): 'A' = 65  y 'a' = 97. Queda 97 > 65

#solo if = solo si la condicion se cumple
a = 33
b = 200
if a > b:
    print(f"{a} is greater than {b}")
    print(a, 'is greater than', b)
print("Finished")


#if + else
a = 33
b = 200
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is not greather than {b}")
print("Finished")

running =False
if running:
    print ("game running ok")
else:
   print ("game is over")

response = input( "Would you like to eat? (y/n): ")
if response == "y":
    print("Have some food, enjoy!")
else:
    print("ok, no food for you")

name = input("What is your name? ")
if name == '':
    print("Missing name!")
else:
    print(f"Welcome {name}!")

for_sale = True
if for_sale:
    print ("Item for sale")
else:
    print ("Item NOT for sale")

online = False
if online:
    print ("user online")
else:
    print ("user offline")


#if + elif
a = 33
b = 200
if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
print("Finished")


#if + elif + else
a = 33
b = 200
if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{b} is greater than {a}")
print("Finished")


age = int(input("Enter your age: "))
if age >=100:
    print("You are too old to sign up")
elif age >=18:
    print("You are now signed up!")
elif age < 0:
    print("You have not be born yet")
else:
    print ("You must be +18 years old")