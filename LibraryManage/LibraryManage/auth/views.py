from flask import render_template, redirect, url_for, flash, request
from .forms import LoginForm
from . import auth
from LibraryManage.database.Models import Admin

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    """Log in."""
    form = LoginForm()
    if request.method == 'POST':
        return Admin.query.filter_by(name = 'Ling').first().id
    return render_template('login.html',form=form)