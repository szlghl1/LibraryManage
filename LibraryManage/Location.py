#Location.py
#Ling He
#10/2/2016

class Location:
    '''
    location of a book
    include floor, shelf and level
    '''
    def __init__(self, floor = -1, shelf = -1, level = -1):
        self.floor = floor
        self.shelf = shelf
        self.level = level