"""
Flask commands defined here.
"""
import os
from flask_script import Manager
from app import create_app
import pytest

app = create_app()
app.app_context().push()
manager = Manager(app)

@manager.command
def run():
    """ Run main application. """
    app.run()

@manager.command
def test():
    """ Run tests. """
    pytest.main(['-x', 'tests/'])

if __name__ == '__main__':
    manager.run()