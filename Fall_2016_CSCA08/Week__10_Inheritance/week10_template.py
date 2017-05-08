class Book():
    def __init__(self, author, title, subject, num_pages):
        '''(Book, str, str, str, int) -> NoneType
        Initialize this book with an author's name (author), the book's
        title (title), the topic of the book (subject) and the total number
        of pages in the book (num_pages)
        REQ: num_pages > 0
        '''


    def __str__(self):
        '''(Book) -> str
        Return a string representation of this book.
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

class AutoBiography(Book):


    # an improved approach
    def __init__(self, author, title, num_pages):
        '''(AutoBiography, str, str, int) -> NoneType
        Initialize this autobiography with the Author's name (author),
        the title of the book (title), and the number of pages. The 
        subject of all autobiographies is assumed to be the life of the
        author
        REQ: num_pages > 0
        '''
        
class KidsBook(Book):
    
    MAX_KIDS_BOOK_PAGES = 10
    
    def __init__(self, author, title, subject, num_pages, min_age, max_age):
        '''(KidsBook, str, str, str, int, int, int) -> NoneType
        Initialize this kids book with the author's name (author), the
        title of the book (title), the subject that the book covers (subject)
        the total number of pages (num_pages), and the minimum and maximum
        ages for which this book is appropriate (min_age and max_age).
        
        Note that kids books are limited to 10 pages, any num_pages > 10
        will simply be truncated to 10 (I guess we'll throw out the rest
        of the pages or something)
        REQ: min_age, max_age > 0
        REQ: min_age <= max_age
        REQ: num_pages > 0
        '''
        #we're going to restrict kids books to a set number of pages

    
    def __str__(self):
        '''(KidsBook) -> str
        Return a kid-friendly string representation of this kid's book
        '''


if(__name__ != "__main__"):
    geb = Book("Douglas Hoffstadter", "Godel Escher Bach",  "strange loops", 650)
    bh = AutoBiography("Brian Harrington", "The untold story of a CS lecturer", 1000)
    vhc = KidsBook("Eric Carle", "The Very Hungry Caterpillar", "Eating disorders", 25, 2, 7)
    print(geb)
    print(bh)
    print(vhc)