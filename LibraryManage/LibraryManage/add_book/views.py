from flask import render_template, redirect, url_for, flash, request
from .forms import BookForm
from . import add_book
from flask_login import login_required

@add_book.route('/add_book', methods = ['GET', 'POST'])
@login_required
def add_book():
    """Add a book."""
    form = BookForm()
    if request.method == 'POST':
        return 'Hello World!'
    return render_template('book_form.html',form=form, title="Add a book", header="Type in the information of your book.")