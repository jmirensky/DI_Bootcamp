#W3 D1 30 Dic 25
#intro

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def intro(self):
        return f'Hello there, my name is {self.name}'
    
    def age(self):     #age se recalcula constantmente, x eso no se guarda estatica como variable/atributo sino como metodo
        return 2026 - self.birth_year
    
joel = Person('Joel', 1991)  #ingreso un objeto a la clase    
print(joel.name)   #Joel --> es atributo, no lo llamo entre paréntesis
print(joel.intro())  #Hello there, my name is Joel   con paréntesis xq es 1 método!
print(joel.age())   # 35   con paréntesis xq es 1 método!

#no entiendo para que seria esto, dijo que como alias (creo)
class Person2:
    def greetings(self):   
        print('Helloooo')
me = Person2
rabea = me()   #crea el objeto no dese el init....
rabea.greetings()

# -------------------------

#4 pilares de OOP: Encapsulation, abstracción, Inheritance, Polymorphism

# Encapsulation (Encapsulamiento)
# Es la unión de datos y funciones [atributos y métodos] que los manipulan.
#Encapsular en un solo objeto para mantenerlo en "una caja" con la que podamos interactuar.
# Sirve para: evitar errores - mantener el control - acercarnos a la representacion del mundo real

# abstracción = significa ocultar o abstraer información y dar acceso solo a lo necesario.
# => no es preciso conocer la lógica completa de cómo funciona algo, solo usarla:
# un telefono celular, una máquina de cafe,etc
#Si intentamos comprender cada detalle, podremos enloquecer.
# Solo necesitamos un método o un atributo y acceder a él sin tener que preocuparnos por cómo se implementa...

# Inheritance (Herencia) 
# Una clase puede heredar cosas de otra.
# Animal → sabe comer y dormir
# Dog → es un Animal, pero además ladra. El perro hereda lo básico y agrega o cambia lo suyo.
# Sirve para: reutilizar código - ordenar ideas

# Polymorphism (Polimorfismo) = muchas formas
# La misma acción, con el mismo puede comportarse distinto según el objeto, segun a la clase que pertenece.
# Todos los animales hacen “sonido”, cada uno lo hace diferente: dog.sound() → guau - cat.sound() → miau
# Sirve para: escribir código flexible - no llenar todo de if

# -------------------------

#herencia
#adquirir rasgos o caracteristicas de tus "padres"
#tambien se puede adquirir atributos y métodos propias x fuera de las heredadas

#herencia = Inheritance --> mecanismo mediante el cual una clase adquiere, adopta, hereda, reusa los atributos y métodos de otra.
#    * clase hija/derivada  = la recién formada, ej Perro --> todo Perro es un Animal
#    * clase padre/base = de la que se deriva la clase hija, ej Animal --> no todo Animal es un Perro

#Beneficios
# Reutilización del código y escabilidad
#  clase hija:  hereda atributos y métodos de la clase padre, pero también puede tener método y caracteristicas propias.

# Código estructurado --> Al dividir el código en clases, podemos estructurar mejor nuestro software, 
# dividiendo la funcionalidad en clases.

class Animal:    #original , clase padre
    def __init__(self, name):
        self.name = name

class Dog(Animal):   #hereda todo de Animal, clase hija = padre entre paréntesis en la definición de la clase.
    
    #no necesita el init
    def bark(self):
        print(f"{self.name} barked, WAF !")

my_dog = Dog('Peanut')   
print(my_dog.name)    #Peanut,               name lo heredó de Animal.
my_dog.bark()         #Peanut barked, WAF !   bark() es propio de Dog.


class Animal:   #clase padre
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):  #clase hija
    def fetch_ball(self):
        print(f"I am a {self.type} and I love fetching balls")

rex= Dog("dog", 4, "wouaf")   #objeto rex Dog que usa el método y atributos de la clase Animal (padre)

print('This animal is a:', rex.type)  # hereda del papa
# >> This animal is a dog

print(f'This {rex.type} has {rex.number_legs} legs')  # hereda del papa
# >> This dog has 4 legs

print(f'This {rex.type} makes the sound {rex.sound}')  # hereda del papa
# >> This dog makes the sound wouaf

rex.make_sound()    # hereda del papa
# >> I am an animal, and I love saying wouaf   

rex.fetch_ball()  #método de la clase hija
# >> I am a dog, and I love fetching balls

roger = Animal('cat', 4, "miau")  #creado como animal, no como perro
#roger.fetch_ball()   #método de la clase hija, no lo puede hacer
# >> AttributeError: 'Animal' object has no attribute 'fetch_ball'

  
#Exercise - #Analyse the code below before executing it. What will be the output ?
class Circle:
    def __init__(self):
        self.color = "red"

class NewCircle(Circle):  #lo hereda
     def __init__(self):             #deberia haber un super() 
        self.color = "blue"

nc = NewCircle()
print(nc.color)    #blue, xq el objeto se creo dentro de clase NewCircle

#NO DEBERIA HABER INIT sin super() EN EL HIJO! LOS COLORES DEBERIAN reemplazarse o con super o con METODOS
#es solo un ejemplo diáctico --> # “Funciona sin super(), pero no es una buena práctica porque rompe la herencia 
# si la clase padre cambia: # ej si se le agrega diametro el hijo no lo hereda.”

class Circle:
    def __init__(self, diameter):
      self.diameter = diameter

    def grow(self, factor=2):
        """grows the circle's diameter x factor"""
        self.diameter = self.diameter * factor

class NewCircle(Circle):                #lo hereda y pisa el metodo grow
    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = (self.diameter * factor * 2)

nc = NewCircle(1)  #desde el hijo
print(nc.diameter)   #1
nc.grow()
print(nc.diameter)   #4  (1*2*2)

c = Circle(1)  #desde el padre
print(c.diameter)   #1
c.grow()     
print(c.diameter)   #2  (1*2)


#Overriding Parent Methods 
# si se repite el mismo método en clase padre y clase hija, "gana" la clase hija, sobrescribe el método de clase padre.

class Animal:
    def __init__(self, type, number_legs, sound):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):    #se repite make sound = se sobreescribe esta
        print(f"I am an animal, and I love saying {self.sound}")

class Dog(Animal):
    def fetch_ball(self):
        print("I am a dog, and I love fetching balls")

    def make_sound(self):    #se repite make sound = gana esta
        print("I am an DOGGG !!! WOUAFFF!!")

rex = Dog('dog', 4, "Wouaf")
rex.make_sound()
# >> I am an DOGGG !!! WOUAFFF!!   gana el metodo detallado en Dog
rex.fetch_ball()  #metodo propio de Dog
# >> I am a dog, and I love fetching balls
#ojo lo opuesto no sucede, x ej creo un caballo desde clase Animal y le quiero aplicar el metodo fetch_ball = ERROR!

# las clases hijas anulan y amplían la funcionalidad de las clases madre. 
# Tendran las funciones de la clase madre, + sus funciones.


#The super() Function => desde el init y desde los metodos
#se usa para EXTENDER un comportamiento(metodo, acción). No para reemplazar o pisar.

#super() significa “andá a buscar esto a la clase padre”.
                    #“Primero hacé lo que hace el padre al nacer, después agrego lo mío.”

#The super() Function => desde el constructor (__init__)
# Mantiene una jerarquía limpia y no se repite código
#super().__init__ llama al constructor de la clase padre (Animal) desde la clase hija (Dog).
#Para que lo 'basico' lo tome del papa, y desde el hijo lo especifico, lo de nicho.
# El padre inicializa atributos importantes
# No querés repetir código
# Querés extender, no reemplazar

class Animal:
    def __init__(self, type, number_legs, sound):
        self.type = type     #basic
        self.number_legs = number_legs  #basic
        self.sound = sound  #basic
    
    def sleep(self):
        return 'animal sleeps outsisde...'

class Dog(Animal):
    def __init__(self, type, number_legs, sound, fetch_ball): 
         #en comun = type, number_legs, sound,      específico = fetch_ball
        super().__init__(type, number_legs, sound) 
        #xq super() desde el constructor (__init__) 
            # para poder acceder a lo basico desde el papa        
            # el perro nace siendo un animal válido, con todo lo que ya tienen los animales
            # Inicializa atributos, Evita repetir código, es estructural
        self.fetch_ball = fetch_ball   #especifico
        
rex = Dog('dog', 4, "wouaf", True)
print('This animal is a:', rex.type)    #This animal is a dog
print('This dog has', rex.number_legs , ' legs')   #This dog has 4  legs
print('This dog makes the sound ', rex.sound)   # This dog makes the sound wouaf
print(rex.sleep())  #animal sleeps outsisde...

print('Does this dog fetchs balls ? ', rex.fetch_ball)   #Does this dog fetchs balls ? True


#super() en los metodos = acceso, uso, extension a los métodos del papa, sin sobresescrbir/pisar/ignorar lo

class MyClass:        #clase padre
    def func(self):
        print("I'm talking like a Parent class")

class ChildClass(MyClass):   #clase hija
    def func(self):          #se pisa (override) el método del padre, func. Manda la hija... PERO...
        print("I'm actually taking like a Child class")
        print("But too...")
        # Calling the `func()` method from the Parent class... No lo sobreescribe! NO QUEDA IGNORADO
        super().func()    #al llamar a func(), usa lo de el padre 
         #super(ChildClass, self).func()   #es lo mismo q el renglon de arriba

my_instance_2 = ChildClass()  #instancia de la clase hija
my_instance_2.func()  #Se llama a func()
# I'm actually taking like a Child class           # la clase hija hace algo propio
# But too...
# I'm talking like a Parent class                # Luego ejecuta lo que hace el padre

#en sintesis:
# super() en __init__ → heredás estado
# super() en métodos → heredás comportamiento
# Sin super() → estás reemplazando, no heredando
# el hijo puede agregar cosas… pero no finge que no tiene padre 


class Cat(Animal):
    def __init__(self, type, number_legs, sound, hs_of_sleep):
          #en comun = type, number_legs, sound,      específico = hs_of_sleep
        super().__init__(type, number_legs, sound)
        self.hs_of_sleep = hs_of_sleep    #especifico

    def sleep(self): 
        base_msg = super().sleep()  #us super para que no se reescriba el metodo del papa animal
        return (f'{base_msg} but this cat like to sleep on the coach')  #actualiza el resultado

katy = Cat('cat', 4, "grrrr", 16)
print('How much it sleeps ? ', katy.hs_of_sleep)   #how much it sleeps ?  16
print(katy.sleep())  #animal sleeps outsisde... but this cat like to sleep on the coach

print(dir(katy))  #dir me da la INTRPOSPECCION de ese objeto, es decir todos los metodos que tiene.
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', 
# '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
#  '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__',
#  'hs_of_sleep', 'number_legs', 'sleep', 'sound', 'type']

print(dir('hi'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__',
#  'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
#  'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print(dir(5))
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', 
#  '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', 
#  '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', 
#  '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__',
#  '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', 
#  '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', 
# '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 
# 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']

print(dir(True))
#['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', 
# '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
# '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', 
# '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', 
# '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', 
# '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', 
# '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 
# '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 
# 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']


#Exercise  #What is the difference between these 2 pieces of code ?   RTA CHAT GTP
class B:  #papa
    pass

class A(B):  #hija que hereda del papa
    def __init__(self, *args, **kwargs):
        B.__init__(self, *args, **kwargs)   #B.__init__   Llamada directa al padre, pero a una clase específica
        pass
# Problemas
# Rompe herencia múltiple
# se salta el orden correcto de inicialización
# Si mañana hay otra clase entre medio → explota
# No coopera con otras clases
# Funciona solo si:
    # Hay un solo padre
    # La jerarquía es simple
    # Estás seguro de que nunca va a crecer

class A(B):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   #super().__init__   llama al diseño de la jerarquía
                                            #Llamá al siguiente método según el orden de herencia
        pass
# este es el correcto
# Funciona con herencia simple y múltiple
# Respeta el orden correcto (MRO)
# Es extensible
# Es la forma moderna y recomendada
# No llama “al padre directo”, llama al próximo en la cadena.


#Exercise on Inheritance and Composition: Door class JULIANA DIJO QUE ESTE EJERCICIO NO EXPLICA BIEN HERENCIA

#We have a class called Door that has an attribute of is_opened declared when an instance is initiated.
    # Una clase Door
    # Un atributo is_opened al crear la instancia

#We can create a class called BlockedDoor that inherits from the base class Door.
#We just override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those
#  functions, which simply raises an Error that a blocked door cannot be opened or closed.

# Clase base: puerta normal
class Door:             
    def __init__(self):
        self.is_opened = False  # inicializa una puerta cerrada x default
    
    def open_door(self):
        self.is_opened = True    #puerta abierta
        print("The door is now open.")

    def close_door(self):
        self.is_opened = False    #puerta cerrada
        print("The door is now closed.")


# Clase hija: puerta bloqueada hereda de Door, pero pisa el comportamiento: 
# no es posible abrir ni cerrar una puerta que está bloqueada, advierte cuando se intenta
class BlockedDoor (Door):     
    def __init__(self):       
        super().__init__()    # inicializa como una Door normal, cerrada
    
    def open_door(self):    #pisa el metodo
        # muestra advertencia pero no detiene la acción
        return "Cannot open the door!"

    def close_door(self):  #pisa el metodo
        # muestra advertencia pero no detiene la acción
       return "The door is permanantly closed!"

# Puerta normal
door1 = Door()
door1.open_door()   #The door is now open.
door1.close_door()  #The door is now closed.

# Puerta bloqueada
door2 = BlockedDoor()
print(door2.open_door())  #Cannot open the door!
print(door2.close_door())  #The door is permanantly closed!


# Privacidad --> #Restringir el acceso a métodos y variables. 
# Para impedir que los datos se modifiquen directamente, fuera de la clase.
#Se denota usando underscore como prefijo (simple ._  o dobles .___)

class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public attribute
        self.__max_price = 900   # private  attribute

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price): 
        #custom function, estoy dentro de la clase, si puedo hacer referencia a un atributo privado 
        # y usarlo como referencia para otra cosa
        self.__max_price = price   # private  attribute  ??

c = Computer()
print(c.name)  #Apple Computer
c.sell()   #Selling Price: 900   --> El atributo es privado, pero se muestra mediante el método público.

#c.__sell()    #AttributeError: 'Computer' object has no attribute '__sell'  # private 
# El intérprete no puede realizar la función debido al guion, significa que es privada y no puede ser accedida por el usuario

c.__max_price = 1000
c.sell()
# >> The private attribute __max_price cannot be changed  # if tis private = not possible
# >> Selling Price: 900

# using setter function
c.set_max_price(1000)
c.sell()
# >> Selling Price: 1000


#II. Polymorphism = muchas formas ante 1 mismo comando u orden
# 2 clases diferentes, que usan los mismos nombres para sus funciones. Cada una hara algo distinto
# EJ: comando: ¡habla!  --> respuesta: ladrido_perro, maullido_gato, graznido_ave, mugido_vaca

class Parrot():  #loro
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")

class Penguin():
    def fly(self):
        print("Penguin can't fly")
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):  #para testear que ave puede volar
    bird.fly()
def swimming_test(bird):  #para testear que ave puede nadar
    bird.swim()

#instantiate objects & passing the object
blu = Parrot()
peggy = Penguin()

flying_test(blu)   # >> Parrot can fly
flying_test(peggy)  # >> Penguin can't fly
swimming_test(blu)   # >> Parrot can't swim
swimming_test(peggy)  # >> Penguin can swim



#III. Multiple Inheritance (Herencia múltiple) = la 2°
# Una clase puede heredar de más de una clase. Como aprender de más de un maestro.
# Smartphone hereda de: Phone y de Computer
# Ojo: es poderosa - también puede ser confusa - se usa con cuidado

# 4 tipos de herencia
# * herencia single o simple = clase derivada se deriva de una sola clase base MAMA - HIJA  / animal - perro
#     class BaseClass:
#       Base class body
#     class DerivedClass(BaseClass):
#       Derived class body
# * herencia multiple = la clase derivada se deriva de más de una clase base. MAMA + PAPA = HIJA  / ej Alien
#     class BaseClass1:
#       Base class1 body
#     class BaseClass2:
#       Base class2 body
#     class DerivedClass(BaseClass1,BaseClass2):
#       Derived class body
# * herencia jerarquica = 2 clases derivadas se derivan de una misa clase base  MAMA - [HIJO1, HIJO2] / animal [perro - gato]
# * herencia multilevel = la clase derivada se deriva de otra clase derivada   ABUELA - MAMA - HIJA
#     class BaseClass:
#       Base Class body
#     class Derived1(Base):
#         Derived Class1 body
#     class Derived2(Derived1):
#         Derived Class2 body 

''' una clase hija () hereda todos los métodos de la clase madre ().
Sin embargo, en algunas situaciones, el método heredado de la clase madre no encaja del todo en la clase hija
En tales casos, tendrás que reimplementar el método en la clase hija'''

class Alien:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def fly(self):
        print(self.name, 'is flying!')

    def sleep(self):
        print("Aliens don't sleep")

class Animal:
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("zzzZZZZZ")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barked, WAF !")

class AlienDog(Alien, Dog):   #AlienDog hereda de dog y de alien, pero prioriza lo alien porque viene primero en la herencia.
    def __init__(self, name, planet):
        super().__init__(name, planet)  #lo toma de Alien
    def bark(self):
        print(f"{self.name} barked, xoxo (that's how aliens dogs bark..) !")  #pisa lo de Dog


my_normal_dog = Dog("Roger")
my_normal_dog.sleep()   # >> zzzZZZZZ  lo trae de Animal
my_normal_dog.bark()  # >> Roger barked, WAF !   lo trae de Dog

my_alien_dog = AlienDog("Rex", "Neptune")

print(AlienDog.mro())   #primero mira a Alien, despues mira a Dog, despues mira a Animal
#[<class '__main__.AlienDog'>, <class '__main__.Alien'>, <class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>]

print(f'{my_alien_dog.name} is cute')     #Rex is cute     lo trae de AlienDog
print(my_alien_dog.planet)  # >> Neptune        lo trae de Alien
my_alien_dog.fly()  # >> Rex is flying!         lo trae de Alien
my_alien_dog.sleep()  # >> Aliens don't sleep   lo trae de Alien, no de Animal
my_alien_dog.bark()  # >> Rex barked, xoxo (that's how aliens dogs bark..) !    lo trae de AlienDog



#conclusion = #cuando tiene 2 padres, el hijo toma el metodo del padre que tiene escrito primero (alien)
#Primera clase que tenga el método, esa se ejecuta. el orden importa.
#herencia múltiple
# AlienDog  --> bark()  = usa este
#  ├── Alien -->  name = usa este   planet  fly()   sleep() = usa este... __init__ aqui
#  │
#  └── Dog --> bark()
#       └── Animal  -->  name   sleep()


#En herencia múltiple, Python sigue el MRO methdo resolution order (orden de resolución de métodos).

#Ejercicio, analizar la salida y explicar pq.
class A():                              #abuela  A
    def dothis(self):
        print("doing this in A")

class B(A):   #B hereda de A          #mama  B
    pass

class C():                             #papa  C
    def dothis(self):
        print("doing this in C")

class D(B, C):    #D hereda de B y C    #hija
    pass

d_instance = D()   #crea la instancia en D
# D → B → A
# ↓
# C     
d_instance.dothis() #doing this in A ... toma primero de A, Primera clase que tenga el método

print(D.mro())  #primero mira a B, despues mira a A, despues mira a C
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]

#Analiza el código que aparece a continuación antes de ejecutarlo. ¿Cuál será la salida? ¿Por qué?

class Book():
    def __init__(self, title, author, publication_date, price):
        #Constructor guarda todos los atributos: title, author, publication, price.
        self.title = title
        self.author = author
        self.publication = publication_date
        self.price = price
    
    #imprime solo el título.
    def present(self):
        print(f'Title: {self.title}')   

class Fiction(Book):  #hereda de Book
    def __init__(self, title, author, publication_date, price, is_awesome):
        #inicializa los atributos de Book.
        super().__init__(title, author, publication_date, price)
        #Agrega genre, is_awesome y bored (como opuesto de is_awesome) con un mensaje.
        self.genre = 'Fiction'
        self.is_awesome = is_awesome
        if self.is_awesome:
            self.bored = False
            print('Woow this is an awesome book')
        else:
            self.bored = True
            print('Boring Book')

if __name__ == '__main__':
    #Se crea un 1° objeto foundation, como is_awesome = True, se imprime el mensaje 'Woow this is an awesome book'
    foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
    foundation.present()  #Llama a present() de Book → imprime el título (self.title):
    print(foundation.price)  #imprime 5£
    print(foundation.bored)  #imprime False
    
    #Se crea un 2° objeto   como is_awesome = False, se imprime el mensaje 'Boring Book'
    boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
    print(boring_book.bored)  #imprime True

        # Woow this is an awesome book
        # Title: Asimov
        # 5£
        # False

        # Boring Book
        # True

