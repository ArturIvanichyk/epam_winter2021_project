"""
Department views used to manage departments on web application, this module
defines the following classes:

- `DepartmentView`, class that defines department views
"""

from flask import Blueprint, Flask, render_template, request, redirect
from department_app import db
from department_app.models.employee import Item_employee
from department_app.models.department import Item_department

departments_page = Blueprint('departments_page', __name__, template_folder='templates')

@departments_page.route("/department", methods=['POST', 'GET'])
def add_department():
    ''' 
    Show user the page which allows manage departmants (add, edit, delete) 
    Collect department's input data from forms and add it to database

    '''
    dep_items = Item_department.query.all()
    if request.method == 'POST':
        name = request.form['name']
        organisation = request.form['organisation']
        
        for el in dep_items:
            if name == el.name and organisation == el.organisation:
                return redirect('/departments')

        item = Item_department(name=name, organisation=organisation)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/department')
        except:
            return "Something is wrong"
    else:
        return render_template('department.html', dep_data=dep_items)



@departments_page.route("/departments")
def show_departments():
    '''
    Function gets department's data from database 
    and displays it to user
    '''
    dep_items = Item_department.query.all()
    employ_items = Item_employee.query.all()
    for el in dep_items:
        for val in employ_items:
            el.avg_salary = Item_department.calculate_average_salary(val, el)
    db.session.commit()
    return render_template('departments.html', depart_data=dep_items)


@departments_page.route("/departments/<int:id>/update", methods=['POST', 'GET'])
def departments_update(id):
    '''
    Is used for updating department's data

    '''
    items = Item_department.query.get(id)
    if request.method == 'POST':
        items.name = request.form['name']
        items.organisation = request.form['organisation']
        
    try:
        db.session.commit()
        return redirect("/department")
    except:
        return "Something is wrong"


@departments_page.route("/departments/<int:id>/del")
def departments_del(id):
    '''
    Is used for deleting departments

    '''
    items = Item_department.query.get(id)
    try:
        db.session.delete(items)
        db.session.commit()
        return redirect("/departments")
    except:
        return "Something is wrong"