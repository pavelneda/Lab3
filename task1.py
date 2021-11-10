

class Ticket:
    def __init__(self,name_surname,number,price):
        self.name_surname=name_surname
        self.number=number
        self.price=price
    def __str__(self):
        return f'self.__class__.__name__\n'
        
    def getprice(self):
        return self.price
    
    
class Advance_ticket(Ticket):
    def __init__(self,name_surname,number,price):
        super().__init__(name_surname,number,price*0.4)
    
    
class Student_ticket(Ticket):
    def __init__(self,name_surname,number,price):
        super().__init__(name_surname,number,price*0.5)
    
    
class Late_ticket(Ticket):
    def __init__(self,name_surname,number,price):
        super().__init__(name_surname,number,price*1.1)
    
    
a=Advance_ticket("Abob",12412,100)
print(a)