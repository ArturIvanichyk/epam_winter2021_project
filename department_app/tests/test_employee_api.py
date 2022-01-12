"""
This module defines the test cases for employee api

"""

import http
import json

from department_app import db, app
from department_app.models.employee import Item_employee
from department_app.models.department import Item_department
from department_app.tests.conftest import BaseTestCase

class TestEmployeeApi(BaseTestCase):
    """
    Class used for department api test cases
    """

    def test_get(self):
        """
        Testing the get request to /api/employees.
        It should return the status code 200
        """
        client = app.test_client()
        response = client.get('/api/employees')
        
        assert response.status_code == http.HTTPStatus.OK

    def test_get_employee_by_id(self):
        """
        Testing the get request to /api/employees/<id>
        It should return the status code 200
        """
        department = Item_department(name='name', organisation='organisation')
        employee = Item_employee(name='Test Name1', 
                                birth_date='1999-11-19', 
                                salary=2000, 
                                department_id=1)
        db.session.add(department)
        db.session.add(employee)
        db.session.commit()

        client = app.test_client()
        url = '/api/employees/1'
        response = client.get(url)

        assert response.status_code == http.HTTPStatus.OK

    def test_post(self):
        """
        Testing the post request to /api/employees.
        It should return the status code 201
        """
        client = app.test_client()
        
        data = {
            'name': 'Test Name',
            'birth_date': '1999-11-19',
            'salary': 2000,
            'department_id': 1
        }
        response = client.post('/api/employees', data=json.dumps(data),
                               content_type='application/json')
        assert response.status_code == http.HTTPStatus.CREATED

    def test_put(self):
        """
        Testing the put request to /api/employees/<id>
        It should return the status code 200
        """
        employee = Item_employee(name='Test Name1', 
                                birth_date='1999-11-19',
                                salary=2000, 
                                department_id=3)
        db.session.add(employee)
        db.session.commit()
        client = app.test_client()
        url = '/api/employees/1'
        data = {
            'name': 'Update Test Name1',
            'birth_date': '2000-12-12',
            'salary': 2500,
            'department_id': 1
        }
        response = client.put(url, data=json.dumps(data),
                              content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_delete(self):
        """
        Testing the delete request to /api/employees/<id>
        It should return the status code 204
        """
        employee = Item_employee(name='Test Name1', 
                                birth_date='1999-11-19', 
                                salary=2000, 
                                department_id=3)
        db.session.add(employee)
        db.session.commit()

        client = app.test_client()
        url = '/api/employees/1'
        response = client.delete(url)
        assert response.status_code == http.HTTPStatus.NO_CONTENT
