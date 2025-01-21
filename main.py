
class Book:
    def __init__(self, title: str, author: str, year: str, copies: int, isExclusive: bool):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.isExclusive = isExclusive

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            return True
    
    def return_book(self):
        self.copies += 1 
    
    def display_details(self, prefix = ""):
        '''Prints out all book details with an optional prefix'''
        if prefix == "":
            print(f"Wyświetlanie informacji o książce:")
        print(f"{prefix}Tytuł: {self.title}")
        print(f"{prefix}Autor: {self.author}")
        print(f"{prefix}Rok: {self.year}")
        print(f"{prefix}Liczba egzemplarzy: {self.copies}")

class Reader:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.borrowed_books: list[Book] = []
        self.max_books = 5
    
    def borrow(self,book: Book):
        '''Borrows a book and adds to borrowed books list if a book
            - is not exclusive
            - can borrow the book
            - reader has less than the max allowed books he can reserve
        '''
        if book.isExclusive == True:
            return False
        if not book.borrow_book():
            return False
        if len(self.borrowed_books) >= self.max_books:
            return False
        
        self.borrowed_books.append(book)
    
    def return_book(self,book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    
    def display_borrowed_books(self):
        '''Prints out all borrowed books for a reader'''
        print(f"Wyświetlanie wypożyczonych książek dla czytelnika '{self.first_name} {self.last_name}':")
        if len(self.borrowed_books) == 0:
            print("  - Czytelnik nie ma żadnej wypożyczonej książki")
        for borrowed_book in self.borrowed_books:
            print(f"  - {borrowed_book.author} - '{borrowed_book.title}'")

class PremiumReader(Reader):
    '''Premium reader, can borrow more books than a regular reader and can borrow exclusive books'''
    def __init__(self, first_name, last_name):
        self.max_books = 10
        super().__init__(first_name, last_name)
    
    def can_borrow_more(self) -> bool:
        if len(self.borrowed_books) < self.max_books:
            return True

    def borrow_exclusive(self, book: Book) -> bool:
        if not book.borrow_book():
            return False
        if len(self.borrowed_books) >= self.max_books:
            return False
        
        self.borrowed_books.append(book)

class Library:
    '''Library class for storing all books and readers'''
    def __init__(self):
        self.books:list[Book] = []
        self.readers:list[Reader] = []
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def add_reader(self, reader: Reader):
        self.readers.append(reader)
    
    def display_books(self):
        '''Displays all books in a library'''
        print("Wyświetlanie wszystkich książek w bibliotece:")
        for i,book in enumerate(self.books):
            book.display_details(prefix="   - ")
            if i < len(self.books) - 1:
                print("")

    def display_readers(self):
        '''Displays all readers in a library'''
        print("Wyświetlanie wszystkich czytelników w bibliotece:")
        for i,reader in enumerate(self.readers):
            print(f"   - {reader.first_name} {reader.last_name}")
            if i < len(self.books) - 1:
                print("")

def main():
    library = Library()

    book1 = Book("Czerwony Kapturek","Baśnie ludowe","1697",10,False)
    book2 = Book("Harry Potter","J.K. Rowling","1997",2,False)
    exclusiveBook1 = Book("Mein Kampf","Austriacki Malarz","1925",1,True)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(exclusiveBook1)

    reader1 = Reader("Jan","Kowalski")
    premiumReader1 = PremiumReader("Wódz","Wioski")

    library.add_reader(reader1)
    library.add_reader(premiumReader1)

    library.display_books()
    library.display_readers()

    reader1.display_borrowed_books()
    reader1.borrow(book1)
    reader1.display_borrowed_books()
    reader1.return_book(book1)
    reader1.display_borrowed_books()

    if premiumReader1.can_borrow_more():
        print(f"Użytkownik '{premiumReader1.first_name} {premiumReader1.last_name}' może wypożyczyć więcej książek")
    premiumReader1.borrow_exclusive(exclusiveBook1)
    premiumReader1.display_borrowed_books()


if __name__ == "__main__":
    main()