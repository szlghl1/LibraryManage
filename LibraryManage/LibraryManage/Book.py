#Book.py
#Ling He
#10/2/2016
from LibraryManage.Location import Location

class Book:
    '''
    A book in a library
    ISBN, name is compulsory
    optional parameters for init can include 
    authors, publishing_house, floor, shelf, level
    '''
    def __init__(self, ISBN, name, **kwargs):
        self.ISBN = ISBN
        self.name = name
        self.authors = ''
        self.loca = Location()
        #authors is a string like "Bob, Alice, Ling He"
        if 'authors' in kwargs:
            self.authors = kwargs['authors']
        if 'publishing_house' in kwargs:
            self.publishing_house = kwargs['publishing_house']
        if 'floor' in kwargs:
            self.loca.floor = kwargs['floor']
        if 'shelf' in kwargs:
            self.loca.shelf = kwargs['shelf']
        if 'level' in kwargs:
            self.loca.level = kwargs['level']