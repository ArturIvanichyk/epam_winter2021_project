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
import logging.config
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')

file_handler = logging.FileHandler(filename='app.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

logger = app.logger
logger.handlers.clear()
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)
app.logger.setLevel(logging.DEBUG)

werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(console_handler)
werkzeug_logger.setLevel(logging.DEBUG)


db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app, db, directory=Config.MIGRATION_DIR)

from department_app.views.homepage_view import home_page
from department_app.views.department_view import departments_page
from department_app.views.employee_view import employees_page

app.register_blueprint(home_page)
app.register_blueprint(employees_page)
app.register_blueprint(departments_page)


from department_app.rest import department_api, employee_api

api = Api(app)

api.add_resource(department_api.DepartmentListApi, '/api/departments')
api.add_resource(department_api.DepartmentApi, '/api/departments/<id>')

api.add_resource(employee_api.EmployeeListApi, '/api/employees')
api.add_resource(employee_api.EmployeeApi, '/api/employees/<id>')

from department_app import models
