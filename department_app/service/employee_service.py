from department_app import db


from department_app.models.department import Item_department
from department_app.models.employee import Item_employee

def get_all_employees():
    """
    Select all records from departments table
    
    """
   
    employees = Item_employee.query.all()
    
    return [employee.to_dict() for employee in employees]

def add_employee(name, birth_date, salary, department_id):
    '''
    Add a new department to data base

    '''
    department = Item_department.query.get_or_404(department_id)
    employee = Item_employee(
        name=name,
        birth_date=birth_date,
        salary=salary,
        depart=department
        )

    db.session.add(employee)
    db.session.commit()

def get_employee_by_id(id):
    '''
    Get a specific employee from employees table by id
    '''
    employee = Item_employee.query.get_or_404(id)
    return employee.to_dict()


def update_employee(id, name, birth_date, salary, department_id):
    '''
    Update an existing employee
    '''
    department = Item_department.query.get_or_404(department_id)
    employee = Item_employee.query.get_or_404(id)

    employee.name = name
    employee.birth_date = birth_date
    employee.salary = salary
    employee.depart = department

    db.session.commit()

def update_employee_patch(id, name, birth_date, salary, department_id):
    '''
    Update an existing employee without overwriting the unspecified elements with null
    '''
    
    employee = Item_employee.query.get_or_404(id)

    if name:
        employee.name = name

    if birth_date:
        employee.birth_date = birth_date

    if salary:
        employee.salary = salary

    if department_id:
        department = Item_department.query.get_or_404(department_id)
        employee.depart = department

    db.session.commit()

def delete_employee(id):
    '''
    Delete an employee
    '''

    employee = Item_employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

