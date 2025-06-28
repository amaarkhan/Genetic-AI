'''
Project 1: Simple Library Management System 
Objective: Develop an OOP-based system to manage books and users in a library. 

Concepts to Apply: 

Classes & Objects: Book, User, Library. 

Attributes & Methods: Store book details (title, author, ISBN, availability), user details (name, user ID, borrowed books), and library collection. Methods for borrowing, returning, adding/removing books, registering/unregistering users. 

Encapsulation: Make book_id, user_id, and is_available private/protected where appropriate, with public methods for access and modification. 

Inheritance (Optional but Recommended): 
User base class, with subclasses Librarian and Member. Librarian might have additional methods like add_book() or remove_book(). 
Book base class, with subclasses FictionBook and NonFictionBook, potentially having unique attributes or methods. 

Polymorphism (Optional): If you implement different User types, you could have a perform_action() method that behaves differently based on the user type (e.g., Librarian can add_book, Member can borrow_book). 

Core Features: 
Book Management: Add new books, remove existing books, search for books by title/author/ISBN.

User Management: Register new users, remove users. 

Borrowing & Returning: Allow users to borrow books (if available) and return them. 

Tracking: Keep track of which books are borrowed by which user. 

User Interface: Simple text-based menu interface for interaction. 
'''
class Book:
    def __init__(self,id,title, author, isbn, is_available):
        self.__id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_available = is_available

    def get_id(self):
        return self.__id

    def get_is_available(self):
        return self._is_available

    def set_is_available(self, is_available):
        self._is_available = is_available    
        

class User:
    def __init__(self,name,user_id,borrowed_books):
        self.name = name
        self.__user_id = user_id
        self.borrowed_books = list(borrowed_books)

    def get_user_id(self):
        return self.__user_id       

    def borrow_book(self, book):
        pass

    def return_book(self, book):
        pass

    def get_borrowed_books(self):
        pass

class Librarian(User):
    def __init__(self,user_id, name, borrowed_books=[]):
        super().__init__(name, user_id, borrowed_books)
        self.designation = "Librarian"

    def add_book(self, title, author, isbn, is_available=True):
        new_book = Book(len(self.borrowed_books) + 1, title, author, isbn, is_available)
        self.borrowed_books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def remove_book(self, book_id):
        for book in self.borrowed_books:
            if book.get_id() == book_id:
                self.borrowed_books.remove(book)
                print(f"Book with ID {book_id} removed successfully.")
                return
        print(f"Book with ID {book_id} not found.") 


class Member(User):
    def __init__(self, user_id, name, borrowed_books=[]):
        super().__init__(name, user_id, borrowed_books)
        self.designation = "Member"

    def borrow_book(self, book):
        if book.get_is_available():
            self.borrowed_books.append(book)
            book.set_is_available(False)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.set_is_available(True)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")  


    def get_borrowed_books(self):
        return [book.title for book in self.borrowed_books] if self.borrowed_books else "No books borrowed."


class Library:
    def __init__(self,books,users):     
        self.books = list(books)
        self.users = list(users)

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("Available Books:")
        for book in self.books:
            availability = "Available" if book.get_is_available() else "Not Available"
            print(f"ID: {book.get_id()}, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {availability}")



    def display_users(self):
        if not self.users:
            print("No users registered in the library.")
            return
        print("Registered Users:")
        for user in self.users:
            print(f"User ID: {user.get_user_id()}, Name: {user.name}, Borrowed Books: {user.get_borrowed_books()}")

    def register_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"User '{user.name}' registered successfully.")
        else:
            print(f"User '{user.name}' is already registered.")

    def unregister_user(self, user_id):
        for user in self.users:
            if user.get_user_id() == user_id:
                self.users.remove(user)
                print(f"User with ID {user_id} unregistered successfully.")
                return
        print(f"User with ID {user_id} not found.")


    def search_book(self):
        search_term = input("Enter book title, author, or ISBN to search: ").lower()
        found_books = [book for book in self.books if (search_term in book.title.lower() or 
                                                        search_term in book.author.lower() or 
                                                        search_term in book.isbn)]
        if found_books:
            print("Search Results:")
            for book in found_books:
                availability = "Available" if book.get_is_available() else "Not Available"
                print(f"ID: {book.get_id()}, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {availability}")
        else:
            print("No books found matching the search criteria.")



b1= Book(1, "abc", "the great khan", "09387224", True)
b2= Book(2, "xyz", "qauid-e-azam", "12334059893", True)     
b3= Book(3, "pqr", "Allama iqbal", "23456789876", True)                                   

books = [b1, b2, b3]

u1 = Librarian(1, "Ali",[])
u2 = Member(2, "Amaar",[])

users = [u1, u2]

library = Library(books, users)

print("Welcome to the Library Management System")
while True:
    print("\nMenu:")
    print("1. Display Books")
    print("2. Display Users")
    print("3. Register User")
    print("4. Unregister User")
    print("5. Search Book")
    print("6. Add Book (Librarian Only)")
    print("7. Borrow Book (Member Only)")
    print("8. Return Book (Member Only)")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.display_books()
    elif choice == '2':
        library.display_users()
    elif choice == '3':
        name = input("Enter user name: ")
        user_id = int(input("Enter user ID: "))
        user_type = input("Enter user type (Librarian/Member): ").strip().lower()
        if user_type == 'librarian':
            new_user = Librarian(user_id, name)
        else:
            new_user = Member(user_id, name)
        library.register_user(new_user)
    elif choice == '4':
        user_id = int(input("Enter user ID to unregister: "))
        library.unregister_user(user_id)
    elif choice == '5':
        library.search_book()
    elif choice == '6' and isinstance(u1, Librarian):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        library.users[0].add_book(title, author, isbn)  # Assuming the first user is a librarian
    elif choice == '7' and isinstance(u2, Member):
        book_id = int(input("Enter book ID to borrow: "))
        for book in library.books:
            if book.get_id() == book_id:
                u2.borrow_book(book)
                break
        else:
            print(f"Book with ID {book_id} not found.")
    elif choice == '8' and isinstance(u2, Member):
        book_id = int(input("Enter book ID to return: "))
        for book in u2.borrowed_books:
            if book.get_id() == book_id:
                u2.return_book(book)
                break
        else:
            print(f"Book with ID {book_id} not found in borrowed books.")
    elif choice == '9':
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print
("Invalid choice. Please try again.")
print("Invalid choice. Please try again.")


