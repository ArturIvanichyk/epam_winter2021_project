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

    def __init__(self, name, organisation, avg_salary):
        #: Name of the department
        self.name = name

        #: Organisation the department belongs to
        self.organisation = organisation

        self.avg_salary = avg_salary
