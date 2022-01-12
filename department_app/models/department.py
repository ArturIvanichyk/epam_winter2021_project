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
    avg_salary = db.Column(db.Integer, nullable=True)
    
    #: Employees working in the department
    employees = db.relationship('Item_employee', backref=db.backref('depart'))


    def to_dict(self):
        '''
        Return a dictionary from its fields
        
        '''
        return {
            'id': self.id,
            'name': self.name,
            'organisation': self.organisation,
            'avg_salary': self.avg_salary,
            'employees': [employee.to_dict() for employee in self.employees]
            }
