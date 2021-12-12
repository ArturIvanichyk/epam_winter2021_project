import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Base configuration
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'department_app/database/dep_app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MIGRATION_DIR = os.path.join('department_app', 'migrations')