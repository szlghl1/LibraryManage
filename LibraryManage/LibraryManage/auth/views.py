from flask import render_template, redirect, url_for, flash, request
from .forms import LoginForm
from . import auth

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    """Log in."""
    form = LoginForm()
    if request.method == 'POST':
       return "hello world"
    return render_template('login.html',form=form)