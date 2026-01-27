class PlayerCharacter:
    #class object attribute, igual para todos los objetos (no dinámico)
    membesrship = True   
    
    def __init__(self, name='anonymus', age=0):   #CONSTRUCTOR INSTANCE, puedo definir parametros defaults
        if (age > 18):  #filtro que solo se puedan crear mayores de edad
            self.name = name   #atributos "unicos" para el objeto
            self.age = age

    def presentation(self):
        print(f'my name is {self.name} and I have {self.age}!')  #uso el self xq varia de instancia en instancia
    
    def self(self):  #self refiere a PlayerCharacter
        return self
    
player1 = PlayerCharacter('Coco', 30)  #CREO UNA INSTANCIA, EL OBJETO
player2 = PlayerCharacter('Tom', 45) 
player2.attack = 50   #creo un atributo desde el objeto-instancia
player5 = PlayerCharacter('Andrei', 60)

print(player1)   #<__main__.PlayerCharacter object at 0x0000025170F986E0> --> esta instancia vive en este lugar de la memoria

print(player1.name)   #Coco
print(player2.age)   #45
player2.presentation() #my name is Tom and I have 45! -->> sin print, ya lo tiene incluido
print(player5.self())  #<__main__.PlayerCharacter object at 0x0000020315D78B90> --> esta instancia vive en este lugar de la memoria

print(player1.membesrship) #True  p/ todas las instancias, x eso aca no se usa el self 
print(player2.membesrship)  #True

attributes = player2.__dict__   #para ver todos los atributos que tiene esta instancia
print(attributes)  # {'name': 'Tom', 'age': 45, 'attack': 50}


#instancias que no pasaron el filtro y no fueron creadas
#player3 = PlayerCharacter()  #tomo los valores default, pero como edad 0 < 18 (filtro) no existe
#player4 = PlayerCharacter('Cindy', 15)  # como edad 15 < 18 (filtro) no existe

#attributes = player3.__dict__   #para ver todos los atributos que tiene esta instancia
#print(attributes)  # {} xq tiene 0 años x default, x tanto no permite ser creado

#print(player4.shout()) #PlayerCharacter' object has no attribute 'name', no se creo xq tiene 15 años


#aca solo se esta hablando de los metodos, no hay init => como se crea la instancia?
class Calc:

    def sum(x,y):
        answer = x + y
        print(answer)
    
    def rest(x,y):
        answer = x - y
        print(answer)
    
    def multi(x,y):
        answer = x * y
        print(answer)
    
    def divi(x,y):
        answer = x / y
        print(answer)

my_sum = Calc.sum(10,2)  #12
my_rest = Calc.rest(10,2)  #8
my_multi =Calc.multi(10,2)  #20
my_div =Calc.divi(10,2)  #5
print(my_sum)  #None  --> my_sum no es isntancia ??
print(type(my_sum))  # <class 'NoneType'>
print(dir(my_sum))
#['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__'] 



class Shape:
  sides = 4 #first property
  name = "Square" #second property
  
  def description(a): #method defined
    return ("A square with 4 sides")

s1 = Shape() #creating an object of Shape
print( "Name of shape is:",(s1.name))    #Name of shape is: Square
print ("Number of sides are:",(s1.sides))  #Number of sides are: 4
print (s1.description())  #A square with 4 sides

'''The class Shape has the following properties: sides  name
and the following method:  description
the argument passed to the method is the word 'self', which is a reference to objects that are made based on this class.
To reference the instance of the class, self will always be the first parameter.'''