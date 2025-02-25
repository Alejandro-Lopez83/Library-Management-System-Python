"""
Library Management System

A simple Python program to manage books in a library system.
This system allows for adding, borrowing, returning, displaying and searching for books.

Author: Your Name
Date: February 25, 2025
"""


class Book:
    """
    Represents a book in the library management system.
    
    This class manages all operations related to books including adding,
    borrowing, returning, and searching functionalities.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN (International Standard Book Number) of the book.
        available (bool): Indicates if the book is available for borrowing.
    """
    
    def __init__(self, title, author, isbn, available=True):
        """
        Initialize a new Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            available (bool, optional): Whether the book is available. Defaults to True.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
    
    @staticmethod
    def add(title, author, isbn, book_list):
        """
        Add a new book to the library's collection.
        
        Validates the ISBN format and ensures no duplicates exist before adding.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            book_list (list): The list where books are stored.
            
        Returns:
            Book or None: The newly created Book object if successful, None otherwise.
        """
        # Normalize ISBN by removing hyphens and spaces
        clean_isbn = isbn.replace("-", "").replace(" ", "")
        
        # Validate ISBN format (must be 13 digits)
        if not clean_isbn.isdigit() or len(clean_isbn) != 13:
            print("Error: The ISBN must have exactly 13 numeric digits.")
            return None
        
        # Check for duplicate ISBN
        for book in book_list:
            if book.isbn == clean_isbn:
                print(f"Error: A book with ISBN {clean_isbn} already exists in the library.")
                return None
        
        # Create and add new book if validation passes
        new_book = Book(title, author, clean_isbn)
        book_list.append(new_book)
        print(f"Book '{title}' successfully added.")
        return new_book
    
    def borrow(self):
        """
        Mark the book as borrowed if it's available.
        
        Displays appropriate messages based on the operation's success.
        """
        if self.available:
            self.available = False
            print(f"The book '{self.title}' has been successfully borrowed.")
        else:
            print(f"Error: The book '{self.title}' is currently on loan.")
    
    def return_book(self):
        """
        Mark the book as returned (available) if it was borrowed.
        
        Displays appropriate messages based on the operation's success.
        """
        if not self.available:
            self.available = True
            print(f"The book '{self.title}' has been successfully returned.")
        else:
            print(f"Error: The book '{self.title}' was already available in our system.")
    
    @staticmethod
    def show(book_list):
        """
        Display all books in the library with their details.
        
        Args:
            book_list (list): The list containing all Book objects.
        """
        print("\n" + "*" * 15 + " BOOK CATALOG " + "*" * 15)
        
        if not book_list:
            print("There are no books registered in the system at this time.")
            return
        
        for i, book in enumerate(book_list, 1):
            status = "Available" if book.available else "Borrowed"
            print(f"{i}. Title: {book.title} || Author: {book.author} || ISBN: {book.isbn} || Status: {status}")
    
    @staticmethod
    def search(isbn, book_list):
        """
        Search for a book by its ISBN.
        
        Validates the ISBN format before searching and displays
        the book's information if found.
        
        Args:
            isbn (str): The ISBN to search for.
            book_list (list): The list of Book objects to search in.
            
        Returns:
            Book or None: The found Book object or None if not found.
        """
        # Normalize ISBN by removing hyphens and spaces
        clean_isbn = isbn.replace("-", "").replace(" ", "")
        
        # Validate ISBN format (must be 13 digits)
        if not clean_isbn.isdigit() or len(clean_isbn) != 13:
            print("Error: The ISBN must have exactly 13 numeric digits.")
            return None
        
        # Search for the book by ISBN
        for book in book_list:
            if book.isbn == clean_isbn:
                status = "Available" if book.available else "Borrowed"
                print(f"Book found: Title: {book.title} || Author: {book.author} || ISBN: {book.isbn} || Status: {status}")
                return book
        
        print("There are no books with that ISBN.")
        return None


def display_menu():
    """
    Display the main menu options for the library system.
    
    Returns:
        str: The user's selected option.
    """
    print("\n" + "*" * 15 + " LIBRARY SYSTEM MENU " + "*" * 15)
    print("1 - Add book")
    print("2 - Borrow book")
    print("3 - Return book")
    print("4 - Show all books")
    print("5 - Search by ISBN")
    print("6 - Exit")
    return input("Select an option (1-6): ")


def main():
    """
    The main function that runs the library management system.
    
    Creates a book collection and handles user interactions through a menu.
    """
    # Initialize empty list to store books
    books = []
    
    # Main program loop
    while True:
        option = display_menu()
        
        if option == "1":   # Add a new book
            print("\n" + "*" * 10 + " ADD NEW BOOK " + "*" * 10)
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            isbn = input("Enter the book ISBN (must contain 13 digits): ")
            Book.add(title, author, isbn, books)
            
        elif option == "2":    # Borrow a book option
            print("\n" + "*" * 10 + " BORROW BOOK " + "*" * 10)
            if not books:  # Check if the list is empty
                print("The system has no registered books. Cannot process a loan.")
            else:
                isbn = input("Enter the ISBN of the book to borrow: ")
                book = Book.search(isbn, books)
                if book:
                    book.borrow()
                
        elif option == "3":    # Return book option
            print("\n" + "*" * 10 + " RETURN BOOK " + "*" * 10)
            if not books:  # Check if the list is empty
                print("The system has no registered books. Cannot process a return.")
            else:
                isbn = input("Enter the ISBN of the book to return: ")
                book = Book.search(isbn, books)
                if book:
                    book.return_book()
                
        elif option == "4":     # Display all books option
            Book.show(books)
            
        elif option == "5":   # Search book by ISBN option
            print("\n" + "*" * 10 + " SEARCH BOOK BY ISBN " + "*" * 10)
            isbn = input("Enter the book ISBN (must contain 13 digits): ")
            Book.search(isbn, books)
            
        elif option == "6":     # Exit option
            print("Goodbye!")
            break
            
        else:
            print("\nError: You can only select an option between 1 and 6")


if __name__ == "__main__":
    """
    Entry point of the program.
    This code will only run if the script is executed directly (not imported).
    """
    main()
