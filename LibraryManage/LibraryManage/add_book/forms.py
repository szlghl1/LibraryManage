from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required

class BookForm(FlaskForm):
    ISBN = StringField("ISBN", validators=[Required()])
    Name = StringField("Name", validators=[Required()])
    Floor = StringField("Floor", validators=[Required()])
    Shelf = StringField("Shelf", validators=[Required()])
    Level = StringField("Level", validators=[Required()])
    submit = SubmitField("Add")