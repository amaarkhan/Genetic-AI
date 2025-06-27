
# q1
#Question 1.1: Define a Python class named Dog. Inside the class, simply use pass. 
# Then, create an instance of this Dog class and assign it to a  variable named my_dog. Print the my_dog variable. 

class Dog:
    pass

my_dog = Dog()
print(my_dog)

print("---------------------\n")

#q1.2
# Modify the Dog class to include an __init__ method that takes name and breed as parameters. Initialize these as instance attributes. 
# Create two Dog objects: one named "Buddy" of "Golden Retriever" breed, and another named "Lucy" of "Labrador" breed. 
# Print the name and breed of both dogs.



class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    


my_dog1 = Dog("Buddy", "Golden Retriever")
my_dog2 = Dog("Lucy", "Labrador")
print(f"Dog 1:Name : {my_dog1.name}, Breed: {my_dog1.breed}")
print(f"Dog 2 Name: {my_dog2.name}, Breed 2 :{my_dog2.breed}")

print("---------------------\n")            

#q1.3
#  Create a class Car with an __init__ method that takes make, model, and year. 
# Add a method display_info that prints the car's make, model, and year. 
# Create three different Car objects and call display_info for each. 

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

a=Car("Toyota", "Corolla", 2020)
b=Car("Honda", "Civic", 2019)
c=Car("Ford", "Mustang", 2021)
a.display_info()
b.display_info()
c.display_info()
print("---------------------\n")            
        


