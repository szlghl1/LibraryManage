"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = "LibraryManageByLingHe"
import LibraryManage.views
