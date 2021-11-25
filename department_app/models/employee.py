from department_app import db


class Item_employee(db.Model):
    '''
    Employee model used to represent employees

    '''
    #: Name of the database table storing employees
    __tablename__ = 'employee_db'

    #: employee's database id
    id = db.Column(db.Integer, primary_key=True)

    #: employee's name
    name = db.Column(db.String(64), nullable=False)

    #: employee's date of birth
    birth_date = db.Column(db.String(64), nullable=False)

    #: employee's salary
    salary = db.Column(db.Integer, nullable=False)

    #: department's name an employee works in
    depart = db.Column(db.String(64), nullable=False)


    def __init__(self, name, birth_date, salary, depart):
        #: Name of the department
        self.name = name

        #: Organisation the department belongs to
        self.birth_date = birth_date

        self.salary = salary

        self.depart = depart
