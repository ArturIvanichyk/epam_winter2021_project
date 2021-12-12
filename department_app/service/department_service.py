"""
This module consists of the CRUD operations to work with `departments` table

"""

from department_app import db


from department_app.models.department import Item_department
from department_app.models.employee import Item_employee

def calculate_average_salary(departments):
    '''
    Calculates average salary of each department

    '''
    employees = Item_employee.query.all()

    for department in departments:
        for employee in employees:
            try:
                department.avg_salary = int(sum(map(lambda employee: int(employee.salary), 
                    department.employees)) / len(department.employees))
            except ZeroDivisionError:
                department.avg_salary = 0
    db.session.commit()

def get_all_departments():
    """
    Select all records from departments table
    
    """
   
    departments = Item_department.query.all()
    calculate_average_salary(departments)
    return [department.to_dict() for department in departments]

def add_department(name, organisation):
    '''
    Add a new department to data base

    '''
    department = Item_department(name=name, organisation=organisation)

    db.session.add(department)
    db.session.commit()

def get_department_by_id(id):
    '''
    Get a specific department from departments table by id
    '''
    department = Item_department.query.get_or_404(id)
    return department.to_dict()


def update_department(id, name, organisation):
    '''
    Update an existing department
    '''
    department = Item_department.query.get_or_404(id)

    department.name = name
    department.organisation = organisation

    db.session.commit()

def update_department_patch(id, name, organisation):
    '''
    Update an existing department without overwriting the unspecified elements with null
    '''
    department = Item_department.query.get_or_404(id)

    if name:
        department.name = name

    if organisation:
        department.organisation = organisation

    db.session.commit()

def delete_department(id):
    '''
    Delete a department
    '''

    department = Item_department.query.get_or_404(id)

    db.session.delete(department)
    db.session.commit()