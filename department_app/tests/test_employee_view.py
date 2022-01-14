
"""
This module defines the test cases for employees' views
"""
import http

from department_app import app, db
from department_app.tests.conftest import BaseTestCase
from department_app.models.employee import Item_employee


class TestEmployeeView(BaseTestCase):
    """
    This is the class for home_page view test case
    """

    def test_employee_page(self):
        """
        Testing /employee page 
        """
        client = app.test_client()
        response1 = client.get('/employee')
        response2 = client.post('/employee')
        assert response1.status_code == http.HTTPStatus.OK
        assert response2.status_code == http.HTTPStatus.BAD_REQUEST

    def test_employees_page(self):
        """
        Testing /employees page 
        """
        client = app.test_client()
        response = client.get('/employees')
        assert response.status_code == http.HTTPStatus.OK

    def test_employee_update_page(self):
        """
        Testing /employees/<id>/update page 
        """
        client = app.test_client()
        response1 = client.get('/employees/1/update')
        response2 = client.post('/employees/1/update')
        assert response1.status_code == http.HTTPStatus.FOUND
        assert response2.status_code == http.HTTPStatus.BAD_REQUEST

    def test_employee_delete_page(self):
        """
        Testing /employees/<id>/del page 
        """
        item = Item_employee(name='name', birth_date='1997-09-12', salary=1000, department_id=None)
        db.session.add(item)
        db.session.commit()

        client = app.test_client()
        response = client.get('/employees/1/del')
        assert response.status_code == http.HTTPStatus.FOUND


