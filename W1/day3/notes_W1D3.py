#W1 D2      15Dic  SELF LEARNING

#W1 D3      16Dic

#TODOS son data types, según un determinado formato o estructura.
#   números: int float complex  / texto / bool  / NoneType =  PRIMITIVES
#   colecciones: list tuple set dict   = NO primitivos

#data types - guardo un solo valor
#números = int, float
#string = almacena caracteres         sequences
#bol = V/F

# data types & data structure (en simultáneo) - complex types
# se organizan varios datos en conjunto
#es un container
#List  []  → mutable, ordenada, ej  lista de frutas, de precios      sequences
#Tuple () → inmutable, ordenada                                      sequences
#Set  → mutable, no ordenada, sin duplicados    no tienen idea del orden de sus elementos
#Dictionary  {}  → pares clave–valor            no tienen idea del orden de sus elementos

#list - tuple - string = son secuences, x tanto son indexables = posicion  --> sequence_name[index_num].

#List
#versátil
#pueden albergar cualquier objeto: int, str, bool, incluido otras listas.
#Permite duplicados.
#elementos mutables (modificables), se pueden reasignar, eliminar, insertar nuevos elementos.
#aplicar rangos  range_index
#some methods: append, remove, insert, count, clear, split, join

list_fruits =["apple", "banana", "cherry", "kiwi", "strawberry", "pineapple", "mango"]
selected_fruit = list_fruits[0]  #la primera
selected_fruit = list_fruits[-1]  #la última
quant_fruits = len(list_fruits)   #cantidad, extension
sorted_fruits = sorted(list_fruits)  #orden alfabetico/creciente, no cambia la lista original, es un nuevo objeto
print(sorted_fruits)
sorted_fruits2 = sorted(list_fruits, reverse=True)  #orden decreciente, no cambia la lista original, es un nuevo objeto
print(sorted_fruits2)
list_fruits.sort()  #sobre el mismo objeto
print(list_fruits)

#Built-in methods
list_fruits.append('orange')  #agrego un elemento al final
list_fruits.remove('kiwi')   #elimino un elemento en particular x descriptiva
list_fruits.pop(-1)  #elimino un elemento en particular x posición
print(list_fruits[0:4])  #las primeras 4 = range_index
print(list_fruits.index('mango'))  #busca la posicion donde ocurre el elemento x 1°vez
list_fruits[5] = 'pear'    #modifico un elemento que ya existe
print(list_fruits[0][0])   #a de apple
print(list_fruits)

members = input('Enter family member\'s names separated by comma: ').split(',')
print(members)  #['ana', ' luis', ' juan']

text ='murcielago'  #string es iterable, aplicandole lista llego a
chars = list(text)
print(chars)   # ['m', 'u', 'r', 'c', 'i', 'e', 'l', 'a', 'g', 'o']

students = ["John", "Peter", "Vicky"]
x = " - ".join(students)
print(x)    # John - Peter - Vicky

#una lista con 3 listas adentro
grid = [ [1 , 2 , 3 ],
         [4 , 5 , 6 ],
         [7 , 8 , 9 ]
                      ]
print(grid[0][0])   #1 #la diagonal
print(grid[1][1])   #5
print(grid[2][2])   #9

prices =[34,49,90]   #funciones matématicas
sum_prices = sum(prices)
print(sum_prices)
sorted_prices = sorted(prices)
print(sorted_prices)

my_name = "Jack"
my_age = 27
hello = "Hello World"
my_list = [my_name, my_age, hello]   #lista de strings e Int
print(my_list)
print(my_list[0])  #Jack
print(my_list[2][0:5],my_list[2])   #Hello Hello World 
                            #--> del 3° elemento, las primeras 5 posiciones seguido del 3° elemento

#acceder al item de acuerdo a su index_number

my_list = ['car',126,42]
print(my_list[0])   #star counting in 0
print(my_list[-1])  #star counting from the back

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(my_list[3:7])  # result [40, 50, 60, 70]  = range_index

my_hobbies = ["Eat", "Sleep", "Code"]
print(my_hobbies[2])  #code   

#Actualizaciones

my_hobbies[1] = "Meditate"  # modificar un elemento x posicion
print(my_hobbies)

my_hobbies.append("Baseball")  #agregar un elemento al final
print(my_hobbies)

my_hobbies.remove("Meditate")  #eliminar un elemento específico x descriptiva
print(my_hobbies)

my_hobbies.pop(-1)  #eliminar un elemento específico x posición
print(my_hobbies)

#sumar dos listas = uno una atras de la otra con +
new_hobbies = ['paint', 'gym']
print(my_hobbies + new_hobbies)

#Buil-in functions
prices = [3,18,25,12]
print(len(prices))  #cantidad de items
print(sorted(prices)) 
prices.append(15)  #agrego 1 elmento al final
prices.remove(18) #elimino un elemento en particular x descriptiva, su 1° ocurrencia
price_25 = prices.pop(1)  #elimino un elemento en particular x posición, y lo puedo guardar como objeto (no desaparece)
prices.insert(3,45)  #agrego 1 elemento en la pposicion 3
prices.extend([100,105,39]) #extiendo la lista agregando los elementos de otra lista
prices2 = [52, 4]
print(prices+prices2)   #extiendo la lista agregando el nombre de otra lista
print(prices)
print(price_25)
print(sum(prices))  #funciones matemáticas básicas
print(min(prices))
print(max(prices))
average = sum(prices) / len(prices)  
print(average)

#Exercise:
#find the value 20 in the list
list1 = [5, 10, 15, 20, 25, 50, 20]
busco_al20= (list1.index(20))  #.index para buscar x descriptiva
print(busco_al20)

#if is present, replace it with 200. Only update the first occurrence of a value
list1[3]= 200  #primero lo reemplazo
print(list1)    #[5, 10, 15, 200, 25, 50, 20]

# ---------

#Tuple () es secuencial, admite indexación (encontrar posición, órden) y duplicados;
#pero ES INMUTABLE = no se puede editar (agregar/quitar) una vez creada. x eso es Más rápida y seguro

my_tuple = (1+3, 2.7, 'Thursday')
print (my_tuple)
print (my_tuple[-2])   #2.7
#my_tuple[1] = 5  #error! #NO puedo modificar una vez creada  'tuple' object does not support item assignment

my_tuple2 = (5,6,7, 'hello')
a,b,c,d = my_tuple2   #unpack, descomprimir, separar en variables individuales
print(a*2)
print(b)
print(c)
print(d)
print(my_tuple2[0])   #asi accedo al primer elemento, no puedo unpack un elemento solo

a, *b = my_tuple2  #con el asterisco = todo el resto en b
print(a*2)
print(b)  

#Exercise
#Unpack the following tuple into 4 variables
a_tuple = (10, 20, 30, 40)
a,b,c,d = a_tuple
print(a) #  10
print(b) #  20
print(c) #  30
print(d) #  40

# ---------
#set {} 
#almacenar valores desordenados
#No admite duplicadados
#puede comenzar vacío, con .add le agrego elementos 1 a 1

set_fruits = {'banana', 'pera', 'mango'}
set_fruits.add('manzana')
set_fruits.add('uva')
set_fruits.add('mango')  #lo ignora, no lo vuelve a ingresar xq duplica
print(set_fruits)

# ---------

#loop = 
# iterar, repetir algo mediante una instruccion/comando para cada elemento (1 a 1) de un "grupo" (lista, rango).

#For loops = Se detiene al llegar al final de la lista/rango
#Con indentation o sangría

fruits = ['apple', 'banana', 'kiwi', 'pear']
for fruit in fruits:
  print(fruit)

cities = ["London", "San Francisco", "Paris", "Barcelona"]
for city in cities:
    print("I once went to", city)

li = [2, 5, 7, 8]
my_sum = 0
for item in li:
    my_sum = my_sum + item
    print (f'current sum: {my_sum}')
print (f'final sum: {my_sum}')

#Ranges = 1 sequencia dado un valor inicial, un valor final y un salto en particular.
# Solo numeros int
#No es una lista. Es type range
#Permite las iteraciones
 
for n in range(4,19):   #19 no incluido
    print(n)   
    print(n*5)
    if n % 2 == 0 and n > 9:
        print(n)

for _ in range (10,-1, -1):  #va en reversa
    print (_)
print ('happy new year!')
           
for n in range(10, 21, 2):  #solo los pares
    print(n)   

for n in range(1,6):   #uno abajo del otro = no es una lista
     print(n)


#hacer un conteo de la suma de mis elementos
list1 = [0, 1, 2, 3]
counter = 0  #pongo la constante inicial afuera del loop
for i in list1:
    counter = counter + i
    print(counter)    #avanza a medida que avanza el loop, esta dentro del loop
print(f'final sum = {counter}')  #muestra la iteracion final pq eta afuera del loop


#Some built-in functions that use for loops : min max sum (no vimos ejemplos)

#Exercise
#Accept a number from the user and print its multiplication table
user_number = int (input("give a number: "))

for number in range(11):
    print(f"{user_number} x {number} = {user_number * number}")


#While loops = 
# La extensión no depende del largo de una lista/rango
# corre mientras la condición es True. Se detiene cuando se alcanza un punto de interrupción (condicion falsa).
# se ejecuta el loop, se prueba la condicion, se repite, hasta q la condicion ya no se cumple más.

current_number = 1 
while current_number <= 5:  
   print(current_number)   
   current_number += 1  #incremento despues del print
print("Finished")   # del 1 al 5

current_number = 1 
run = int (input ('how many times do you want to run this code? '))  #la longitud la decide el user
while current_number <= run:  
   print(current_number)   
   current_number += 1  #incremento despues del print
print("Finished")   # del 1 a run

current_number = 1 
while current_number <= 5:  
   current_number += 1   #incremento antes del print
   print(current_number)   
print("Finished")  # del 2 al 6

current_number = 0     #inicio en cero
while current_number < 5:  #no agrego el igual
   current_number += 1   #incremento antes del print
   print(current_number)   
print("Finished")    # del 1 al 5



li = [2, 5, 7, 8]
i = 0
while i < len(li):
    print (li[i])
    i += 1
print ('fin')

password = ''                                             #forma1
while password != 'secret123':
  password = input('What is the top secret password? ')
print('You guessed the right password!')


password = 'secret123'                                      #forma2
guess = input('What is the top secret password? ')

while guess != password:
    print ('Incorrect password')
    guess = input('What is the top secret password? ')
print('Right password!')

password = 'secret123'                                      #forma3 con limitacion de intentos
guess = input('What is the top secret password? ')
tries = 1
max_tries = 5

while guess != password and tries < max_tries:
    tries += 1
    print ('Incorrect password')
    guess = input('What is the top secret password? ')
if guess == password:
    print('Right password!')
if tries == max_tries:
      print('Number of attempts allowed exceeded')


#EXCERCISE #4
#Print the numbers from 1 to 10 using while loop
current_number = 1 
while current_number <= 10:    
    print(current_number)   
    current_number += 1

#for num in range(10):   #este es mejor pq usa menos código, pero no es while loop
#    print(num)


#Infinite loop = no hay condición que la frene
#while 1==1:
#    print ('looping...')

#Using a flag = true or false. Hace q todo el programa esté activo/desactivo

active = True
while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)
print("Goodbye !")

#Para gestionar el flujo del bucle tenemos break y continue

#break = cuando se ejecuta, Python sale del loop

while True: 
    city = input("Please enter the name of a city you have visited (enter 'quit'  when you are finished): ")
    if city == 'quit':
        break
    else:
        print("I'd love to go to", city)
print("Goodbye !")

secret_number = 4
while True:
    user_number = input('Guess the secret number: ')
    if int(user_number) == secret_number:
        print('Congrats! You win!')
        break
    else:
        print('Wrong guess...')


#continue:  vuelve al principio del bucle, sigo ejecutando codigo. "salta" una parte.
i = 0
while i < 10:
    i += 1         #incremento ANTES del if
    if i %2 == 0:  #skip numeros pares
          continue
    print (i)

current_number = 0
while current_number < 10:
    current_number += 1         #incremento ANTES del if
    if 3 < current_number < 7:  # If the number is between 3 and 7 
        continue                # Go back to the beginning of the loop
    print(current_number)

#ojo el orden, aca el loop while se hace infinito cuando current = 4
#current = 0
#while current <= 10:
#    print(current)
#    if 3 < current < 7:
#        continue
#   current += 1    #the incrementation is after the if statement



#Debugging = encontrar y corregir errores.
#Si el código tuviera “bichos” que hacen que no funcione, funcione mal, o explote.. los encontramos.

#al lado del numero de linea apretamos hasta q se ponga aun boton rojo
# modulo Run & Debug (F5) > python > current file para:
#leyer el código con lupa,
#probar valores,
#mirar errores que tira Python,
#usar print() o un debugger para ver qué está pasando paso a paso.