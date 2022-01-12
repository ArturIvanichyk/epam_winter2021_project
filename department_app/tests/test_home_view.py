
"""
This module defines the test cases for home views
"""
import http

from department_app import app
from department_app.tests.conftest import BaseTestCase


class TestBaseView(BaseTestCase):
    """
    This is the class for home_page view test case
    """

    def test_homepage(self):
        """
        Testing home_page accessibility
        """
        client = app.test_client()
        response1 = client.get('/')
        response2 = client.get('/home')
        assert response1.status_code == http.HTTPStatus.OK
        assert response2.status_code == http.HTTPStatus.OK


