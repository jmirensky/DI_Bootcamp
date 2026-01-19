#W3 D1 30 Dic 25
#Excepciones = el programa se corta cuando encuentra un error, no avanza a las siguientes líneas

#Try:/except = dijo q es re importante
#Que el progrma no se corte cuando encuentra un error

#Tipos de errores:
# * de sintaxis, cuando hay una afirmación incorrecta. Ej error x parentesis, x puntuación...se soluciona escribiendo bien
# * Excepciones (error x dividir x cero, x index, x key, x persmiso, por archivo inexistente, etc). # Se solucionana
        # con una gestion de excepcon  try-except block 

#Try:/except:
#     PROBLEMATIC CODE
#     ADDITIONAL CODE
# except:
#     EMERGENCY CODE
# if the program crashes on PROBLEMATIC CODE, then ADDITIONAL CODE won't be reached

def age():
   user_age = input("How old are you?\n>>> ")
   try:
       user_age = int(user_age)
       print(f"Next year, you will be {user_age+1} years old")
       print("End of Message")
   except:
        print("Your age is not a real age")
age()
#NO HAY UN LOOP, TE LO PREGUNTA UNA SOLA VEZ

valid_flag = False
while not valid_flag:
    userage = input("How old are you?\n>>> ")
    try:
        userage = int(userage)
        valid_flag = True
    except:
        print("Please enter a real age v2")

print("Next year, your age will be",userage+1)
print("End of Message")
#HAY UN LOOP, Pueden hacer el error que quieren, arroja el emergency code y no se detiene hasta q se ingrese una edad valida

valid_flag = False
while not valid_flag:
    userage = input("How old are you?\n>>> ")
    try:
        userage= int(userage)
        valid_flag = True
    except:
        pass

print("Next year, your age will be",userage+1)
#HAY UN LOOP, Pueden hacer el error que quieren, pero no arroja el emergency code... No se detiene hasta q se ingrese una edad valida


#Exercise: Given a list of numbers, write a function that returns the sum of every number.
# BUT you can have a malicious string inside the list.
my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

def addit(num_list):
    total = 0
    for num in num_list:
        try:
          total +=num
        except:
            pass    #salta, ignora los maliciosos
   
    return total

print(addit(my_list))   #59


#the else statement
valid_flag = False
while not valid_flag:
    userage = input("How old are you?\n>>> ")
    try:    # TRY THIS
        userage = int(userage)
    except: # IF YOU GOT AN ERROR
        print("Wrong age v3!")
    else:   # ELSE
        valid_flag = True

print("Next year, your age will be",userage+1)


#the finally statement
valid_flag = False
while not valid_flag:
    userage = input("How old are you?")
    try:    # TRY THIS
        userage= int(userage)
    except: # IF YOU GOT AN ERROR
        print("Wrong age v4!")
    else:   # ELSE
        valid_flag = True
    finally:
        print('There may or may not have been an exception.')

print("Next year, your age will be",userage+1)


#desarrollo de Juliana, mezcla un poco de todo lo anterior
secret_number = 50
while True:  #significa que que el loop no se termina, excepto que se alcance el break
    try:
        number = int(input('give me a number: '))
        if number == secret_number:
            print(f'You won! Secret number was {secret_number}')
            break
        else:
            print(f'Sorry, {number} is not the Secret number = {secret_number}')
            break
    #except:    #el codigo no se rompe ni se interrumpe
        # sirve para cuando caigo en un error, ej de data type (puse una letra, un float, un simbolo, un espacio)
        #print('sorry, you need to say a number, try again')   #respuesta elegante
    except Exception as e:
        print(e)    
        #me dice exacto cual fue el error  --> invalid literal for int() with base 10: 'd'... respuesta "técnica"
    finally:
        print("End of Message")   #algo que sale siempre
print('thank you for playing with us')


#Raising an exception = plantear a propósito una excepcion, un error cuando ocurre una condición específica.
# PEROOOO el programa NO sigue
#  x = 10
#  if x > 5:
#       raise Exception(f"x should not exceed 5. The value of x was {x}")
#The error that will appear is your own custom error
#Traceback (most recent call last):
  #File "fffff.py", line 52, in <module>
    #raise Exception(f"x should not exceed 5. The value of x was {x}")
#Exception: x should not exceed 5. The value of x was 10'

#Para que el programa siga: podemos usar un error de Aserción. Es otra forma de plantear una excepción, 
#sirve cuando buscamos un error específico mientras pretendemos mantener nuestro programa en marcha.
z = 9
try:
    assert 1 == z
except AssertionError:
    print(f"Error: Value of z = {z} is not correct...")

print('holisss')