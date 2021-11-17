import time,json,os
from datetime import datetime

ADVANCE_PRICE = 0.6
STUDENT_PRICE = 0.5
LATE_PRICE = 1.1
ADVANCE_DAYS=60
LATE_DAYS=10
class Regular_ticket:   
    def __init__(self, customer, event_name, price, event_date):
        self.ticket_number = self.generate_number()
        self.price = price
        self.event_name = event_name
        self.event_date = event_date
        self.customer = customer
        self.ticket()
        
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
    
    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer
        
    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer
    
    @property
    def event_name(self):
        return self.__event_name

    @event_name.setter
    def event_name(self, event_name):
        self.__event_name = event_name
    
    @property
    def event_date(self):
        return self.__event_date

    @event_date.setter
    def event_date(self, event_date):
        self.__event_date = event_date

    def ticket(self):
        file = open(self.ticket_number + '.json', "w")
        json.dump(self.__dict__, file, indent = 2)
        file.close()

    def get_ticket(file_name):
        if not os.path.exists(file_name + '.json'):
            raise FileNotFoundError
        file = open(file_name + '.json')
        input = json.load(file)
        customer = input["_Regular_ticket__customer"]
        event_name = input['_Regular_ticket__event_name']
        event_date = input['_Regular_ticket__event_date']
        if '_Student_ticket__price' in input:
            price = input['_Student_ticket__price']
        elif '_Late_ticket__price' in input:
            price = input['_Late_ticket__price']
        elif '_Advance_ticket__price' in input:
            price = input['_Advance_ticket__price']
        else:
            price = input['_Regular_ticket__price']
        file.close()
        return f"{file_name}\n{customer}\n{event_name}\nPrice: {round(price)}\n{event_date}"

    def create_ticket(file_name):
        if not os.path.exists(file_name):
            raise FileNotFoundError
        file = open(file_name, "r")
        input = json.load(file)
        customer = input['customer']
        general_price = input['general_price']
        event_name = input['event_name']
        event_date = input['event_date']
        student = False
        if 'student' in input:
            student = input['student']
        file.close()
        return Regular_ticket.generate_ticket(customer, event_name, event_date, general_price, student)

    def generate_ticket(customer, event_name, event_date, general_price, student = False):
        if not isinstance(customer, str) and not isinstance(event_name, str) and not isinstance(event_date, str) and not isinstance(general_price, int) and not isinstance(student, bool):
            raise TypeError("wrong types of data")
        if student:
            return Student_ticket(customer, event_name, general_price, event_date)
        elif Regular_ticket.days_to_event(event_date) > ADVANCE_DAYS:
            return Advance_ticket(customer, event_name, general_price, event_date)
        elif Regular_ticket.days_to_event(event_date) < LATE_DAYS:
            return Late_ticket(customer, event_name, general_price, event_date)
        else:
            return Regular_ticket(customer, event_name, general_price, event_date)
   
    def __str__(self):
        return f"{self.ticket_number}\n{self.customer}\nEvent: {self.event_name}\nPrice: {round(self.price)}"

    def generate_number(self):
        real_time = datetime.now() 
        month = real_time.month
        day = real_time.day
        year = real_time.year
        hour = real_time.hour
        minute = real_time.minute
        second = real_time.second
        mlsec = real_time.microsecond
        time.sleep(0.0025)
        return f"{month}{day}{year}-{hour}{minute}{second}{mlsec}"

    def days_to_event(event_date):
        try:
            first = datetime.now()
            second = datetime.strptime(event_date, "%d.%m.%Y")
        except:
            raise ValueError("Wrong format of date")
        if (second-first).days < 0:
            raise ValueError("Wrong date")
        else:
            return (second - first).days

class Advance_ticket(Regular_ticket):   #derived class
    def __init__(self, customer, event_name, price, event_date):
        super().__init__(customer, event_name, price, event_date)
    @property
    def price(self):
        return self.__price 
    @price.setter
    def price(self, price):
        self.__price = price * ADVANCE_PRICE 

class Late_ticket(Regular_ticket):  #derived class
    def __init__(self, customer, event_name, price, event_date):
        super().__init__(customer, event_name, price, event_date)
    @property
    def price(self):
        return self.__price 
    @price.setter
    def price(self, price):
        self.__price = price * LATE_PRICE

class Student_ticket(Regular_ticket):   #derived class
    def __init__(self, customer, event_name, price, event_date):
        super().__init__(customer, event_name, price, event_date)
    @property
    def price(self):
        return self.__price 
    @price.setter
    def price(self, price):
        self.__price = price * STUDENT_PRICE

print(Regular_ticket.create_ticket("order.json"))
#print(Regular_ticket.get_ticket('11182021-02220265996'))
