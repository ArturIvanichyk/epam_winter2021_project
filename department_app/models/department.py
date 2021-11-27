from department_app import db


class Item_department(db.Model):
    '''
    Department model used to represent departments

    '''
    __tablename__ = 'department_db'

    #: Database id of the department
    id = db.Column(db.Integer, primary_key=True)

    #: Name of the department
    name = db.Column(db.String(64), nullable=False)

    #: Organisation the department belongs to
    organisation = db.Column(db.String(64), nullable=False)

    #: average salary of the department
    avg_salary = db.Column(db.Integer, nullable=False)
    
    #: Employees working in the department
    employees = db.relationship('Item_employee', backref=db.backref('depart'))

    def __init__(self, name, organisation, avg_salary=0, employees=None):

        self.name = name

        self.organisation = organisation

        self.avg_salary = avg_salary

        if employees is None:
            employees = []
        #: Employees working in the department
        self.employees = employees

    def calculate_average_salary(emp, depart):
        '''
        Returns average salary of the department

        '''
        try:
            return int(sum(map(lambda emp: int(emp.salary), depart.employees)) / len(depart.employees))
        except ZeroDivisionError:
            return 0
