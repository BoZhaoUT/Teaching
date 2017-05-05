class Book():
    '''A class to represent a book'''
    
    def __init__(self, author, title, num_pages):
        '''(Book, str, str, str, int) -> NoneType
        Initialize this book with an author's name (author), the book's
        title (title) and the total number of pages in the book (num_pages)
        REQ: num_pages > 0
        '''
        pass
    
    def __str__(self):
        '''(Book) -> str
        Return a string representation of this book
        '''
        pass

    def get_title(self):
        '''(Book) -> str
        Return the title of this book
        '''
        pass

    def get_author(self):
        '''(Book) -> str
        Return the author of this book
        '''
        pass
    
        
class KidsBook(Book):
    '''A class to represent a kids book'''
    
    def __init__(self, author, title, subject, num_pages, min_age, max_age):
        '''(KidsBook, str, str, str, int, int, int) -> NoneType
        Initialize this kids book with the author's name (author), the
        title of the book (title), the total number of pages (num_pages), and
        the minimum and maximum ages for which this book is appropriate
        (min_age and max_age).
        '''
        pass
    
    def __str__(self):
        '''(KidsBook) -> str
        Return a kid-friendly string representation of this kid's book
        '''
        pass
    
    
if(__name__ == "__main__"):
    #bh = Book("Brian Harrington", "The untold story of a CS lecturer", 1000)
    #lc = KidsBook("Lewis Carroll", "Alice in Wonderland", 20, 3, 8)