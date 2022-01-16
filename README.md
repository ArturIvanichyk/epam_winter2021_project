[![Coverage Status](https://coveralls.io/repos/github/ArturIvanichyk/epam_winter2021_project/badge.svg?branch=main)](https://coveralls.io/github/ArturIvanichyk/epam_winter2021_project?branch=main)(92)


# Department App

Department App is a simple web application for managing departments and employees. 
It uses RESTful web service to perform CRUD operations.
The user is allowed to:

1. Check the lists of departments with department name, description, employee count and average salary  columns. 
   
    Employee count and average salary are calculated automatically based on employees data
   

2. Check the lists of employees with employee name, department in which the employee is, salary and birthday columns.


3. Perform operations with departments such as adding, editing, deleting
   

4. Perform operations with employees such as adding, assigning, editing, deleting
***
### Start using the application

Python must already be installed
***
### Deployment

1. Clone the repo: 
   
   * `git clone https://github.com/ArturIvanichyk/epam_winter2021_project`
    
2. Create the virtual environment in project:

   * `cd epam_winter2021_project-main`

   * `python -m venv env`
   
   * `source venv/bin/activate`
   
3. Install project requirements:

   * `pip install -r requirements.txt`

4. Run the migration scripts to create database schema:
       
   * `flask db init` - further use is optional, in case of intentional reinstallation
   
   * `flask db migrate`
     
   * `flask db update`
***
##### After these steps you should see the home page of the application

![alt text](documentation/mockups/home_page.png)
***
### API operations

* ###### /api/departments

    * GET - get all departments in json format
    * POST - create a new department:
    
    `{'name': 'department', 'organisation': 'department organisation' }`

* ###### /api/departments/id

    * GET - get the department with a given id in json format
    * PUT - ***completely*** update the department with a given id (every field required)
      
      `{'name': 'updated department', 'organisation': 'updated department organisation' }`
      
    * PATCH - ***partially*** update the department with a given id
      
      `{'name': 'Research' }` or
      
      `{'organisation': 'Google' }`
      
    * DELETE - delete the department with a given id

* ###### /api/employees

    * GET - get all employees in json format
    * POST - create a new employee:
      
      `{'name': 'new employee',
        'salary': '1000',
        'birthday': '1987-03-12',
        'department_id': 1,
        }`

* ###### /api/employees/id

    * GET - get the employee with a given id in json format
    * PUT - ***completely*** update the employee with a given id (every field required)
      
      `{'name': 'updated employee',
        'salary': '3000',
        'birthday': '1997-07-17',
        'department_id': 2,
        }`
      
    * PATCH - ***partially*** update the employee with a given id
      
      `{'salary': '2000'}`
      
    * DELETE - delete the employee with a given id

