from Book import Book

class SearchEngine:
    'The class used to search a book.'
    def __init__(self):
        self.bookList = [Book(0000,'Harry Potter'), 
                         Book(1234, 'Cloud Computing'),
                         Book(1234, 'Book 0'),
                         Book(1234, 'Book 1'),
                         Book(1234, 'Book 2'),
                         Book(1234, 'Book 3'),
                         ]

    def search(self, name):
        returnList = []
        for book in self.bookList:
            if name.upper() in book.name.upper():
                returnList.append(book)
        return returnList 