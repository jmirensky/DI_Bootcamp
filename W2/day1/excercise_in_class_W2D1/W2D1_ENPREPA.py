#W2 D1  21Dic25

# funciones  f(x)
#keep the code "dry"
    # do not repeat

# cuando la estamos construyendo: empieza con def
#def say_hello():   #funcion definition con name, entre () van los parametros. () son mandatorios anque vayan vacios
#    """A function that says hello"""  # es como un comentario, no se ejecuta
#    print("Hello!") # con indention

#say_hello()  #funcion call
#say_hello()
#say_hello()

#pasar info (argumentos / parametros) a la funcion
#valor q la funcion usa, es la x de f(x)

# def say_hello(username):
#    print(f"Hello "+ {username})  #NO ME SALIO Q SE COMPLETE CON RICK
    
#say_hello("Rick") # "Rick" is an argument
# output "Hello Rick"

#ESTA PARTE NO SE SI ENTENDI pero primero la definicion, despues el argumento

#def say_hello(username, language):
#    if language == "EN":
#        print("Hello "+username)
#    elif language == "FR":
#        print("Bonjour "+username)
#    else:
#        print("This language is not supported: " + language)

#hicieron algo con un input ???

#say_hello("Rick", "FR")   #aca si iria en orden
#say_hello(username="Rick", language="FR")
#say_hello(language="FR", username="Rick")  #no importa el orden
#elegi un metodo y apegate a ese, no mezcles

#default value

#def say_hello(username, language = 'EN'):  #En es el idioma en default
#    if language == "EN":
#        print("Hello "+username)
#    elif language == "FR":
#        print("Bonjour "+username)
#    else:
#        print("This language is not supported: " + language)

#say_hello("PHILLIP", "FR")   
#say_hello("REBECA") # si no aclaro idioma me toma el default
#say_hello (username = 'Tom Sawyer')  # si no aclaro idioma me toma el default

#Avoiding argument errors
#the number of arguemtnso = debe matchear

#my_number = 4    #global scope

#def numberator(number):
#    new_number = my_number * number
#    print(f'{my_number} times {number} is {new_number}')  #tengo acceso a 3, 2 locales y  global

#numberator(9)  #es una multiplicacion

#print(my_number)  #global scope
#print(new_number)  #is not defined, es local
#print(number)    #is not defined, es local

#funciones dentro de funciones

#Return values
#no hace falta display/imprimir el resultado de la funcion, sino que lo uso para otra cosa

my_number = 4   #local and global scope

def numberator(number):  #global scope
    new_number = my_number * number  #local scope
    return new_number  #not in the global scope

my_val = numberator(9)   #36
print (my_val * 8)   #288


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)    #Jimi Hendrix

#funciona con listas y tuplas tambien

def divide_by_three(number):
  return number / 3

first_number = 12
first_number_computed = divide_by_three(first_number)
print(first_number_computed)  #4.0

second_number = 27
second_number_computed = divide_by_three(second_number)
print(second_number_computed) #9.0


#Excercise
#Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it.
# And also it must return both addition and subtraction in a single return call

#def calculation(a, b):
#    return (a-b, a+b)

#minus, plus = calculation(40, 10)
#print(minus, plus)   #30  50

#print(calculation)   #guardado en esta direccion de la ram <function calculation at 0x0000020729433950>

#Passing list as function arguments
#def greet_users(users):             # users should be a list
#    for user in users:              # Because it's a list, we can loop through it
#        print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

#usernames = ["steve", "stan", "debbie"]
#greet_users(usernames)


#Seeing functions as an address   = no me salio

#lo que el explico con una lista de funciones.. no entendi nada
#ver codigo
#para que serviria esto?

#def my_f1():
#    print("Hello")

#def my_f2():
#    print("Word")

#def my_f3():
#    print("This is Rick!")

#list_of_functions = [my_f1, my_f2, my_f3]

#for function in list_of_functions:
#    function()

#Modifying a list in a function
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

# Simulate printing each design until none are left. 
# Move each design to completed_models after printing. 

while len(unprinted_designs) != 0:    
    current_design = unprinted_designs.pop() #lo eliminado lo guarda como objeto

    # Simulate creating a 3D print from the design.    
    print("Printing model: " + current_design)    
    completed_models.append(current_design)    

# Display all completed models. 
print("\nThe following models have been printed:") 
for completed_model in completed_models:    
    print(completed_model)

#Printing model: iPhone case
#Printing model: robot pendant
#Printing model: dodecahedron

#al final dijo que esto estaba mal??
#Printing model: dodecahedron
#Printing model: robot pendant
#Printing model: iphone case

#The following models have been printed:
#dodecahedron
#robot pendant
#iphone case


#def print_models(unprinted_designs, completed_models):
#    """    
#    Simulate printing each design until none are left.    
#    Move each design to completed_models after printing.    
#    """

#    while unprinted_designs:        
#        current_design = unprinted_designs.pop()            

#        # Simulate creating a 3D print from the design.        
#        print("Printing model: " + current_design)        
#        completed_models.append(current_design)        

#def show_completed_models(completed_models):    
#    """
#    Show all the models that were printed.
#    """    
#    print("\nThe following models have been printed:")   
#    for completed_model in completed_models:        
#        print(completed_model)        

#unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
#v2
# unprinted_designs = ['starship Enterprise', '5 shekel thing'] #o sea agrega ests 2 a los 3 primeros
#completed_models = []

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)

#Printing model: dodecahedron
#Printing model: robot pendant
#Printing model: iphone case

#The following models have been printed:
#dodecahedron
#robot pendant
#iphone case

# ------------
#o sea agrega ests 2 a los 3 primeros
#The following models have been printed:
#dodecahedron
#robot pendant
#iphone case
#Printing model: 5 shekel thing
#Printing model: starship Enterprise

#The following models have been printed:
#5 shekel thing
#starship Enterprise

#*args
#**kwargs
#no entendi que son ni para que funcionan
#es para funciones q requieren muchos argumentos


#Lambda, Map, Reduce & Filter Functions
#dijo q lambda es lo + importante

#no entendi que son ni para que funcionan
#map_functions
#filter () functions
#reduce algo que hay q importar

#lambda = 1 linea... es como hacer una funcione en 1 sola linea ?

#Exercise
#Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters

#chat GTP
names = ["Ana", "Juan", "Sofia", "Luis", "Pedro", "Luz"]

short_names = filter(lambda name: len(name) <= 4, names)
greetings = map(lambda name: f"Hello {name}", short_names)

print(list(greetings))



#lo va aenviar el profe x slack
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

filter_short_names = filter(lambda name: len(name) <= 4, people)
#print(filter_short_names)
mapped_list_greetings = map(lambda name: f"Hello {name}", filter_short_names)

print(list(mapped_list_greetings))

#work shop o masterclass 5.30 vinecodign o algo asi?
# despues hay 1 mniproyect, o sea hay q traer algo preparado
