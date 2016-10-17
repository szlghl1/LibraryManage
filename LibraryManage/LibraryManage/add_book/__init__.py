from flask import Blueprint

add_book = Blueprint('add_book', __name__)

from . import views