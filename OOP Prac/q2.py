# Q2.1: Building on the Car class from Q1.3, add an instance attribute current_speed initialized to 0.
#  Add two instance methods: accelerate(speed_increase) that increases current_speed 
#  brake(speed_decrease) that decreases current_speed (ensure speed doesn't go below 0). 
# Demonstrate accelerating and braking a car object. 

class Car:
    def __init__(self, make, model, year, current_speed=0):
        
        self.make = make
        self.model = model
        self.year = year
        self.current_speed = current_speed
    def accelarate(self,speed_increase):
        self.current_speed += speed_increase
        print(f"The current speed of the {self.make} {self.model} is now {self.current_speed} km/h.")
    def brake(self, speed_decrease):
        if self.current_speed - speed_decrease < 0:
            self.current_speed = 0
        else:
            self.current_speed -= speed_decrease
        print(f"The current speed of the {self.make} {self.model} is now {self.current_speed} km/h.")


a=Car("Toyota", "Corolla", 2020,20)
a.accelarate(30)
a.brake(10)
a.brake(50)  


#q2.2 Question 2.2: Create a Student class. Its __init__ method should take name and student_id.
#  Add an instance method enroll_course(course_name) which adds the course_name to a list of courses associated with the student. 
# Add another method get_courses() that returns the list of enrolled courses.

class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.courses = []

    def enroll_course(self,course_name):
        self.courses.append(course_name)

    def get_courses(self):
        return self.courses

s1 = Student("Alice", "S123")
s1.enroll_course("Math")
s1.enroll_course("Science")
print(f"Student Name: {s1.name}, ID: {s1.id}, Enrolled Courses: {s1.get_courses()}")    


#Question 2.3: Design a BankAccount class. Its __init__ should take account_number and initial_balance.
#  Include instance methods deposit(amount) and withdraw
#(amount). Ensure withdrawals cannot go below zero balance. 

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

b1 = BankAccount("123456789", 1000)
b1.deposit(500)
b1.withdraw(200)
b1.withdraw(1500)  # Attempting to withdraw more than the balance

#q2.4 Enhance the Dog class. Add a class attribute number_of_dogs initialized to 0. 
# Modify the __init__ method to increment number_of_dogs every time a new Dog object is created. 
# Add a class method get_total_dogs() that returns number_of_dogs. Create several Dog objects and 
# then print the total number of dogs using the class method. 

class Dog:
    number_of_dogs=0
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.number_of_dogs += 1
        
    def get_total_dogs(self):
        
        return Dog.number_of_dogs
        
a = Dog("Buddy", "Golden Retriever")
b= Dog("Lucy", "Labrador")

print(f"Total number of dogs: {Dog.number_of_dogs}")  

#q2.5 Question 2.5: Create a Product class. It should have a class attribute discount_rate initialized to 0.10 (10%).
#  The __init__ method should take name and price. Add an instance method get_discounted_price()
#  that calculates the price after applying the discount_rate.
#  Add a class method set_discount_rate(new_rate) that allows modifying the discount_rate. 
class Product:
    discount_rate=0.1
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_discounted_price(self):
        dis=self.price*0.1
        return self.price - dis
    @classmethod
    def set_discount_rate(cls, new_rate):
        cls.discount_rate = new_rate

a= Product("Laptop", 1000)
c=a.get_discounted_price()
print(f"Discounted price of {a.name}: {c}")


#q2.6 Design a Circle class. Add a class attribute PI set to 3.14159. The __init__ should take radius. 
# Add an instance method calculate_area(). 
# Create a class method set_pi_precision(new_pi) that allows changing the value of PI. 
class Circle:
    PI=3.14159
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return Circle.PI * (self.radius ** 2)
    @classmethod
    def set_pi_precision(cls, new_pi):
        cls.PI = new_pi

a = Circle(5)
print(f"Area of the circle with radius {a.radius}: {a.calculate_area()}")

#q2.7  In the Car class, add a static method display_general_car_safety_tips(). 
# This method should print some generic safety advice (e.g., "Always wear seatbelts.").
#  It should not access any instance or class attributes. 

class Car:
    def __init__(self, make, model, year, current_speed=0):
        
        self.make = make
        self.model = model
        self.year = year
        self.current_speed = current_speed
    def accelarate(self,speed_increase):
        self.current_speed += speed_increase
        print(f"The current speed of the {self.make} {self.model} is now {self.current_speed} km/h.")
    def brake(self, speed_decrease):
        if self.current_speed - speed_decrease < 0:
            self.current_speed = 0
        else:
            self.current_speed -= speed_decrease
        print(f"The current speed of the {self.make} {self.model} is now {self.current_speed} km/h.")

    @staticmethod
    def display_general_car_safety_tips():
        print("General Car Safety Tips:")
        print("1. Always wear seatbelts.")
        
a= Car("Toyota", "Corolla", 2020,20)
a.display_general_car_safety_tips()


#q2.8 Create a MathUtility class. Add a static method add(a, b) that returns the sum of a and b. 
# Add another static method multiply(a, b).
#  These methods should not depend on the state of any MathUtility object. 
class MathUtility:
    @staticmethod
    def add(a,b):
        return a + b
    def mul(a,b):
        return a * b
    
a= MathUtility.add(5, 10)
b = MathUtility.mul(5, 10)
print(f"Sum: {a}, Product: {b}")

#q2.9 For the Student class, add a static method generate_student_id(). 
# This method should generate a random 6-digit student ID (e.g., using random module).
#  It should not take self or cls as arguments and should not rely on any instance or class data. 

import random
class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.courses = []

    def enroll_course(self,course_name):
        self.courses.append(course_name)

    def get_courses(self):
        return self.courses
    @staticmethod
    def generate_student_id():
        return str(random.randint(100000, 999999))

s1 = Student("Alice", Student.generate_student_id())    
print(f"id student ",{s1.id})