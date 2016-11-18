"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, request, flash
from .forms import QueryForm
from . import main
from LibraryManage.database.Models import Book

@main.route('/')
@main.route('/home')
def home():
    """Renders the home page."""
    return redirect(url_for('main.query'))

@main.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@main.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='This is a library management system by Ling He. It helps you find the location of books you are looking for.'
    )

@main.route('/query', methods = ['GET', 'POST'])
def query():
    """query a book."""
    form = QueryForm()
    if request.method == 'POST':
        if form.ISBN.data or form.name.data or form.authors.data:
            d ={}
            if len(form.ISBN.data) != 0:
                d['ISBN'] = form.ISBN.data
            if len(form.name.data) != 0:
                d['name'] = form.name.data
            if len(form.authors.data) != 0:
                d['author'] = form.authors.data
            return render_template('showbooklist.html', title = 'Here are the books you queryed.', bookList = Book.query.filter_by(**d).all())
        else:
            flash("Please fill at least one field.")
    return render_template('book_form.html',form=form, title="Find your book here", header="Find your books by One Click!")