from flask import render_template, redirect, url_for, flash, request, flash
from .forms import BookForm
from . import add_book
from LibraryManage import db
from LibraryManage.database.Models import Book
from flask_login import login_required

@add_book.route('/add_book', methods = ['GET', 'POST'])
@login_required
def add_book():
    """Add a book."""
    form = BookForm()
    if form.validate_on_submit():
        book = Book(ISBN = form.ISBN.data, name = form.Name.data, author = form.Author.data,\
            floor = form.Floor.data, shelf = form.Shelf.data, level = form.Level.data) 
        db.session.add(book)
        db.session.commit()
        flash("Successfully added book.")
        return render_template('showbooklist.html', bookList = [book], title = 'The book you added.')
    return render_template('book_form.html',form=form, title="Add a book", header="Type in the information of your book.")