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
    """ Run main application. """
    pytest.main(['-x', 'tests/'])
    # tests = unittest.TestLoader().discover('tests/')
    # print('tests: %s' % tests)
    # result = unittest.TextTestRunner(verbosity=2).run(tests)
    # if result.wasSuccessful():
    #     return 0
    # return 1

if __name__ == '__main__':
    manager.run()