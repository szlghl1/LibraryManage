"""
This script runs the LibraryManage application using a development server.
"""

from LibraryManage import get_app
from os import environ

application = get_app()

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    application.run(HOST, PORT)