
  
"""
This module defines the test cases for department service
"""

from department_app import db
from department_app.models.department import Item_department
from department_app.models.employee import Item_employee
from department_app.service import employee_service
from department_app.tests.conftest import BaseTestCase


class TestDepartmentService(BaseTestCase):
    """
    This is the class for department service test cases
    """

    def test_get_all_employees(self):
        """
        Testing get_all_employees by adding new employees with
        the specified parameters and checks if the count of records is equal to 2
        """
        department = Item_department(name='name', organisation='organisation')

        employee1 = Item_employee(name='Test Name1', 
                                birth_date='1999-11-19', 
                                salary=2000, 
                                department_id=1)
        employee2 = Item_employee(name='Test Name2', 
                                birth_date='1999-11-19', 
                                salary=2000, 
                                department_id=1)

        db.session.add(department)
        db.session.add(employee1)
        db.session.add(employee2)
        
        db.session.commit()
        self.assertEqual(2, len(employee_service.get_all_employees()))

    def test_add_employee(self):
        """
        Testing add_employee by adding a new employee with
        the specified parameters and checks if the count of records is equal to 1
        """
        department = Item_department(name='name', organisation='organisation')
        db.session.add(department)
        employee_service.add_employee(name='Test Name1', 
                                birth_date='1999-11-19', 
                                salary=2000, 
                                department_id=1)
        self.assertEqual(1, Item_employee.query.count())

    def test_update_employee(self):
        """
        Testing update_employee by adding a new employee with
        the specified parameters and updates them by new records
        """
        department = Item_department(name='name', organisation='organisation')
        employee = Item_employee(name='Test Name1', 
                                birth_date='1999-11-19', 
                                salary=2000, 
                                department_id=1)
        db.session.add(department)
        db.session.add(employee)
        db.session.commit()
        employee_service.update_employee(1,
                                name='new name', 
                                birth_date='2000-12-12', 
                                salary=12, 
                                department_id=1)
        employee = Item_employee.query.get(1)
        self.assertEqual('new name', employee.name)
        self.assertEqual('2000-12-12', employee.birth_date)
        self.assertEqual(12, employee.salary)

    def test_delete_employee(self):
        """
        Testing delete_employee by adding a new employee with
        the specified parameters, deletes it and checks if the count of records is equal to 0
        """
        department = Item_department(name='name', organisation='organisation')
        employee = Item_employee(name='Test Name1', 
                                birth_date='1999-11-19', 
                                salary=2000, 
                                department_id=1)
        db.session.add(department)
        db.session.add(employee)
        db.session.commit()
        employee_service.delete_employee(1)
        self.assertEqual(0, Item_employee.query.count())

    def test_get_employee_by_id(self):
        """
        Testing get_employee_by_id by adding a new employee with
        the specified parameters and checks if the employee id is equal to 1
        """
        department = Item_department(name='name', organisation='organisation')
        employee = Item_employee(name='Test Name1', 
                                birth_date='1999-11-19', 
                                salary=2000, 
                                department_id=1)
        db.session.add(department)
        db.session.add(employee)
        db.session.commit()
        self.assertEqual(1, employee_service.get_employee_by_id(1)['id'])
