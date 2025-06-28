#Question 5.1: (Revisit) Create a base class Shape with a method draw(). Create subclasses Circle and Square, 
# both overriding draw() to print "Drawing a Circle" and "Drawing a Square" respectively. 
# Create a list of Shape objects (containing both Circle and Square instances) and iterate through it, calling draw() on each. 

class Shape:
    def __init__(self):
        pass
    def draw(self):
        print(" Shape")
class Circle(Shape):
    def __init__(self):
        pass
    def draw(self):
        print("Drawing a Circle")
class Square(Shape):
    def __init__(self):
        pass
    def draw(self):
        print("Drawing a Square")


shapes = [Circle(), Square(), Circle(), Square()]
for shape in shapes:
    shape.draw()
print("---------------------\n")



#q 5.2: Define a Printer base class with a print_document(doc) method. Create subclasses LaserPrinter and InkjetPrinter.
#  Override print_document in each to simulate different printing behaviors (e.g., "Laser printing..." vs. "Inkjet printing..."). 
# Demonstrate by putting instances in a list and calling the method. 

class Printer:
    def __init__(self):
        pass
    def print_doucment(self,doc):
        print(f"Printing document: {doc}")
class LaserPrinter(Printer):
    def __init__(self):
        pass
    def print_doucment(self, doc):
        print(f"Laser printing: {doc}")
class InkjetPrinter(Printer):
    def __init__(self):
        pass
    def print_doucment(self, doc):
        print(f"Inkjet printing: {doc}")

printers = [LaserPrinter(), InkjetPrinter(), LaserPrinter()]
for printer in printers:
    printer.print_doucment("Sample Document")
print("---------------------\n")                        


#q 5.3: Create a base class PaymentMethod with a method process_payment(amount). Create subclasses CreditCardPayment, PayPalPayment,
#  and CashPayment. Override process_payment in each to simulate specific payment processing steps. 
class PaymentMethod:
    def __init__(self):
        pass
    def process_payment(self, amount):
        print(f"Processing payment of {amount} using generic method.")
class CreditCardPayment(PaymentMethod):
    def __init__(self):
        pass
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}.")
class PayPalPayment(PaymentMethod):
    def __init__(self):
        pass
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}.")              
class CashPayment(PaymentMethod):
    def __init__(self):
        pass
    def process_payment(self, amount):
        print(f"Processing cash payment of {amount}.")


payment_methods = [CreditCardPayment(), PayPalPayment(), CashPayment()]
for payment_method in payment_methods:
    payment_method.process_payment(100.00)
print("---------------------\n")


#Question 5.4: Create two unrelated classes, Robot with a perform_action() method and Human with a perform_action() method.
#  The Robot's method should print "Robot is performing a task," and the Human's should print "Human is performing an activity."
#  Create a list containing instances of both Robot and Human and call perform_action() on each, demonstrating polymorphism through "duck typing." 

class Robot:
    def __init__(self):
        pass
    def perform_action(self):
        print("Robot is performing a task.")
class Human:
    def __init__(self):
        pass
    def perform_action(self):
        print("Human is performing an activity.")

entities = [Robot(), Human(), Robot()]
for entity in entities:
    entity.perform_action()
print("---------------------\n")


#q5.5 Define a function process_items(items_list) that iterates through a list. Each item in the list is expected to have a process() method.
#  Create two distinct classes, FileProcessor and DataAnalyzer, each with a process() method that does something different.
#  Demonstrate process_items working with a list containing instances of both. 

class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
    def process(self):
        print(f"Processing file: {self.filename}")
class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    def process(self):
        print(f"Analyzing data: {self.data}")

def process_items(items_list):
    for item in items_list:
        item.process()

items = [FileProcessor("file1.txt"), DataAnalyzer("data1"), FileProcessor("file2.txt"), DataAnalyzer("data2")]
process_items(items)
print("---------------------\n")

#q 5.6: Create a Notifier function that takes an object and calls its send_notification() method. 
# Then, create two classes EmailSender and SMSSender, both having a send_notification() method (with different implementations). 
# Show how Notifier can work with either. 

class EmailSender:
    def __init__(self, email):
        self.email = email
    def send_notification(self):
        print("email notification  ")

class SMSSender:
    def __init__(self, phone_number):
        self.phone_number = phone_number
    def send_notification(self):
        print("Sending SMS notification ")

def Notifier(notification_sender):
    notification_sender.send_notification()

items= [EmailSender("jdkd"),SMSSender("123")]
for item in items:
    Notifier(item)
print("---------------------\n")

#q 5.7: Create a Vector class with x and y coordinates. Override the __add__ operator so that two Vector objects can be added together, 
#resulting in a new Vector object where x and y coordinates are summed independently. 

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return self.x+other.x, self.y+other.y
    
v1= Vector(3, 4)
v2= Vector(1, 2)
v3 = v1 + v2
print(f"Resultant Vector: x={v3[0]}, y={v3[1]}")
print("---------------------\n")

#q5.8: For the Book class (from Q4.2), override the __len__ method to return the length of the book's title. 

class Book:
    def __init__(self,title):
        self.title = title
        
    def __len__(self):
        return len(self.title)

b1 = Book("amaar khan the grear")
print(f"Length of the book title '{b1.title}': {len(b1)}")
print("---------------------\n")    


#    5.9: Create a Money class with an amount attribute. 
# Override the __eq__ (equality) operator to compare two Money objects based on their amount.

class Money:
    def __init__ (self,amount):
        self.amount=amount
    def __eq__(self,another):
        return self.amount == another.amount

m1 = Money(100)
m2 = Money(100)

if(m1 == m2):
    print("Both Money objects are equal."   )
