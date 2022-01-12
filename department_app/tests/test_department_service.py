
  
"""
This module defines the test cases for department service
"""

from department_app import db
from department_app.models.department import Item_department
from department_app.models.employee import Item_employee
from department_app.service import department_service
from department_app.tests.conftest import BaseTestCase


class TestDepartmentService(BaseTestCase):
    """
    This is the class for department service test cases
    """

    def test_get_all_departments(self):
        """
        Testing get_all_departments by adding new departments with
        the specified parameters and checks if the count of records is equal to 2
        """
        department1 = Item_department(name='department1', organisation='organisation1')
        department2 = Item_department(name='department2', organisation='organisation2')
        db.session.add(department1)
        db.session.add(department2)
        db.session.commit()
        self.assertEqual(2, len(department_service.get_all_departments()))

    def test_add_department(self):
        """
        Testing add_department by adding a new department with
        the specified parameters and checks if the count of records is equal to 1
        """
        department_service.add_department(name='New department', organisation='New organisation')
        self.assertEqual(1, Item_department.query.count())

    def test_update_department(self):
        """
        Testing update_department by adding a new department with
        the specified parameters and updates them by new records
        """
        department = Item_department(name='department1', organisation='organisation1')
        db.session.add(department)
        db.session.commit()
        department_service.update_department(1, name='new name', organisation='new organisation')
        department = Item_department.query.get(1)
        self.assertEqual('new name', department.name)
        self.assertEqual('new organisation', department.organisation)

    def test_delete_department(self):
        """
        Testing delete_department by adding a new department with
        the specified parameters, deletes it and checks if the count of records is equal to 0
        """
        department = Item_department(name='department1', organisation='organisation1')
        db.session.add(department)
        db.session.commit()
        department_service.delete_department(1)
        self.assertEqual(0, Item_department.query.count())

    def test_get_department_by_id(self):
        """
        Testing get_department_by_id by adding a new department with
        the specified parameters and checks if the department id is equal to 1
        """
        department = Item_department(name='department1', organisation='organisation1')
        db.session.add(department)
        db.session.commit()
        self.assertEqual(1, department_service.get_department_by_id(1)['id'])

    def test_get_average_salary(self):
        """
        Testing the average_salary by department by adding a new department and employees
        and compares the received value with the given one.
        If they are equal then the test is successful
        """
        department = Item_department(name='test_department_salary', organisation='test')
        db.session.add(department)

        employee1 = Item_employee(name='user1',
                                  birth_date='1978-04-05',
                                  salary=10000,
                                  depart=department)
        employee2 = Item_employee(name='user2',
                                  depart=department,
                                  salary=500,
                                  birth_date='1968-04-05')
        db.session.add(employee1)
        db.session.add(employee2)
        db.session.commit()
        departments = Item_department.query.all()
        department_service.calculate_average_salary(departments)
        self.assertEqual(5250, departments[0].avg_salary)