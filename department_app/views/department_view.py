'''
Department views used to manage departments on web application, 

'''

from flask import Blueprint, Flask, render_template, request, redirect
from department_app import db
from department_app.models.employee import Item_employee
from department_app.models.department import Item_department
from department_app.service import department_service

departments_page = Blueprint('departments_page', __name__, template_folder='templates')

@departments_page.route("/department", methods=['POST', 'GET'])
def add_department():
    ''' 
    Show user the page which allows manage departmants (add, edit, delete) 
    Collect department's input data from forms and add it to database

    '''
    dep_items = Item_department.query.all()
    if request.method == 'POST':
        try:
            name = request.form['name']
            organisation = request.form['organisation']
            
            for el in dep_items:
                if name == el.name and organisation == el.organisation:
                    return redirect('/departments')

            item = Item_department(name=name, organisation=organisation)

            db.session.add(item)
            db.session.commit()
            return redirect('/department')
        except:
            return 'Something wrong', 400
    else:
        return render_template('department.html', dep_data=dep_items)



@departments_page.route("/departments")
def show_departments():
    '''
    Function gets department's data from database 
    and displays it to user
    '''
    departments = Item_department.query.all()
    department_service.calculate_average_salary(departments)
    return render_template('departments.html', depart_data=departments)


@departments_page.route("/departments/<int:id>/update", methods=['POST', 'GET'])
def departments_update(id):
    '''
    Is used for updating department's data

    '''
    dep_items = Item_department.query.get(id)
    if request.method == 'POST':
        #: applies old data if the user doesn't specify new one
        try:
            name = request.form['name']
            if name:
                dep_items.name = name

            organisation = request.form['organisation']
            if organisation:
                dep_items.organisation = organisation
        
            db.session.commit()
        except:
            return 'Something wrong', 400
    return redirect("/departments")


@departments_page.route("/departments/<int:id>/del")
def departments_del(id):
    '''
    Is used for deleting departments

    '''
    items = Item_department.query.get(id)
    
    db.session.delete(items)
    db.session.commit()
    return redirect("/departments")
