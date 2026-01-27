

# DECORATOR   @staticmethod   @classmethod  @property
# DUNDER METHODS  methodos especiales   __func__


from datetime import datetime, date  #importo un modulo y 2 funciones

class Person:

    id_number = 0

    def __init__ (self, name, last_name, birth_date):
        #self.name = name   #omito esto y reformulo... 
        self.name = self.format_name(name)
        self.last_name = self.format_name(last_name)
        #self.birth_date = birth_date  #omito esto y reformulo... 
        #al momento de generarse el objeto, automaticamente transformo su birth_date a formato date
        self.birth_date = self.parse_birthdate(birth_date) 
        Person.id_number +=1

    @staticmethod   #no necesito poner self xq no depende del estado del objeto
    def parse_birthdate (date_str):
        return datetime.strptime(date_str, '%Y-%m-%d').date()  # strptime() → de formato string parse (cambia) a formato fecha
    
    @staticmethod   #no necesito poner self xq no depende del estado del objeto
    #Convierte el string en Capitalize (o lo mantiene)
    def format_name (name):
        if not name[0].isupper():
            return name.capitalize()
        else:
            return name
        

    @classmethod   #se relaciona con la clase! El 1° parametro es la propia clase
    #PERMITE CREAR OBJETOS DE UNA FORMA ALTERNATIVA = constructor alternativo
    # crea un metodo mediante el cual le das la edad y te calcula la fecha de nacimiento 
    def from_age_get_date_birth (cls, name, last_name, age):
        current_year = datetime.today().year
        birth_year = current_year - age
        birth_date = f'{birth_year}-01-01'
        return cls(name, last_name , birth_date)


    @property
     #crear una propiedad o atributo (no incluido en el __init__, me olvide de hacerlo al ppo)
     # usando un metodo
     #automaticamente cada objeto "tendrá" un nuevo atributo que acabo de generar, pero OJO
     #vive en la clase, no en la instancia real
    def age (self):  #SI necesito poner self 
        today = date.today()
        age = today.year - self.birth_date.year
        return age
   
    @property
    def mail (self):  #SI necesito poner self 
        return f"{self.name}.{self.last_name}@westeros.com"


    def __str__(self):        #una linda presentacion cuando hago print del objeto, para el usuario
      return f"Hello!\nName: {self.name}\nlast Name: {self.last_name}\nage: {self.age}" 
     
    def __repr__(self):             #| representation | usefull info for the developer
        return f'{self.__dict__}'               

    def __lt__(self, other):      #comparaciones numericas entre 2 objetos
        return self.age < other.age
    
    def __eq__(self, other):      #comparaciones numericas entre 2 objetos
        return self.age == other.age
    
    def __call__(self):
        return ('Character of ASOIAF')


p1 = Person('sansa', 'stark', '2001-07-29')
p2 = Person('Jon', 'Snow', '1990-04-30')
p3 = Person('Robert', 'Baratheon', '1971-10-14')
print(Person.id_number)  #3, hay 3 personas
print(p1.birth_date)    #2001-07-29 cuando le pregunto su fecha de nacimiento, lo devuelve NO como un string,
                        #sino con formato datetime.date
print(type(p1.birth_date))  #<class 'datetime.date'> 
print(Person.format_name('julieta'))  #Julieta --> funciona para cualquier objeto
print(p1.name) #Sansa

p4= Person.from_age_get_date_birth('arya', 'stark', 14)
print(p4.birth_date)  #2012-01-01
print(type(p4.birth_date))    #<class 'datetime.date'>
print(p4.last_name)  #Stark
print(Person.id_number)  #4, hay 4 personas

print(p3.age)  #55  #age lo recalcula como atributo, pero a partir de un metodo que lleva @property (esta fuera del init)
#vive en la clase, no en la instancia
print(p3.mail)   #Robert.Baratheon@westeros.com  #mail: misma logica que age
print(p3.__dict__)   #{'name': 'Robert', 'last_name': 'Baratheon', 'birth_date': datetime.date(1971, 10, 14)}
print(Person.__dict__['age'])   #<property object at 0x000001FE3F478A90>
print(Person.__dict__['mail'])  #<property object at 0x000001FE3F478C70>

print(p1)        #__str__
# Hello!
# Name: Sansa
# last Name: Stark
# age: 25

print(p1.__repr__)
#{'name': 'Sansa', 'last_name': 'Stark', 'birth_date': datetime.date(2001, 7, 29)}       __repr__

print(p1 < p2)  #True  25 < 36    __lt__

print(p1 == p2)  #False  25 <not = 36    __eq__

print(p4())  #Character of ASOIAF  pongo el objeto y luego () = obtengo acceso a __call__


#seguir aca 
# https://octopus.developers.institute/courses/collection/125/course/503/section/1307/chapter/323 :)
