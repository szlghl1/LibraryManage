"""
The flask application package.
"""

from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = "LibraryManageByLingHe"
bootstrap = Bootstrap(app)
from .main import main as main_blueprint
from .auth import auth as auth_blueprint
from .add_book import add_book as add_book_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(add_book_blueprint)

