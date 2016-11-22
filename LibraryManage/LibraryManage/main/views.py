"""
Routes and views for the flask application.
"""

from datetime import datetime
from sqlalchemy import func
from flask import render_template, redirect, url_for, request, flash, session
from flask_login import current_user
from .forms import QueryForm
from . import main
from LibraryManage.database.Models import Book
from LibraryManage import db

@main.route('/')
@main.route('/home')
def home():
    """Renders the home page."""
    return render_template('home.html')

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
            bookList = Book.query.filter_by(**d).all()
            session['searching_conditions'] = d
            return redirect(url_for('main.show_books'))
        else:
            flash("Please fill at least one field.")
    return render_template('book_form.html',form=form, title="Find your book here", header="Find your books by One Click!")

@main.route('/show_books', methods = ['GET', 'POST'])
def show_books():
    '''
    GET: show searched books. parameters passed by cookie
    POST: delete the books you selected
    '''
    #this is for case sensitive whole comparison
    #bookList = Book.query.filter_by(**session['searching_conditions']).all()
    bookList = Book.query
    queryConditions = session['searching_conditions']
    for k in queryConditions:
        #both statements work, just think the later one should be faster
        #bookList = bookList.filter(getattr(Book, k).ilike('%' + queryConditions[k] + '%'))
        bookList = bookList.filter(func.lower(getattr(Book, k)).contains(func.lower(queryConditions[k])))
    bookList = bookList.all()
    if request.method == 'GET':
        return render_template('showbooklist.html', title = 'Here are the books you queryed.', bookList = bookList, if_deletable = current_user.is_authenticated)
    if request.method == 'POST':
        if current_user.is_authenticated:
            count = 0
            for key in request.form:
                #key is like checkbox[integer], so we can simply use the [8:]
                index = int(key[8:])
                db.session.delete(bookList[index])
                count += 1
            db.session.commit()
            flash('The selected %i books are deleted' % count)
        else:
            flash('Illegal try to delete. You do not login.')
        return redirect(url_for('main.show_books'))