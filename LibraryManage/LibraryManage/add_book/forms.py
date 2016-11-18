from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, validators
from wtforms.validators import Required

class BookForm(FlaskForm):
    ISBN = StringField("ISBN", validators=[Required()])
    Name = StringField("Name", validators=[Required()])
    Author = StringField("Author", validators=[Required()])
    int_validator = validators.Regexp('\d+', message="integers only")
    Floor = StringField("Floor", validators=[int_validator])
    Shelf = StringField("Shelf", validators=[int_validator])
    Level = StringField("Level", validators=[int_validator])
    submit = SubmitField("Add")