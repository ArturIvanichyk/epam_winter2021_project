"""
This module defines the test cases for department api

"""

import http
import json

from department_app import db, app
from department_app.models.department import Item_department
from department_app.tests.conftest import BaseTestCase

class TestDepartmentApi(BaseTestCase):
    """
    Class used for department api test cases
    """

    def test_get(self):
        """
        Testing the get request to /api/departments.
        It should return the status code 200
        """
        client = app.test_client()
        response = client.get('/api/departments')
        
        assert response.status_code == http.HTTPStatus.OK

    def test_get_department_by_id(self):
        """
        Testing the get request to /api/departments/<id>
        It should return the status code 200
        """
        department = Item_department(name='name', organisation='organisation')
        db.session.add(department)
        db.session.commit()
        
        client = app.test_client()
        url = '/api/departments/1'
        response = client.get(url)

        assert response.status_code == http.HTTPStatus.OK

    def test_post(self):
        """
        Testing the post request to /api/departments.
        It should return the status code 201
        """
        client = app.test_client()
        data = {
            'name': 'Test Name',
            'organisation': 'Test Organisation'
        }
        response = client.post('/api/departments', data=json.dumps(data),
                               content_type='application/json')
        assert response.status_code == http.HTTPStatus.CREATED

    def test_post_failure(self):
        """
        Testing the post request to /api/departments.
        It should return the status code 400
        """
        client = app.test_client()
        data1 = None
        data2 = {
            'name': '',
            'organisation': ''
        }
        response1 = client.post('/api/departments', data=json.dumps(data1),
                               content_type='application/json')
        response2 = client.post('/api/departments', data=json.dumps(data2),
                               content_type='application/json')
        assert response1.status_code == http.HTTPStatus.BAD_REQUEST
        assert response2.status_code == http.HTTPStatus.BAD_REQUEST

    def test_put(self):
        """
        Testing the put request to /api/departments/<id>
        It should return the status code 200
        """
        department = Item_department(name='Test Name1', organisation='Test Organisation1')
        db.session.add(department)
        db.session.commit()
        client = app.test_client()
        url = '/api/departments/1'
        data = {
            'name': 'Update Test Name1',
            'organisation': 'Update Test Organisation1'
        }
        response = client.put(url, data=json.dumps(data),
                              content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_put_failure(self):
        """
        Testing the put request to /api/departments/<id>
        It should return the status code 400
        """
        department = Item_department(name='Test Name1', organisation='Test Organisation1')
        db.session.add(department)
        db.session.commit()
        client = app.test_client()
        url = '/api/departments/1'
        data1 = None
        data2 = {'somekey': 'google'}
        response1 = client.put(url, data=json.dumps(data1),
                              content_type='application/json')
        response2 = client.put(url, data=json.dumps(data2),
                              content_type='application/json')        
        assert response1.status_code == http.HTTPStatus.BAD_REQUEST
        assert response2.status_code == http.HTTPStatus.BAD_REQUEST

    def test_patch(self):
        """
        Testing the patch request to /api/departments
        It should return the status code 200
        """
        department = Item_department(name='Test Name1', organisation='Test Organisation1')
        db.session.add(department)
        db.session.commit()
        client = app.test_client()
        url = '/api/departments/1'
        data = {
            'name': 'Update Test Name1'
        }
        response = client.patch(url, data=json.dumps(data),
                              content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_patch_failure(self):
        """
        Testing the patch request to /api/departments
        It should return the status code 400
        """
        department = Item_department(name='Test Name1', organisation='Test Organisation1')
        db.session.add(department)
        db.session.commit()
        client = app.test_client()
        url = '/api/departments/1'
        data = {'somekey': 'Update test name1'}
        response = client.patch(url, data=json.dumps(data),
                              content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_delete(self):
        """
        Testing the delete request to /api/departments/<id>
        It should return the status code 204
        """
        department = Item_department(name='Test Name1', organisation='Test Organisation1')
        db.session.add(department)
        db.session.commit()

        client = app.test_client()
        url = '/api/departments/1'
        response = client.delete(url)
        assert response.status_code == http.HTTPStatus.NO_CONTENT
