class Library:
    def __init__(self):
        self.books = []  
    
    def add_book(self, title):
        self.books.append(title)  
        print(f"Added: {title}")
    
    def show_books(self):
        if not self.books:  
            print("No books in the library")
        else:
            print("Books in the library:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")


lib = Library()


lib.add_book("The Great Gatsby")
lib.add_book("To Kill a Mockingbird")
lib.add_book("1984")


lib.show_books()
