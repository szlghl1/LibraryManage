from LibraryManage import db

class Admin(db.Model):
    __tablename__ = 'Admins'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return '<Name %r>' % self.name

class Book(db.Model):
    '''
    A book in a library
    ISBN, name is compulsory
    optional parameters for init can include 
    authors, publishing_house, floor, shelf, level
    '''
    __tablename__ = 'Books'
    ISBN = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(256), unique = True)
    author = db.Column(db.String(64))
    floor = db.Column(db.Integer)
    shelf = db.Column(db.Integer)
    level = db.Column(db.Integer)
    def __repr__(self):
        return 'ISBN = %r, name = %r, floor = %r, shelf = %r, level = %r' % self.ISBN, self.name, self.floor, self.shelf, self.level

db.create_all()
#admin = Admin(name = 'Ling')
#db.session.add(admin)
#book1 = Book(ISBN = '12345', name = 'Cloud Computing', author = 'Ling') 
#book2 = Book(ISBN = '23456', name = 'Data Mining', author = 'Ling') 
#db.session.add(book1)
#db.session.add(book2)
#db.session.commit()