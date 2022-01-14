"""
This module consists of the REST operations to work with employees

"""

from flask import jsonify, request
from flask_restful import Resource

from department_app.service import employee_service


class EmployeeListApi(Resource):
    """
    Class for DepartmentListApi Resource available at '/api/departments' url
    
    """
    @staticmethod
    def get():
        """
        Called when GET request is sent
        :return: all employees in json format
        """
        return jsonify(employee_service.get_all_employees())


    @staticmethod
    def post():
        '''
        Called when POST request is sent
        Add an employee with specified data
        return msgs with status code 400 in case of wrong data
        and return msg with status code 201 in case of successfull operation
        
        '''
        employee_json = request.json
        try:
            if not employee_json:
                return {'message': 'Wrong data'}, 400

            elif employee_json['name'] == '' or \
                employee_json['birth_date'] == '' or \
                employee_json['salary'] == '' or \
                employee_json['department_id'] == '':
                return {'message': 'Wrong data'}, 400
        except KeyError:
            return {'message': 'Wrong data'}, 400

        try:
            employee_service.add_employee(
                name=employee_json['name'],
                birth_date=employee_json['birth_date'],
                salary=employee_json['salary'],
                department_id=employee_json['department_id']
            )
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Employee has been successfully added', 201


class EmployeeApi(Resource):
    """
    Class for Employee Resource available at '/api/departments/<id>' url

    """
    @staticmethod
    def get(id):
        """
        Called when GET request is sent
        :return the employee with a given id in json format
        """
        return jsonify(employee_service.get_employee_by_id(id))

    @staticmethod
    def put(id):
        """
        Called when PUT request is sent
        :return: the 'Employee has been successfully updated' with status code 200
        """
        employee_json = request.json
        if not employee_json:
            return {'message': 'Wrong data'}, 400
        try:
            employee_service.update_employee(
                id,
                name=employee_json['name'],
                birth_date=employee_json['birth_date'],
                salary=employee_json['salary'],
                department_id=employee_json['department_id']

            )
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Employee has been successfully updated', 200

    @staticmethod
    def patch(id):
        """
        Called when PATCH request is sent
        Update an existing employee without overwriting the unspecified elements

        """
        employee_json = request.json

        if not employee_json.get('name') and \
           not employee_json.get('birth_date') and \
           not employee_json.get('salary') and \
           not employee_json.get('department_id'):
            return {'message': 'Wrong data'}, 400

        try:
            employee_service.update_employee_patch(
                id,
                name=employee_json.get('name'),
                birth_date=employee_json.get('birth_date'),
                salary=employee_json.get('salary'),
                department_id=employee_json.get('department_id')
            )
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return "Employee has been successfully updated", 200

    @staticmethod
    def delete(id):
        """
        Called when DELETE request is sent
        Delete employee
        """
        employee_service.delete_employee(id)
        return "Employee has been deleted", 204