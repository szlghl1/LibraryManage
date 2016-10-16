from flask_wtf import Form
from wtforms import StringField, SubmitField

class QueryForm(Form):
    ISBN = StringField("ISBN")
    name = StringField("Name (case insensitive)")
    authors = StringField("Authors seperated by comma")
    submit = SubmitField("Press to Query")