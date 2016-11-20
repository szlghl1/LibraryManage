from flask import Flask
from flask_bootstrap import Bootstrap
from os import sys, path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

app = Flask(__name__)
app.config['SECRET_KEY'] = "LibraryManageByLingHe"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://library@password@localhost/library'
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///foo.db')
bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def get_app():
    login_manager.init_app(app)
    from LibraryManage.main import main as main_blueprint
    from LibraryManage.auth import auth as auth_blueprint
    from LibraryManage.add_book import add_book as add_book_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(add_book_blueprint)
    return app

#config is in app.config
db = SQLAlchemy(app)