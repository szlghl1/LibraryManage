from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, RadioField, validators
from wtforms.validators import Required

class BookForm(FlaskForm):
    ISBN = StringField("ISBN", validators=[Required()])
    Name = StringField("Name", validators=[Required()])
    Author = StringField("Author", validators=[Required()])
    Floor = IntegerField("Floor")
    Shelf = IntegerField("Shelf")
    Level = IntegerField("Level")
    submit = SubmitField("Add")