from department_app import db
from .department import Item_department

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
    birth_date = db.Column(db.String(10), nullable=False)

    #: employee's salary
    salary = db.Column(db.Integer, nullable=False)

    #: database id of the department employee works in
    department_id = db.Column(db.Integer, db.ForeignKey('department_db.id'))

    def __init__(self, name, birth_date, salary, depart):

        self.name = name

        self.birth_date = birth_date

        self.salary = salary

        self.depart = depart


    def to_dict(self):
        '''
        Return a dictionary from its fields
        return: the employee in json format
        '''
        return {
            'id' : self.id,
            'name': self.name,
            'birth_date': self.birth_date,
            'salary': self.salary,
            'department': Item_department.query.get_or_404(self.department_id).name
            }


