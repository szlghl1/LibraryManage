from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class QueryForm(FlaskForm):
    ISBN = StringField("ISBN")
    name = StringField("Name")
    authors = StringField("Author")
    submit = SubmitField("Press to Query")