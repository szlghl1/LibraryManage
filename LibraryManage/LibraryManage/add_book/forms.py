from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required

class BookForm(Form):
    ISBN = StringField("ISBN", validators=[Required()])
    Name = StringField("Name", validators=[Required()])
    Floor = StringField("Floor", validators=[Required()])
    Shelf = StringField("Shelf", validators=[Required()])
    Level = StringField("Level", validators=[Required()])
    submit = SubmitField("Add")