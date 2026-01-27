#  OOP and Modules
#W3 D3 04 ENE26

#Python modules
'''Un módulo es un archivo .py que guarda código (funciones, clases y variables -arrays, dictionaries, objects, etc.-)
para usarlo en otro lado. Usa el comando import.'''

#1) creadas  x el usuario  User-defined. ejemplo

#Archivo: math_utils.py
#def sum_numbers(a, b):  #define a function in myModule.py
#    return a + b

#Archivo: main.py

#Importar todo
#import math_utils    #callModule.py
#print(math_utils.sum_numbers(3, 4))    #myModule.myFunction

#Importar solo lo que necesitás
#from math_utils import sum_numbers    #call the function in the Module
#sum_numbers(1, 2)                     #the function    


#2) ya vienen integrados/incorporados con Python  Built in
#import moduleName #call a module
#moduleName.function()#use module function

#Ejemplo
import math
print("The value of cosine is", math.cos(3))
print("The value of sine is", math.sin(3))
print("The value of tangent is", math.tan(3))
print("The value of pi is", math.pi)

'''Beneficios:
Código estructurado = el código se organiza lógicamente agrupándose en un solo archivo Python, lo que facilita el desarrollo y es menos propenso a errores.
El código es más fácil de entender y usar.

Reutilizabilidad = La funcionalidad definida en un solo módulo puede ser fácilmente reutilizada por otras partes de la aplicación. 
Esto elimina la necesidad de recrear código duplicado.

* no repetir código
* separar responsabilidades
* reutilizar
* mantener el proyecto legible '''


# Modulo Collections en Python
# 6 estructuras de datos especiales, más eficientes o más cómodas que las básicas (list, dict, tuple).

# 1 defaultdict = Diccionario sin KeyError
# Un diccionario que no rompe cuando accedés a una clave que no existe.
# En vez de KeyError, devuelve un valor por defecto. 
# Uso típico: contadores - acumuladores

from collections import defaultdict  
nums = defaultdict(int)  
nums['one'] = 1  
nums['two'] = 2
nums['three'] = 3 
print(nums)
print(nums['four'])  # 0 --> aunque el 4 no se inicializó, el compilador devuelve un valor, 0 al intentar acceder a él.

# 2 Counter
# Para contar ocurrencias de elementos.
# Dado una lista → devuelve cuántas veces aparece cada valor
# Uso típico: conteo de palabras, frecuencias, análisis de datos 

from collections import Counter  
my_list = [1,2,3,4,1,2,6,7,3,8,1,2,2]  
answer=Counter()
answer = Counter(my_list)  
print(answer[2])  #4

#3 deque
# Una lista optimizada para: agregar - remover elementos desde ambos extremos
# Más rápida que una list para esto.
# Colas y pilas eficientes

from collections import deque  
#initialization
list = ["a","b","c"]  
deq = deque(list)  
print(deq)  

#insertion = z is being added at the end of the given list and g is at the start of the same list.
deq.append("z")  
deq.appendleft("g")  
print(deq)
#removal
deq.pop()  
deq.popleft()  
print(deq)


# 4 namedtuple
# Una tupla con nombres en vez de índices.
# No hace falta recordar el indice de cada campo de un objeto tupla
# En lugar de t[0]  Usás t.nombre
# Uso típico: registros simples - datos inmutables con estructura clara

from collections import namedtuple
Student = namedtuple('Student', 'fname, lname, age, dog')  
s1 = Student('Peter', 'James', '13', 'Rex')  
print(s1.fname) 
print(s1.dog) 


# 5 ChainMap
# Une varios diccionarios y devuelve una sola lista, lo encapsula en una sola unidad.
# No los copia
# Busca la clave en orden

import collections

dictionary1 = { 'a' : 1, 'b' : 2 }  
dictionary2 = { 'c' : 3, 'b' : 4 }  
chain_Map = collections.ChainMap(dictionary1, dictionary2)  
print(chain_Map.maps)  


# 6 OrderedDict
# Diccionario que mantiene y garantiza el orden de inserción. Incluso si se cambia el valor de la clave posteriormente, la posición se mantendrá.
# Desde Python 3.7, los dict normales ya mantienen el orden, así que hoy: se usa poco - en casos muy específicos

from collections import OrderedDict  
order = OrderedDict()  
order['a'] = 1  
order['b'] = 2  
order['c'] = 3  
print(order)  

unordered=dict()  #unordered dictionary
unordered['a'] = 1  
unordered['b'] = 2  
unordered['c'] = 3 
print("Default dictionary", unordered)



#itertools en Python 
# módulo para trabajar con iteradores (for-loop) de forma: eficiente, elegante, legible
# Se usa cuando necesitás recorrer datos sin crear listas innecesarias.
# Trabaja sobre iterables 
# No guarda todo en memoria
# Produce valores uno por uno
# Ideal para: loops grandes - pipelines de datos - evitar código pesado
# 2 tipos
    # *Infinitos: count, cycle, repeat (continuarán ejecutándose indefinidamente si no se establece una condición de corte) vs
    # * Finitos: chain, compress, dropwhile. (terminan, no se entra en un bucle infinito).

# Count(start, step): toma dos argumentos opcionales y devuelve un iterador.
#  - 1° argumento determina el valor inicial.
#  - 2° argumento indica cuánto se incrementará el valor en cada paso.
# Si no se proporcionan los argumentos, el valor predeterminado para el inicio será 0 y el valor para el paso será 1.
# Genera números infinitos.... # Siempre poné condición de corte!
# Uso típico: contadores, secuencias

#print the first four even numbers 0 2 4 6
import itertools
result = itertools.count(start = 0, step = 2)
for number in result:
# termination condition
    if number < 8:
        print (number)
    else:
        break
    # 0
    # 2
    # 4
    # 6

# cycle(iterable)
# Repite un iterable una y otra vez. Recorre elemento por elemento
# Uso típico: patrones repetidos, simulaciones

# print hasta contar 10 repeticiones
import itertools
result = itertools.cycle('abc')
counter = 0
for number in result:
# termination condition
    if counter < 10 :
        print (number)
        counter = counter + 1
    else:
        break
    # a
    # b
    # c
    # a
    # b
    # c
    # a
    # b
    # c
    # a

# repeat(element, times) = como cycle, pero repite un mismo valor, el objeto entero

# print hello two times
import itertools
result = itertools.repeat('hello', times = 2)
for word in result:
    print (word)
    # hello
    # hello

# chain() = Une varios iterables y los recorre a todos en orden.

# iterate over three lists
import itertools
list_one = ['a', 'b', 'c']
list_two =['d', 'e', 'f']
list_three = ['1', '2', '3']
result = itertools.chain(list_one, list_two, list_three)
for element in result:
  print (element)
    # a
    # b
    # c
    # d
    # e
    # f
    # 1
    # 2
    # 3

# compress(data, selectors) = Filtra datos según una lista de booleanos.
# Uso típico: máscaras - filtros claros y expresivos
#find the names of people who have the flu
import itertools
names = ['Alice', 'James', 'Matt']
have_flu = [True, True, False]
result = itertools.compress(names, have_flu)
for element in result:
  print (element)
    # Alice
    # James


# dropwhile(condition, iterable)
# Se le pasa un iterable y una función (predefinida o lambda).
# Según la condición dentro de la función, dropwhile continúa eliminando valores del iterable hasta que encuentra el primer elemento que evalúa como falso.

# Descarta elementos mientras la condición sea true. Cuando falla por primera vez, devuelve todo lo demás.
# Ojo: no filtra todo, solo actúa hasta que la condición deje de cumplirse

import itertools
my_list = [0, 0, 1, 2, 0]
result = itertools.dropwhile(lambda x: x == 0, my_list)
for elements in result:
  print (elements)
    # 1
    # 2
    # 0

# - - - - - - 

#Class Atribute
# un atributo que pertenece a la clase, es compartido por todas las instancias.
# No es del objeto, es del molde.
# Se define fuera del __init__
# Se usa para:
#     ✔ constantes compartidas
#     ✔ configuraciones globales
#     ✔ contadores
#     ✔ valores comunes a todos los objetos

class Dog:
    number_of_dogs = 0
    dogs_king = "Bernie IV"   #atributo de la clase

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print(f"A new dog has been initialized! His name is {name_of_the_dog}")
        self.name = name_of_the_dog
        # Increment the number of dogs
        Dog.number_of_dogs += 1

    def bark(self):
        print(f"{self.name} barks ! WAF")

    def walk(self, number_of_meters):
        print(f"{self.name} walked {number_of_meters} meters")

    def rename(self, new_name):
        self.name = new_name

dog1 = Dog("Rex")    #A new dog has been initialized! His name is Rex
dog2 = Dog('Paul')   #A new dog has been initialized! His name is Paul
dog3 = Dog('Ash')    #A new dog has been initialized! His name is Ash
dog4 = Dog("Bernie V")  #A new dog has been initialized! His name is Bernie V

dog3.walk(130)  #Ash walked 130 meters
dog4.bark()   #Bernie V barks ! WAF

print("The king of the dogs is:", Dog.dogs_king)  #The king of the dogs is: Bernie IV
print(dog1.dogs_king)  #Bernie IV  

print(f"Curently, there are {Dog.number_of_dogs} dogs")  #Curently, there are 4 dogs

Dog.dogs_king ='Philipe'  #edito el atributo de la clase
print(dog2.dogs_king)  #Philipe  


#excercise
#Analyse the code below. What will be the outputs ?
#Explain the goal of the methods
class Circle:
    color = "red"   #atributo de la clase

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2)
print(circle1.color) #red   (Busca en el objeto → no está → va a la clase)
print(Circle.color)   #red    (class attribute puro)
print(circle1.get_color())  #red   (devuelve el atributo de clase)
print(circle1.diameter)  #2
circle1.grow(3)
print(circle1.diameter) # 3 * 2 = 6   

circle1.color = 'blue'
print(circle1.color) #blue  #crea un atributo nuevo solo en ese objeto, x fuera del init. NO cambia Circle.color
print(circle1.get_color())  #red  --> porque hace el return de la clase. → accede a un dato compartido por todos


# - - - - -   

#Class Decorators: @staticmethod, @classmethod, @property
#funciones que cambian cómo se comportan los métodos dentro de una clase.
#

# @staticmethod
'''El código pertenece a una clase, pero no utiliza el objeto en sí.
Al usar @staticmethod, sabemos que el método no depende del estado del objeto.
Limita un método a la definición de la clase.'''
# Método que NO usa self
# Vive dentro de la clase por organización, no por dependencia

class Person:
    pass

class Man(Person):
    sex = "Male"

    @staticmethod
    def get_nicknames():
        return ["Bro", "Dude", "Buddy"]

print(Man.get_nicknames())  #['Bro', 'Dude', 'Buddy']
print(Man.get_nicknames()[0])  #Bro


class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
print(Math.add(3,6))  #9


# @classmethod
'''métodos que no están vinculados a un objeto, sino a una clase. Su primer argumento es la propia clase.'''
# Método ligado a la clase, no al objeto
# Recibe cls como primer argumento
# Accede a class attributes
# Para qué sirve
    # ✔ trabajar con variables de clase, como los contadores
    # ✔ constructores alternativos
    
class MyClass:
    __counter = 0

    @classmethod
    def add(cls,a): 
        return cls.__counter + a

print(MyClass.add(3))  #3  -->   se llama como Clase.metodo()

new_class = MyClass
new_class.__counter = 1
print(MyClass.add(3))  #3 --> the method add refers to the class definition, not the counter of the new_class  [NO ENTIENDO]


class MyClass2:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

print(MyClass2.get_count())  #0
#querés ver cómo cambia:
MyClass2.count = 5
print(MyClass2.get_count())  #5



class MyClass3:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

MyClass3.increment()  #ejecuté increment x1
MyClass3.increment()  #ejecuté increment x1
print(MyClass3.get_count())  #2


from datetime import date

class MyClass4:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        MyClass4.count += 1

    @classmethod
    def fromYear_get_age (cls, name, birth_year):    #constructor alternativo = #generar la edad de las personas a partir del año de nacimiento
        THIS_YEAR = date.today().year
        return cls(name, THIS_YEAR - birth_year)  #no pone self

    @classmethod
    def get_count(cls):
        return cls.count
    
    def __str__(self):
        return f"{self.name}, {self.age} años"

person = MyClass4.fromYear_get_age("Juan", 1990)  
person1 = MyClass4.fromYear_get_age("Clara", 1992) 

print(person.name)  #Juan
print(person.age)  #36 --> se ASOCIA con el resultado del metodo fromYear_get_age !!
print(person.__dict__)  #{'name': 'Juan', 'age': 36}
print(person)  #Juan, 36 años
print(MyClass4.get_count())  #2
print(MyClass4.__str__(person) )  #Juan, 36 años



# @property
# 1. Getter = Sirve para fabricar atributos x fuera del init, usando un métodos (simulan atributos reales)
# 
# atributos calculados
# Beneficio:
#     ✔ código más limpio
#     ✔ encapsulación
#     ✔ no rompés código si cambia la lógica interna

class MyClass5:
  def __init__(self, first_name, last_name):
    self.__first_name = first_name      #con __ es atributo privado
    self.__last_name = last_name

  @property
  def email(self): 
    return f"{self.__first_name}.{self.__last_name}@gmail.com"

obj1 = MyClass5("John", "Doe")    #creado con el metodo, con el atributo
#print(obj1.email())  # TypeError: 'str' object is not callable
print(obj1.email)  #SIN PARENTESIS  --> John.Doe@gmail.com     #atributo calculado


from datetime import date

class Person:
    used_names = set()    #ninguna persona puede llamarse igual que otra (identificadores únicos simples)

    def __init__(self, name, age):
        if name in self.used_names:
            name = input("That name is taken. Enter another name: ")   #input() dentro de la clase no es buena práctica

        self.name = name
        self.age = age                 #se ASOCIA con el resultado del metodo fromYear_getage !
        self.used_names.add(name)

    @classmethod
    def fromYear_getage(cls, name, birth_year):      #generar la edad de las personas a partir del año de nacimiento
        THIS_YEAR = date.today().year
        return cls(name, THIS_YEAR - birth_year)

    @property                                    #generar atributos desde un método, fuera del __init__
    def professional_name(self):
        return "Mr-Mrs-Miss " + self.name   

p1 = Person("Carlos", 40)
p2 = Person.fromYear_getage("Carlos", 1980) #--> That name is taken. Enter another name: Pedro
print(p1.professional_name)  #Mr-Mrs-Miss Carlos   (parece atributo, pero es metodo)
print(p2.professional_name)  #Mr-Mrs-Miss Pedro    (parece atributo, pero es metodo)
print(Person.used_names)  #{'Pedro', 'Carlos'}


#2. Setter
# permiten asignar-modificar valores a los atributos privados de una clase.
# el profesor omitio esta exxplicacion
class MyClass6:
  def __init__(self, first_name, last_name):
    self.__first_name = first_name          #con __ es atributo privado
    self.__last_name = last_name

  @property
  def email(self): 
    return f"{self.__first_name}.{self.__last_name}@gmail.com"

  @email.setter
  def email(self, name): 
    self.__first_name = name

obj1 = MyClass6("John", "Doe")
obj1 .email = "Sarah"
print(obj1.email)  #SIN PARENTESIS --> Sarah.Doe@gmail.com



#Exercise: Analyze the code below. What will be the ouput ?

class MyClass(object):
    count = 0              #pertenece a la clase.

    def __init__(self, val):
        self.val = val
        MyClass.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):     #classmethod: mira la clase, no el objeto.
        return cls.count

object_1 = MyClass(10)         #entra al __init__ y suma 1 a MyClass.count.
    #val = 10  y count pasa de 0 a 1
print("\nValue of object : %s" % object_1.get_val())    #Value of object : 10
print(MyClass.get_count())                              #1

object_2 = MyClass(20)         #entra al __init__ y suma 1 a MyClass.count.
    #val = 20  y count pasa de 1 a 2
print("\nValue of object : %s" % object_2.get_val())    #Value of object : 20
print(MyClass.get_count())                              #2



#Exercise: Analyze the code below. What will be the ouput ?

class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        MyClass.count += 1

    @staticmethod
    def filterint(value):       #NO usa self ni cls. Es una función común “guardada” dentro de la clase. Sirve para validar datos, nada más      
        if not isinstance(value, int):
            print("Entered value is not an INT, value set to 0")
            return 0
        else:
            return value


a = MyClass(5)    #5 es int → se guarda 5 y count = 1
b = MyClass(10)   #10 es int → se guarda 10 y count = 2
c = MyClass(15)   #15 es int → se guarda 15 y count = 2

print(a.val)    #5
print(b.val)    #10
print(c.val)    #15
print(a.filterint(100))  #100 --> 100 es int, No imprime advertencia, Devuelve 100




# ---------

#Dunder Methods (special methods, magic methods)
#Empieza y termina con __  doble underscore
#Python lo llama solo, sin que vos lo invoques. Python los ejecuta por detrás..
# Forma en que Python traduce acciones normales (+, print, len) en métodos internos.

#__init__   called when you create an instance (nace el objeto + inicializar atributos)
# def __init__(self, val):
#     self.val = val

#__str__   what print(obj) shows =  convert an object to a string = representacion informal de un string,
                                    #  #una linda presentacion cuando hago print del objeto
# def __str__(self):
#     return "Hola"

#__len__   what len(obj) returns = return the length of the object
# def __len__(self):
#     return 5

#__call__  the instance become a dunder metod. El objeto se comporta como una función. Al llamar al objeto (agregar () al final del nombre).
# obj.__call__()

# __repr__    para calcular la representación oficial de string de un objeto.  “behind the scenes” look at the object.
# def __repr__(self):
#     return "Objeto Person"

#__getitem__  how obj[key] works

# __add__   cuando usamos + 
# a.__add__(b)
first_list = ["a", "b", "c"]
second_list = ["d", "e", "f"]

print("\nCalling the `+` builtin with both lists")
print(first_list + second_list)
# >> Calling the `+` builtin with both lists
# ['a', 'b', 'c', 'd', 'e', 'f']

print("\nCalling `__add__()` with both lists")
print(first_list.__add__(second_list))
# >> Calling `__add__()` with both lists
# ['a', 'b', 'c', 'd', 'e', 'f']

# Cuando usás un operador o una función built-in, Python llama un dunder.
# Vos escribís	            Python ejecuta
# x = A()	                A.__new__() → A.__init__()
# print(obj)	            obj.__str__()
# len(obj)            	    obj.__len__()
# obj1 + obj2	            obj1.__add__(obj2)
# obj()	                    obj.__call__()

#Example with __repr__()     | representation | usefull info for the developer
class Person:
  def __init__(self, name, age):
      self.name = name
      self.age  = age

  def __repr__(self): 
      return f"{self.__class__.__name__} : {self.name} {self.age}"   
      #return f"{self.__class__.__name__} is a cool person"       #Person is a cool person

newPerson = Person('Sarah', 24)

print(newPerson) # Person : Sarah 24 
# __repr__ is the representation of an object


class Eden:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f"Hello! my name is {self.name}" 
     
    def __len__(self):
        return len(self.name)
    
    def __call__(self):
        return f"{self.name} is {self.height} cm tall."
    
    def __repr__(self):
        return f"{self.name} is a cool person"
    
my_friend = Eden('Eden', 190)

print(str(my_friend))   #Hello! my name is Eden    __str__
print(my_friend)  #Hello! my name is Eden   __str__

print(len(my_friend))  #4   __len__


res = my_friend()
print(res)  #Eden is 190 cm tall.    __call__
print(repr(my_friend))   #Eden is a cool person    __repr__


#Example with __add__()
class Car:
    def __init__(self, color):
        self.color = color

    def __add__(self, other):
        if isinstance(other, Car):
            print("CRASH!!!")
            print(f"{self.color} + {other.color}")
            return None
        else:
            raise TypeError("Can only add Car to Car")

my_car = Car("green")
abdallah_car = Car("blue")
my_car.__add__(abdallah_car)
    # CRASH!!!
    # green + blue
#added_again = my_car + abdallah_car  ES LO MISMO QUE EL DUNDER
    # CRASH!!!
    # green + blue


#Example with __add__()
class Person:
  def __init__(self, name, lastName):
      self.name = name
      self.lastName = lastName

  def __repr__(self):
      return f"{self.__class__.__name__} : {self.name} {self.lastName}"

  def __add__(self, other):
      return Person(self.name, other.lastName)   #self + another, regresa una nueva persona

father = Person('John', 'Snow')
mother = Person('Kaleesi', 'MotherOfDragons')
# using the __add__() method
dragon1 = father + mother 
print(dragon1)  # Person : John MotherOfDragons // __add__ is called to add two objects
dragon2 = mother + father
print(dragon2)  # Person : Kaleesi Snow

print(type(dragon1 ))  # <class '__main__.Person'>

print(dir(dragon1 ))  # todos los dunder methods que se le pueden aplicar al objeto
# ['__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__',
#  '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
#  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__',
#  '__str__', '__subclasshook__', '__weakref__', 'lastName', 'name']




 #"Overload" (sobrecargar) un método dunder significa darle un significado más amplio que su significado original.
 # Solo necesita definir el método correspondiente en su clase. 
 
class Person:
  def __init__(self, name, lastName):
      self.name = name
      self.lastName = lastName

#Overloaded the method by redefining '__repr__ 'using 'def' and passed the argument '(self)'
#definir un dunder para cambiar el comportamiento por defecto.
# We can write whatever we want inside this method, but we have to return an object.
  def __repr__(self):
    return f"{self.__class__.__name__} : {self.name} {self.lastName}"

  def __add__(self,other):
      name = self.name[0] + other.name[1:]
      lastname = other.lastName
      return Person(name,lastname)

father = Person('John', 'Snow')
mother = Person('Kaleesi', 'MotherOfDragons')

dragonChild = father + mother # using the __add__() method
print(dragonChild) #Person : Jaleesi MotherOfDragons


# --------------------------------------------------
# Clase PrintList
# --------------------------------------------------
class PrintList():
    '''Constructor: guarda la lista dentro del objeto'''
    def __init__(self, my_list):
        self.mylist = my_list

    # # Representación en consola del objeto
    def __repr__(self):
        return str(self.mylist)

# Usamos PrintList
pl = PrintList(["a", "b", "c"])
print(pl) # >> ['a', 'b', 'c']




#Modules = archivos de python individuales que pueden importarse y usarse dentro de otro archivo.
# Sirve para ordenar código y reutilizar funciones y clases.
# Módulos comunes
    # time → tiempo
    # random → aleatorios
    # os → sistema operativo
    # requests → HTTP (APIs)


#1. import
import math   #Importa todo el módulo.
print(math.sqrt(9))  #usar modulo.funcion   #3

#por convención, las declaraciones de importación van en la parte superior de la página.

#2. from
from math import floor    #Importa solo lo que necesitás.
print(floor(9.8))  #9     #Usás la función directamente, sin el nombre del módulo. --> floor redondea hacia abajo al entero más cercano.

#3. as
import math as m    #Le ponés un apodo al módulo. Muy común y práctico. Código más limpio
print(m.sqrt(16))  #4

#4. pip = instala paquetes desde internet, Se usa desde la terminal!
# Conviene activar el ambiente virtual
# Un paquete es una carpeta con varios módulos.
# Puede tener un __init__.py (hoy no es obligatorio, pero sigue apareciendo).
# Al importar el paquete, ese archivo se ejecuta.


#CheatSheet on Dunder Methods
#Binary Operators
#Assignment Operators
#Unary Operators
#Comparison Operators


#Modulo os
#para interactuar con el sistema operativo y manipular archivos y directorios... safety things
# Para tareas más avanzadas, se puede usar shutil.
    # os.name → nombre del sistema operativo
    # os.getcwd() → directorio de trabajo actual
    # os.environ → variables de entorno

# Manipulación de archivos y directorios
# Listar contenido:
        # os.scandir(directory) → lista los archivos/directorios de un directorio
        # os.walk(directory) → lista archivos/directorios recursivamente
# Crear directorios:
        # os.mkdir() → crea un directorio
        # os.makedirs() → crea varios directorios de golpe
# Renombrar/Eliminar:
        # os.rename() → renombrar archivos o carpetas
        # os.remove() → eliminar archivos
        # os.removedirs() → eliminar carpetas vacías

# Manipulación de nombres y rutas, Usando os.path:
    # os.path.exists(filename) → verifica si existe
    # os.path.isfile(filename) → verifica si es archivo
    # os.path.isdir(filename) → verifica si es directorio
    # os.path.abspath(filename) → ruta absoluta
    # os.path.basename(path) → nombre del archivo
    # os.path.dirname(path) → carpeta padre
    # os.path.join(dir, file) → combinar rutas
    # os.path.splitext(filename) → obtener extensión# Para funciones de rutas más avanzadas, usar pathlib.



#Time and Datetime modules - hora y fecha/Hora [el profesor dijo que era un tema complejo]

#It’s based on the epoch time, which is the number of seconds that have passed since 01.01.1970.

#Módulo time
# Basado en epoch time: tiempo en segundos transcurridos desde 01/01/1970.

# Funciones importantes:
#     * time.time() → devuelve los segundos transcurridos desde la época. Útil para medir cuánto tarda un código en ejecutarse.
#     * time.sleep(segundos) → pausa el programa durante los segundos indicados.

#Ejemplo de uso:

import time

before = time.time()
long_number = 1000**1000  #le pido este cálculo... a ver cuanto tarda?
after = time.time()
print(f"Tardó {after - before} segundos")     #Tardó 4.220008850097656e-05 segundos
time.sleep(2)  # pausa 2 segundos

print(time.time())  #1769440590.2569373 segundos desde 1/1/1970


#Modulo Datetime
# Más avanzado, maneja fechas y horas humanas y zonas horarias.
# Objetos principales:
# date → solo fecha
# datetime → fecha y hora

# Obtener fecha/hora actual:
# datetime.date.today() → fecha de hoy
# datetime.datetime.now() → fecha y hora actuales

# Se puede sumar tiempo usando datetime.timedelta (días, horas, minutos, segundos).

# Formatear fechas:
# strftime() → de fecha a string con formato
# strptime() → de string a fecha según formato

# Ejemplo de uso:

import datetime

today_date = datetime.date.today()   #fecha de hoy
actual_datetime = datetime.datetime.now()  #fecha y hora actuales = now
in_15_hours = actual_datetime + datetime.timedelta(hours=15, minutes=10)   #future

print(f"Today is the {today_date.day}/{today_date.month}")   #Today is the 26/1
print(f"In 15 hours and 10 minutes it will be the {in_15_hours.day}/{in_15_hours.month}") 
 #In 15 hours and 10 minutes it will be the 27/1
print(in_15_hours)  #2026-01-27 08:36:02.575262


print(datetime.date.today())  #2026-01-26
print(datetime.datetime.today()) #2026-01-26 17:26:02.575841  formato yyyy-mm-dd hh:mm:ss.decimas de segundo
print(datetime.datetime.now())  #2026-01-26 17:26:02.575841
print(today_date.strftime("%d/%m"))   #26/01

# Convertir string a fecha
string_date = "10/09/2020"
dt = datetime.datetime.strptime(string_date, "%d/%m/%Y")
print(dt)   #2020-09-10 00:00:00


print(datetime.date.today().weekday())  #0 es lunes
    # Lunes → 0
    # Martes → 1
    # Miércoles → 2
    # Jueves → 3
    # Viernes → 4
    # Sábado → 5
    # Domingo → 6

# Obtener el número del día de la semana
today_weekday_number = datetime.date.today().weekday()  # 0 = lunes, 6 = domingo

# Lista con los nombres de los días
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Obtener el nombre
today_name = days[today_weekday_number]

print(f"Hoy es {today_name}")  # Hoy es Monday


#Exercise
#Try to create a countdown to your birthday !
#For example : "My birthday is in 45 days, and 10:29:46"
#LO RESPONDO CON CHATGTP, primero más simple y luego con funciones

import datetime

# Fecha de hoy
now = datetime.datetime.now()

# Próximo cumpleaños (este año)
birthday = datetime.datetime(now.year, 10, 24, 0, 0, 0)

# Si ya pasó este año, usar el próximo año
if now > birthday:
    birthday = datetime.datetime(now.year + 1, 10, 24, 0, 0, 0)

# Diferencia
time_left = birthday - now

# Extraer días, horas, minutos, segundos
days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Tu cumpleaños es en {days} días, {hours} horas, {minutes} minutos y {seconds} segundos 🎉")
#output: Tu cumpleaños es en 270 días, 6 horas, 18 minutos y 41 segundos 🎉


#con funciones, Ventajas:
# Reutilizable: Podés usarla para cualquier cumpleaños u otra fecha sin reescribir el código.
# Limpia y organizada: Toda la lógica está en un solo lugar, el resto del código solo llama a la función.
# Escalable: Si querés agregar horas exactas, mensajes personalizados o incluso hacerla en tiempo real, es mucho más fácil.
# Legible: Para vos o cualquier otra persona que lea tu código, queda más claro qué hace cada parte.

import datetime

def tiempo_hasta_cumple(dia, mes):
    """Calcula el tiempo restante hasta el próximo cumpleaños dado día y mes"""
    ahora = datetime.datetime.now()
    # Próximo cumpleaños
    cumple = datetime.datetime(ahora.year, mes, dia)
    if ahora > cumple:  # Si ya pasó este año, usar el próximo
        cumple = datetime.datetime(ahora.year + 1, mes, dia)
    
    diferencia = cumple - ahora

    # Extraer días, horas, minutos, segundos
    dias = diferencia.days
    horas, resto = divmod(diferencia.seconds, 3600)
    minutos, segundos = divmod(resto, 60)

    return dias, horas, minutos, segundos

# Uso
dia, mes = 24, 10  # 24 de octubre
dias, horas, minutos, segundos = tiempo_hasta_cumple(dia, mes)

print(f"Tu cumpleaños es en {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos 🎉")
#Tu cumpleaños es en 270 días, 6 horas, 17 minutos y 17 segundos 🎉


