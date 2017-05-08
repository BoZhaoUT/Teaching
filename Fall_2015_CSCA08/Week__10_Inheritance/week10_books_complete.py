class Book():
    '''A class to represent a book'''
    
    def __init__(self, author, title, num_pages):
        '''(Book, str, str, str, int) -> NoneType
        
        Initialize this book with an author's name (author), the book's
        title (title) and the total number of pages in the book (num_pages)
        REQ: num_pages > 0
        '''
        self._author = author
        self._title = title
        self._pages = num_pages
    
    def __str__(self):
        '''(Book) -> str
        
        Return a string representation of this book
        '''
        return self._title + " by " + self._author
    
    def get_title(self):
        '''(Book) -> str
        
        Return the title of this book
        '''
        return self._title
    
    def get_topic(self):
        '''(Book) -> str
        
        Return the topic that this book covers
        '''
        return self._subject
    
        
class KidsBook(Book):
    '''A class to represent a kids book'''
    
    def __init__(self, author, title, num_pages, min_age, max_age):
        '''(KidsBook, str, str, str, int, int, int) -> NoneType
        Initialize this kids book with the author's name (author), the
        title of the book (title), the total number of pages (num_pages), and
        the minimum and maximum ages for which this book is appropriate
        (min_age and max_age).
        '''
        Book.__init__(self, author, title, num_pages)
        self._start_age = min_age
        self._age_rage = max_age - min_age

    
    def __str__(self):
        '''(KidsBook) -> str
        
        Return a kid-friendly string representation of this kid's book
        '''
        result = "Hi kids. Today we're going to read " + self.get_title()
        return result
    
if(__name__ == "__main__"):
    bh = Book("Brian Harrington", "The untold story of a CS lecturer", 1000)
    lc = KidsBook("Lewis Carroll", "Alice in Wonderland", 20, 3, 8)
    