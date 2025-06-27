#q 4.1: Create a class Person with name and age as public attributes. Create an object, access and modify these attributes directly, 
# and print them to demonstrate public access. 

class Person:
    def __init__ (self,name="abc",age=40):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1= Person("efg",50)
p1.display_info()


#q 4.2: Design a Book class with public attributes title, author, and isbn. Create a Book object and print its attributes. 
class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")


Book1 = Book("1", "ABC", "123456")
Book1.display()

#q4.3 Question 4.3: Create a class Wallet with a public attribute balance. Add methods add_money(amount) and spend_money(amount) 
# that directly modify balance. 
class Wallet:
    def __init__(self,balance=0):
        self.balance = balance
    def add_money(self, amount):
        self.balance += amount
        print(f"Added {amount}. New balance is {self.balance}.")
    def spend_money(self, amount):
        if amount > self.balance:
            print("Insufficient funds to spend.")
        else:
            self.balance -= amount
            print(f"Spent {amount}. New balance is {self.balance}.")

w1 = Wallet(100)
w1.add_money(50)
w1.spend_money(30)
w1.spend_money(150)  



#q 4.4: Modify the Person class to have _address as a protected attribute (using a single leading underscore). 
# Show that it can still be accessed directly but explain why this is discouraged. 
# Add a public method get_address() to access it. 
class Person:
    def __init__(self,name="abc",age=40,address="123 Main St"):
        self.name = name
        self.age = age
        self._address = address
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self._address}")


p2 = Person("xyz", 30, "456 tehkal indusrtial")
p2.display_info()


#q 4.5: For the BankAccount class, change account_number to _account_number to indicate it's protected.
#  Add a public method get_account_number() to safely retrieve it. 

class BankAcount:
    def __init__(self,account_no):
        self._account_no = account_no
    def get_account_no(self):
        return self._account_no    

b2 = BankAcount("123456789")
print(f"Account Number: {b2.get_account_no()}")

#q 4.6: Create a Configuration class that stores settings. Make a setting like _database_url protected. 
# Explain that while Python doesn't strictly enforce protection, it's a signal for developers. 
class Configuration:
    def __init__(self,database_url):
        self._database_url = database_url
    def get_database_url(self):
        return self._database_url

c1= Configuration("mysql://localhost:3306/mydb")
print(f"Database URL: {c1.get_database_url()}")    

#q 4.7: Modify the Person class again. Make __ssn (Social Security Number) a private attribute (using double leading underscores).
#  Try to access it directly from outside the class and observe the AttributeError. 
# Then, add a public method set_ssn(ssn) and get_ssn() to properly interact with it. 

class Person:
    def __init__(self,name="abc",age=40,address="123 Main St",ssn="52"):
        self.name = name
        self.age = age
        self._address = address
        self.__ssn = ssn
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self._address}, SSN: {self.__ssn}")


p2 = Person("xyz", 30, "456 tehkal indusrtial", "123-45-6789")
p2.display_info()
#print(f"Trying to access private SSN directly: {p2.__ssn}")  # This will raise an AttributeError



#q 4.8: In the BankAccount class, make __balance truly private. Implement deposit()
#  and withdraw() methods to be the only ways to modify the balance. Add a get_balance() method. 

class BankAccount:
    def __init__(self, account_no, initial_balance=0):
        self._account_no = account_no
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds for withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")

    def get_balance(self):
        return self.__balance
    

b3 = BankAccount("123456789", 1000)
b3.deposit(500)
b3.withdraw(200)
b3.withdraw(1500)  # Attempting to withdraw more than the balance
print(f"Current Balance: {b3.get_balance()}")  # Accessing balance through


#q4.9  .9: Design a LoginSystem class. Make __password_hash a private attribute. 
# Implement a set_password(password) method that hashes the password before storing
#  and a verify_password(password) method that checks against the stored hash. 

class LoginSystem:
    def __init__(self, password_hash):
        self.__password_hash = password_hash
    def set_password(self,password_hash):
        self.__password_hash = password_hash
    def verify_password(self, password):
        return self.__password_hash == password    
        
        
s1= LoginSystem("amaarkhanisagoodboy")
print(f"Password verification: {s1.verify_password('amaarkhanisagoodboy')}")  # Should return True
print(f"Password verification: {s1.verify_password('wrongpassword')}")  # Should