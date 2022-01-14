"""
This module consists of the REST operations to work with departments

"""

from flask import jsonify, request
from flask_restful import Resource

from department_app.service import department_service


class DepartmentListApi(Resource):
    """
    Class for DepartmentListApi Resource available at '/api/departments' url
    
    """
    @staticmethod
    def get():
        """
        Called when GET request is sent
        :return: all departments in json format
        """
        return jsonify(department_service.get_all_departments())

    @staticmethod
    def post():
        '''
        Called when POST request is sent
        Add a new department with specified data
        return msgs with status code 400 in case of wrong data
        and return msg with status code 201 in case of successfull operation
        
        '''
        department_json = request.json
        if not department_json:
            return {'message': 'Wrong data'}, 400

        elif department_json['name'] == '' or \
            department_json['organisation'] == '':
            return {'message': 'Wrong data'}, 400

        try:
            department_service.add_department(
                name=department_json['name'],
                organisation=department_json['organisation']
            )
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Department has been successfully added', 201


class DepartmentApi(Resource):
    """
    Class for Department Resource available at '/api/departments/<id>' url

    """
    @staticmethod
    def get(id):
        """
        Called when GET request is sent
        :return the department with a given id in json format
        """
        return jsonify(department_service.get_department_by_id(id))

    @staticmethod
    def put(id):
        """
        Called when PUT request is sent
        :return: the 'Department has been successfully updated' with status code 200
        """
        department_json = request.json
        if not department_json:
            return {'message': 'Wrong data'}, 400
        try:
            department_service.update_department(
                id,
                name=department_json['name'],
                organisation=department_json['organisation']
            )
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Department has been successfully updated', 200

    @staticmethod
    def patch(id):
        """
        Called when PATCH request is sent
        Update an existing department without overwriting the unspecified elements

        """
        department_json = request.json
        
        if not department_json.get('name') and not department_json.get('organisation'):
            return {'message': 'Wrong data'}, 400

        try:
            name = department_json['name']
            department_service.update_department_patch(
                id,
                name=department_json.get('name'),
                organisation=department_json.get('organisation')
            )
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return "Department has been successfully updated", 200

    @staticmethod
    def delete(id):
        """
        Called when DELETE request is sent
        Delete department
        """
        department_service.delete_department(id)
        return "Department has been deleted", 204