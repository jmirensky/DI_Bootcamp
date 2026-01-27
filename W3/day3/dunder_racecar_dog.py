# --------------------------------------------------
# Clase Racecar
# --------------------------------------------------

class Racecar():
    '''amos un objeto Racecar'''
    def __init__(self, model, reg_no, top_speed=0, nitros=False):
        self.model = model         # Nombre del modelo
        self.reg_no = reg_no       # Número de registro del auto
        self.top_speed = top_speed # Velocidad máxima (default 0)
        self.nitros = nitros       # Booleano: tiene nitros o no

        # Si el auto tiene nitros, le sumamos 50 a la velocidad máxima
        if self.nitros:
            self.top_speed += 50
    
    # Método para mostrar el objeto con print()
    def __str__(self):
        return self.model.capitalize()   # Imprime el modelo con mayúscula inicial

    # Método para la representación "oficial" del objeto
    def __repr__(self):
        return f"This is a Racecar with registration: {self.reg_no}"
    
    # Permite llamar al objeto como función: car()
    def __call__(self):
        print(f"Vroom Vroom. The {self.model} Engines Started")

    # Permite comparar dos autos usando > (mayor velocidad)
    def __gt__(self, other):
        if self.top_speed > other.top_speed:
            return True
        else:
            return False
    
    # Método para simular conducir cierta distancia
    def drive(self, km):
        print(f"You drove the {self.model} {km} km in {km / self.top_speed} hours.")

    # Método para competir contra otro auto
    def race(self, other_car):
        if self > other_car:
            print(f"I am {self.model} and am the winner")
        else:
            print(f"The {other_car.model} is the winner")


# --------------------------------------------------
'''Cada método mágico (__init__, __str__, __repr__, __call__, __gt__) 
sirve para que el objeto se comporte de manera natural en Python.'''

'''Los métodos normales (drive, race) hacen acciones específicas con los atributos del objeto.'''

# Creamos dos autos de carrera
car1 = Racecar("ferrari", "F123", top_speed=200, nitros=True)
car2 = Racecar("lambo", "L456", top_speed=220, nitros=False)

# Imprimimos el modelo (str) y la representación oficial (repr)
print(car1) # Ferrari
print(repr(car1)) # This is a Racecar with registration: F123

# Llamamos al objeto como función para "arrancar el motor"
car1() # Vroom Vroom. The ferrari Engines Started

# Comparamos velocidades
print(car1 > car2) # True según top_speed

# Simulamos conducir
car1.drive(100) # You drove the ferrari 100 km in 0.4 hours..

# Hacemos una carrera entre dos autos
car1.race(car2) # I am ferrari and am the winner
car2.race(car1)  #The ferrari is the winner





# --------------------------------------------------
# Clase Dog
# --------------------------------------------------

from random import choice, randint
class Dog:

    def __init__(self, name, age, weight, breed, gender):
        self.name = name    #nombre del perro
        self.age = age      #edad
        self.weight = weight #peso
        self.breed = breed  #raza
        self.gender = gender #M" o "F"

    def __str__(self):
        return "I'm a DOG called " + self.name    #define cómo se ve el perro cuando lo imprimes.

    def __repr__(self):
        return f"Dog: name = {self.name}"        #define cómo se representa el objeto en la consola o listas.

    def __len__(self):                          #devuelve un número basado en el peso.
        if self.breed == "dachshund":
            return self.weight * 5
        else:
            return self.weight * 3

    def __gt__(self, other):
        return "All dogs are created equal"    #> (mayor que) no compara nada realmente, solo devuelve un string divertido.

    def __ge__(self, other):
        return self.age >= other.age       # >= sí compara la edad de los perros.

    def __add__(self, other):             #+ intenta “cruzar” dos perros:
        if self.gender == other.gender:
            return None                    #Si son del mismo género → no se puede → devuelve None
        if self.breed != other.breed:
            breed = self.breed + "-" + other.breed       #Si son de diferente raza → mezcla nombres de raza
        else:
            breed = self.breed            
       #Genera 1 a 6 cachorros, con:
       #Nombre "Puppy 1", "Puppy 2", etc.
       #Edad 0
       # Peso promedio reducido (self.weight + other.weight)/20
       # Raza combinada
       # Género aleatorio
        age = 0
        weight = (self.weight + other.weight)/20
        return [Dog(f"Puppy {i+1}", age, weight, breed, choice(["M", "F"])) for i in range(randint(1, 6))]

    def __mul__(self, other):
        return self.__add__(other)    #hace lo mismo que +. Solo es un alias.
    
 

# Crear dos perros
fido = Dog("Fido", 4, 20, "labrador", "M")   
bella = Dog("Bella", 3, 18, "beagle", "F")

# Imprimir
print(fido)       # I'm a DOG called Fido      __str__(
print(repr(bella))# Dog: name = Bella         __repr__

# Longitud
print(len(fido))  # 20*3 = 60

# Comparaciones
print(fido > bella)   # All dogs are created equal     __gt__
print(fido >= bella)  # True, porque 4 >= 3            __ge__

# Cruzar perros
puppies = fido + bella
for puppy in puppies:
    print(puppy)
# Salida ejemplo:
# I'm a DOG called Puppy 1
# I'm a DOG called Puppy 2
# ... (1 a 6 cachorros)
