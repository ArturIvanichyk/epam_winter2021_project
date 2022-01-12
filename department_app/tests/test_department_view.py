
"""
This module defines the test cases for employees' views
"""
import http

from department_app import app
from department_app.tests.conftest import BaseTestCase


class TestDepartmentView(BaseTestCase):
    """
    This is the class for home_page view test case
    """

    def test_department_page(self):
        """
        Testing /department page 
        """
        client = app.test_client()
        response = client.get('/department')
        assert response.status_code == http.HTTPStatus.OK

    def test_departments_page(self):
        """
        Testing /departments page 
        """
        client = app.test_client()
        response = client.get('/departments')
        assert response.status_code == http.HTTPStatus.OK

    def test_department_update_page(self):
        """
        Testing /departments/<id>/update page 
        """
        client = app.test_client()
        response = client.get('/departments/1/update')
        assert response.status_code == http.HTTPStatus.FOUND

    def test_department_delete_page(self):
        """
        Testing /departments/<id>/del page 
        """
        client = app.test_client()
        response = client.get('/departments/1/del')
        assert response.status_code == http.HTTPStatus.OK


