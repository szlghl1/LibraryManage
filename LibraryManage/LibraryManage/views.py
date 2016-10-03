"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from LibraryManage import app
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from LibrarySearchEngine import SearchEngine

search_engine = SearchEngine()
bootstrap = Bootstrap(app)
class NameQueryForm(Form):
    name = StringField("The name of the book", validators=[Required()])
    submit = SubmitField("Press to Query")

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return redirect(url_for('query'))

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='This is a library management system by Ling He. It helps you find the location of books you are looking for.'
    )

@app.route('/query', methods = ['GET', 'POST'])
def query():
    """query a book."""
    form = NameQueryForm()
    if form.validate_on_submit():
        print('name = ', form.name.data)
        return render_template('showbooklist.html', bookList = search_engine.search(form.name.data))
    return render_template('query.html',form=form)