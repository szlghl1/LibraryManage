from LibraryManage import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from LibraryManage import login_manager

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

class Admin(UserMixin, db.Model):
    __tablename__ = 'Admins'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

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
    name = db.Column(db.String(256), nullable = False)
    author = db.Column(db.String(64))
    floor = db.Column(db.Integer)
    shelf = db.Column(db.Integer)
    level = db.Column(db.Integer)
    def __repr__(self):
        return 'ISBN = %r, name = %r, floor = %r, shelf = %r, level = %r' % self.ISBN, self.name, self.floor, self.shelf, self.level

def init_db():
    db.create_all()
    admin = Admin(name = 'Ling')
    admin.password = 'password'
    db.session.add(admin)
    book1 = Book(ISBN = '12345', name = 'Cloud Computing', author = 'Ling') 
    book2 = Book(ISBN = '23456', name = 'Data Mining', author = 'Ling') 
    db.session.add(book1)
    db.session.add(book2)
    db.session.commit()

#init_db()