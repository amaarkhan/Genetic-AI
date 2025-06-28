#q3.1 Question 3.1: Create a base class Animal with an __init__ taking name and sound. Add a method make_sound() 
# that prints the animal's name and sound. Create a subclass Dog that inherits from Animal. Create an instance of Dog and call make_sound(). 

class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} makes a sound: {self.sound}")

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)

d1 = Dog("Buddy", "Woof")
d1.make_sound()
print("---------------------\n")

# q3.2: Define a base class Shape with a method area() that returns 0.
#  Create two subclasses: Rectangle (with length and width) and Circle (with radius).
#  Both subclasses should override the area() method to calculate their specific area. 

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * (self.radius ** 2)

R1 = Rectangle(5, 10)
C1 = Circle(7)
print(f"Area of Rectangle: {R1.area()}")
print(f"Area of Circle: {C1.area()}")
print("---------------------\n")    

#q3.3: Design a base class Employee with __init__ taking name and employee_id. Add a method get_details(). 
# Create a subclass Manager that inherits from Employee and adds an __init__ parameter for department. 

class Employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
    def get_deails(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
    def get_deails(self):
        super().get_deails()
        print(f"Department: {self.department}")    

m1 = Manager("Alice", "E123", "Sales")
m1.get_deails()

#q3.4: From Q3.1, in the Dog subclass, override the make_sound() method so that instead of just printing "Woof!", it prints "{} says: Woof Woof!".
#  Ensure the Animal's __init__ is still called correctly using super(). 

class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} makes a sound: {self.sound}")

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    def make_sound(self):
        super().make_sound()

        print(f"{self.name} says: Woof Woof!")    


d1 = Dog("Buddy", "Woof")
d1.make_sound()

#q 3.5: Extend the Employee and Manager classes. Override the get_details() method in Manager to also include the department information,
#  while still calling the Employee's get_details() using super(). 



class Employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
    def get_deails(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
    def get_deails(self):
        super().get_deails()
        print(f"Department: {self.department}")

m1 = Manager("Alice", "E123", "Sales")
m1.get_deails()


#q 3.6: Create a base class Vehicle with __init__ taking make and model, and a method start_engine(). Create a subclass ElectricCar that 
# inherits from Vehicle. Override start_engine() in ElectricCar to print "Starting electric motor silently." 
class Vehicle:
    def __init__(self, make,model):
        self.make=make
        self.model=model
    def start_engine(self):
        print(f"Starting engine of {self.make} {self.model}.")
class ElectricCar(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def start_engine(self):
        print(f"Starting electric motor silently for {self.make} {self.model}.")

e1 = ElectricCar("Tesla", "Model S")
e1.start_engine()                    