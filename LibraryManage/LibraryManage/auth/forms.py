from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    user = StringField("User Name", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("Log in")

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[Required()])
    new_password = PasswordField("New Password", validators=[Required()])
    submit = SubmitField("Submit")