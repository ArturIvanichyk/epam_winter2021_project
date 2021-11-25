"""
Employee views used to manage employees on web application, this module
defines the following classes:

- `EmployeeView`, class that defines employee views
"""

from flask import Blueprint, Flask, render_template, request, redirect
from department_app import db
from department_app.models.employee import Item_employee
from department_app.models.department import Item_department

employees_page = Blueprint('employees_page', __name__, template_folder='templates')


@employees_page.route("/employee", methods=['POST', 'GET'])
def employee():
    ''' 
    Show user the page which allows manage employees (add, edit, delete) 
    Collect employee's input data from forms and add it to database

    '''
    dep_items = Item_department.query.all()
    emp_items = Item_employee.query.all()
    if request.method == 'POST':
        name = request.form['name']
        birth_date = request.form['birth_date']
        salary = request.form['salary']
        depart = request.form['depart']

        for el in emp_items:
            if name == el.name and birth_date == el.birth_date:
                return redirect('/employees')

        item = Item_employee(name=name, birth_date=birth_date, salary=salary, depart=depart)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/employee')
        except:
             return "Something is wrong"
    else:
        return render_template('employee.html', dep_data=dep_items, emp_data=emp_items)



@employees_page.route("/employees")
def employees():
    '''
    Function gets employee's data from database 
    and displays it to user

    '''
    items = Item_employee.query.all()
    return render_template('employees.html', employ_data=items)


@employees_page.route("/employees/<int:id>/update", methods=['POST', 'GET'])
def employees_update(id):
    '''
    Is used for updating employee's data

    '''
    items = Item_employee.query.get(id)
    if request.method == 'POST':
        items.name = request.form['name']
        items.birth_date = request.form['birth_date']
        items.salary = request.form['salary']
        items.depart = request.form['depart']
        
    try:
        db.session.commit()
        return redirect("/employee")
    except:
        return "Something is wrong"


@employees_page.route("/employees/<int:id>/del")
def employees_del(id):
    '''
    Is used for deleting employees from database

    '''
    items = Item_employee.query.get(id)
    try:
        db.session.delete(items)
        db.session.commit()
        return redirect("/employees")
    except:
        return "Something is wrong"
