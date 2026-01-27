#Exercise1: Currencies

class Currency:
    def __init__(self, currency, amount):
        # currency: type of currency ("dollar", "shekel", etc.)
        # amount: amount of money
        self.currency = currency
        self.amount = amount


    def __str__(self):  
        # Defines what is shown when we use print(object)
        return f"{self.amount} {self.currency}s"


    def __repr__(self):
        # Object representation (useful for debugging and development)
        # We use the same representation as __str__
        return self.__str__()


    def __int__(self):
        # Allows the object to be converted to an integer
        return self.amount


    def __add__(self, other):  
        # Handles object + something
        # This method DOES NOT modify the object, it only returns a result

        # Currency + integer
        if isinstance(other, int):
            return self.amount + other

        # Currency + Currency
        if isinstance(other, Currency):
            #If currencies are different, raise an error
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            #If currencies are the same, add the amounts
            return self.amount + other.amount
             
        return NotImplemented

    def __iadd__(self, other):
        # Handles object += something
        # This method DOES modify the object
        
        # Currency += integer
        if isinstance(other, int):
            self.amount += other  #is added within self.amount
            return self

        # Currency += Currency
        if isinstance(other, Currency):
            #If currencies are different, raise an error
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            #If currencies are the same, add the amounts
            self.amount += other.amount   #is added within self.amount
            return self

        return NotImplemented

# Creating instances and invoking dunder methods

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)

print(c1)     #5 dollars
print(int(c2))  #10
print(repr(c3))  # 1 shekels

print(c1 + 5)      # 10
print(c1 + c2)     # 15
#print(c1 + c3)     # TypeError: Cannot add between Currency type <dollar> and <shekel>

c1 += 5
print(c1)          # 10 dollars

c1 += c2
print(c1)          # 20 dollars => (5 + 5) + 10 = 20