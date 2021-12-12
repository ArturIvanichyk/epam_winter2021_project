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

    """
    department_1 = Item_department('Research and Development', 'Google')
    department_2 = Item_department('Purchasing', 'Amazon', 2000)
    department_3 = Item_department('Human Resource Management', 'Huawei')

    employee_1 = Item_employee('John Doe', '1979-12-02', 2000, department_1)
    employee_2 = Item_employee('Jane Wilson', '1983-05-14', 2100, department_2)
    employee_3 = Item_employee('Will Hunting', '1988-03-07', 1800, department_3)

    department_1.employees = [employee_1]
    department_2.employees = [employee_2]
    department_3.employees = [employee_3]

    db.session.add(department_1)
    db.session.add(department_2)
    db.session.add(department_3)

    db.session.add(employee_1)
    db.session.add(employee_2)
    db.session.add(employee_3)

    db.session.commit()
    db.session.close()

