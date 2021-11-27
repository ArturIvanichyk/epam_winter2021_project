"""
Sources root package.

Initializes web application and web service, contains following subpackages and
modules:

Subpackages:

- `database`: contains modules used to populate database
- `migrations`: contains migration files used to manage database
- `models`: contains modules with Python classes describing database models
- `rest`: contains modules with RESTful service implementation
- `service`: contains modules with classes used to work with database
- `static`: contains web application static files (scripts, styles, images)
- `templates`: contains web application html templates
- `views`: contains modules with web controllers/views
- `tests`: contains modules with unit tests
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dep_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from department_app.views.homepage_view import home_page
from department_app.views.department_view import departments_page
from department_app.views.employee_view import employees_page


db.create_all()
app.register_blueprint(home_page)
app.register_blueprint(employees_page)
app.register_blueprint(departments_page)