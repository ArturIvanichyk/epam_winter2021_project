
"""
This module defines the test cases for employees' views
"""
import http

from department_app import app
from department_app.tests.conftest import BaseTestCase


class TestEmployeeView(BaseTestCase):
    """
    This is the class for home_page view test case
    """

    def test_employee_page(self):
        """
        Testing /employee page 
        """
        client = app.test_client()
        response = client.get('/employee')
        assert response.status_code == http.HTTPStatus.OK

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
        response = client.get('/employees/1/update')
        assert response.status_code == http.HTTPStatus.FOUND

    def test_employee_delete_page(self):
        """
        Testing /employees/<id>/del page 
        """
        client = app.test_client()
        response = client.get('/employees/1/del')
        assert response.status_code == http.HTTPStatus.OK


