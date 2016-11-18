from flask import render_template, redirect, url_for, flash, request
from .forms import LoginForm
from . import auth
from LibraryManage.database.Models import Admin
from flask_login import login_required, logout_user, login_user, current_user

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    """Log in."""
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(name=form.user.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid username or password.')
    return render_template('login.html',form=form)

@auth.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    """log out."""
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.home'))