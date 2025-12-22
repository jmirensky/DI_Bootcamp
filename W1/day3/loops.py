#loop = 
# iterar, repetir algo mediante una instruccion/comando para cada elemento (1 a 1) de un "grupo" (lista, rango).

#For loops = Se detiene al llegar al final de la lista/rango
#Con indentation 

#fruits = ['apple', 'banana', 'kiwi', 'pear']
#for fruit in fruits:
#  print(fruit)

#cities = ["London", "San Francisco", "Paris", "Barcelona"]
#for city in cities:
#    print("I once went to", city)


#Ranges = 1 sequencia dado un valor inicial, un valor fina y un salto en particular.
# Solo numeros int
#No es una lista
 
#for n in range(4,19):   #19 no incluido
#    print(n)   
#    print(n*5)

#for n in range(10, 20, 2):  #solo los pares
#    print(n)   

#for n in range(1,6):   #uno abajo del otro = no es una lista
#    print(n)

#numbers = list(range(1,6))  #convierte el rango en lista
#print(numbers)


#Some built-in functions that use for loops : min max sum (no vimos ejemplos)

#Exercise
#Accept a number from the user and print its multiplication table
#user_number = int (input("give a number: "))

#for number in range(11):
#    print(f"{user_number} x {number} = {user_number * number}")


#While loops = 
# La extensión no depende del largo de una lista/rango
# corre mientras la condición es True. Se detiene cuando se alcanza un punto de interrupción (condicion falsa).
# #se ejecuta el loop, se prueba la condicion, se repite, hasta q la condicion ya no se cumple más.

#current_number = 1 
#while current_number <= 5:  
#   print(current_number)   
#   current_number += 1  #incremento despues del print
#print("Finished")   # del 1 al 5

#current_number = 1 
#while current_number <= 5:  
#   current_number += 1   #incremento antes del print
#   print(current_number)   
#print("Finished")  # del 2 al 6

#current_number = 0     #inicio en cero
#while current_number < 5:  #no agrego el igual
#   current_number += 1   #incremento antes del print
#   print(current_number)   
#print("Finished")    # del 1 al 5

#password = ''
#while password != 'hello-world-123':
#  password = input('What is the top secret password? ')

#print('You guessed the right password!')

#EXCERCISE #4
#Print the numbers from 1 to 10 using while loop
#current_number = 1 
#while current_number <= 10:    
#    print(current_number)   
#    current_number += 1

#for num in range(10):   #este es mejor pq usa menos código, pero no es while loop
#    print(num)


#Infinite loop = no hay condición que la frene
#while 1==1:
#    print ('looping...')

#Using a flag = true or false. Hace q todo el programa esté activo/desactivo

#active = True

#while active: 
#    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
#    if city == 'quit':
#        active = False
#    elif city == 'leave me alone':
#        active = False
#    elif city == 'stop':
#        active = False
#    else:
#        print("I'd love to go to", city)

#print("Goodbye !")

#Para gestionar el flujo del bucle tenemos break y continue

#break = cuando se ejecuta, Python sale del loop

#while True: 
#    city = input("Please enter the name of a city you have visited (enter 'quit'  when you are finished): ")
#    if city == 'quit':
#        break
#    else:
#        print("I'd love to go to", city)
#print("Goodbye !")

#secret_number = 4

#while True:
#    user_number = input('Guess the secret number: ')
#    if int(user_number) == secret_number:
#        print('Congrats! You win!')
#        break
#    else:
#        print('Wrong guess...')


#continue:  vuelve al principio del bucle, sigo ejecutando codigo. "alta" una parte.

#current_number = 0
#while current_number < 10:
#    current_number += 1         #incremento ANTES del if
#    if 3 < current_number < 7:  # If the number is between 3 and 7 
#        continue                # Go back to the beginning of the loop
#    print(current_number)

#ojo el orden, aca el loop while se hace infinito cuando current = 4
#current = 0
#while current <= 10:
#    print(current)
#    if 3 < current < 7:
#        continue
#   current += 1    #the incrementation is after the if statement