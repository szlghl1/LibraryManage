from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class QueryForm(FlaskForm):
    ISBN = StringField("ISBN")
    name = StringField("Name (case insensitive)")
    authors = StringField("Authors seperated by comma")
    submit = SubmitField("Press to Query")