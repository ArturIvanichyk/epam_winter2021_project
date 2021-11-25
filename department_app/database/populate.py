"""
This module defines is used to populate database with departments and employees,
it defines the following:

Functions:

- `populate_database`: populate database with employees and departments
"""

from department_app import db
from department_app.models.employee import Item_employee
from department_app.models.department import Item_department


def populate_database():
    """
    Populate database with employees and departments

    :return: None
    """
    department_1 = Item_department('Research and Development', 'Google', 1000)
    department_2 = Item_department('Purchasing', 'Amazon', 2000)
    department_3 = Item_department('Human Resource Management', 'Huawei', 3000)

    employee_1 = Item_employee('John Doe', '02-12-1979', 2000, 'Research and Development')
    employee_2 = Item_employee('Jane Wilson', '14-05-1983', 2100, 'Purchasing')
    employee_3 = Item_employee('Will Hunting', '21-08-1988', 1800, 'Human Resource Management')

    db.session.add(department_1)
    db.session.add(department_2)
    db.session.add(department_3)

    db.session.add(employee_1)
    db.session.add(employee_2)
    db.session.add(employee_3)

    db.session.commit()
    db.session.close()

